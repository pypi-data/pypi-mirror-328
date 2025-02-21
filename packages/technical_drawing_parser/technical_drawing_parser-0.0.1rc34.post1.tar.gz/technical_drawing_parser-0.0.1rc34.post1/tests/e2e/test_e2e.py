from pathlib import Path
from technical_drawing_parser.pipeline.image_pipeline import ImagePipeline
from technical_drawing_parser.pipeline.llm_pipeline import parse_drawing
import json

script_dir = Path(__file__).parent.parent
pdf_path = script_dir / "pdf_drawings"
output_path = script_dir / "output"


def proprecess_image_from_bytes(file: Path):
    with open(file.resolve(), "rb") as pdf:
        print(file)
        ImagePipeline(pdf_bytes=pdf.read(), debug=True, file_name=file.stem, dst_path=str(output_path))


def llm_pipeline(file: Path):
    technical_drawing = None
    with open(file, "rb") as pdf:
        technical_drawing = parse_drawing(pdf.read())
    if technical_drawing is not None:
        print(file)
        with open(f"{output_path}/{file.stem}.json", "w", encoding="utf-8") as f:
            json.dump(technical_drawing.model_dump(mode="json"), f, indent=4, ensure_ascii=False)


# def test_image_pipeline():
#     folder_path = Path(pdf_path)
#     for file in folder_path.iterdir():
#         if file.is_file() and file.suffix.lower() == ".pdf":
#             proprecess_image_from_bytes(file)


def test_llm_pipeline():
    folder_path = Path(pdf_path)
    for file in folder_path.iterdir():
        if file.is_file() and file.suffix.lower() == ".pdf":
            llm_pipeline(file)


# def test_single_image():
#     file = pdf_path / "0051-98744_03.pdf"
#     proprecess_image_from_bytes(file)


# def test_single_pdf():
#     file = pdf_path / "0051-98744_03.pdf"
#     llm_pipeline(file)
