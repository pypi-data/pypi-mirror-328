"""Module for the ImageBlock class"""

from dataclasses import dataclass


@dataclass
class ImageBlock:
    """Class for image blocks in the technical drawing"""

    x: int
    y: int
    w: int
    h: int
    base64_string: str
