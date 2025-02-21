"""The preprocessing pipeline, this pipeline converts pdf bytes into images and run image analysis for partitioin"""

from dataclasses import dataclass, field
from typing import List, Optional
from io import BytesIO
from pdf2image import convert_from_bytes
from pypdf import PdfReader

from ..datamodel.uptool_image import UptoolImage


@dataclass
class ImagePipeline:
    """Class for the ImagePipeline, which is to take a PDF file and convert it to images"""

    pdf_bytes: Optional[bytes] = field(default=None)
    debug: bool = field(default=False)
    file_name: str = field(default="")
    dst_path: str = field(default="")

    images: List[UptoolImage] = field(init=False)

    def __post_init__(self):
        if self.pdf_bytes is None:
            raise ValueError("Must provide pdf either in bytes or path.")
        if self.debug:
            if self.dst_path == "":
                raise ValueError(
                    "Must provide valid dst_path (destination directory) to export images when debug == True."
                )
            if self.file_name == "":
                raise ValueError(
                    "Must provide valid file_name (name of the pdf file) to export images when debug == True."
                )
        self.images: List[UptoolImage] = []
        pdf_reader = PdfReader(BytesIO(self.pdf_bytes))
        page_num: int = pdf_reader.get_num_pages()

        for i in range(page_num):
            image_at_page_i = convert_from_bytes(self.pdf_bytes, dpi=200, first_page=i + 1, last_page=i + 1)[0]
            self.images.append(
                UptoolImage(
                    i,
                    image_at_page_i,
                    self.debug,
                    self.file_name,
                    self.dst_path,
                )
            )
