"""LLMPipeline class takes images blocks from ImagePipeline and prepares the prompt for LLM model"""

from dataclasses import dataclass, field

from textwrap import dedent
from typing import Optional, List

from pydantic import BaseModel
from ..llm_backends.llm_backend import BackendFactory, LLMBackend
from ..datamodel.base_model import TechnicalDrawing, Page
from .image_pipeline import ImagePipeline


@dataclass
class LLMPipeline:
    """Class for the LLM pipeline, which is to take image blocks from ImagePipeline and prepare the prompt for LLM"""

    image_pipeline: Optional[ImagePipeline] = field(default=None)
    llm_provider: Optional[str] = field(default=None)
    llm_model: Optional[str] = field(default=None)

    def __post_init__(self):
        if self.image_pipeline is None:
            raise ValueError("ImagePipeline is required for LLMPipeline")
        if self.llm_provider is None:
            raise ValueError("LLM provider is required for LLMPipeline")
        if self.llm_model is None:
            raise ValueError("LLM model is required for LLMPipeline")

        self.client: LLMBackend = BackendFactory.create_backend(self.llm_provider, self.llm_model)

    def build_prompts(self) -> List[List]:
        """Build the prompt for the LLM model"""
        prompts: List[List] = []
        idx = 0
        if self.image_pipeline is None or self.image_pipeline.images is None:
            raise ValueError("ImagePipeline or its images attribute is not properly initialized")
        for image in self.image_pipeline.images:
            messages = []
            developer_msg = {
                "role": "developer",
                "content": dedent(
                    f"You are an assistant to help us extract information from engineering drawings. \
                        You start with a blank canvas with height {image.page_height} and width {image.page_width}\
                        We are using coordinate system from opencv. The origin (0, 0) is at top left corner.\
                        I will feed you a list of contours from cv2.findContours.\
                        For each contour you received, you will superimpose it back to the canvas for reference.\
                        Each contour is givein in the following format:\
                            id: a unique integer,\
                            x: integer, horizontal coordinate to the top-left corner of the context image,\
                            y: integer, vertical coordinate to the top-left of the context image,\
                            w: integer, width of the block,\
                            h: integer, height of the block,\
                            base64: image content\
                        At the end, you need to return the structured output."
                ),
            }
            messages.append(developer_msg)

            messages.append({"role": "user", "content": f"starting page {image.page_num}..."})
            for i, blk in enumerate(image.image_blocks):
                img_msg = {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": f"id: {idx}, page: {image.page_num},\
                                x: {blk.x}, y: {blk.y}, w: {blk.w}, h: {blk.h},\
                                    when parse measure, diameter, and feature control frame,\
                                        always look for numbers around it,\
                                        do not pass a single special symbol to the structured output.\
                                        One contour may contain multiple structured output.\
                                        E.g., one contour may have note, title block, and bom table.\
                                            one contour may have threads, meausres, diametes,\
                                                  feature control frame, and note.",
                        },
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/png;base64,{image.image_blocks[i].base64_string}"},
                        },
                    ],
                }
                messages.append(img_msg)
                idx += 1

            messages.append(
                {
                    "role": "user",
                    "content": "if there is no material column in the bom table,\
                        look for material in the description to fill up material.",
                }
            )
            messages.append(
                {
                    "role": "user",
                    "content": f"I have finished uploading all the blocks for page {image.page_num}\
                    and return requested structured output.",
                }
            )
            prompts.append(messages)
        return prompts

    def send_request(self):
        """Send the request to the LLM model"""
        results = []
        prompts = self.build_prompts()
        for prompt in prompts:
            technical_drawing: BaseModel = self.client.send_request(prompt, output_format=Page)
            results.append(technical_drawing)
        return results


def parse_drawing(pdf: bytes) -> TechnicalDrawing:
    """Parse the drawing from the PDF"""
    image_pipeline = ImagePipeline(pdf_bytes=pdf, debug=False)
    llm_pipeline = LLMPipeline(image_pipeline=image_pipeline, llm_provider="openai", llm_model="gpt-4o")
    pages = llm_pipeline.send_request()
    drawing: TechnicalDrawing = TechnicalDrawing(pages=pages)
    return drawing
