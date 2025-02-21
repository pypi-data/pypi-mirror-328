"""Base data models for the technical drawing parser"""

import re
from typing import Optional, List
from decimal import Decimal
from enum import Enum
from pydantic import BaseModel, Field, field_validator


class Block(BaseModel):
    """Base class for all blocks in the technical drawing"""

    id: int = Field(..., description="Unique identifier for the block")
    x: int = Field(..., description="X coordinate of the block wrt top left corner of the page")
    y: int = Field(..., description="Y coordinate of the block wrt top left corner of the page")
    w: int = Field(..., description="Width of the block")
    h: int = Field(..., description="Height of the block")


class Thread(Block):
    """Class for threads in the technical drawing, currently only contains the original text content of the thread"""

    description: str = Field(..., description="Original text content of the thread")


class Tolerance(BaseModel):
    """Class for tolerance in the technical drawing."""

    upper_deviation: Optional[Decimal] = Field(None, description="The positive tolerance value, e.g. +0.02")
    lower_deviation: Optional[Decimal] = Field(
        None, description="The negative or zero tolerance value, e.g. -0.02 or 0.00"
    )

    @field_validator("upper_deviation", "lower_deviation", mode="before")  # Runs before Pydantic's conversion
    @classmethod
    def clean_decimal(cls, v):
        """Remove special symbols and leave only numerics."""
        if isinstance(v, str):
            clean_value = re.sub(r"[^\d.]", "", v)  # Remove non-numeric chars
            return Decimal(clean_value)
        return v  # If it's already a Decimal, return it unchanged


class ToleranceSourceType(Enum):
    """Tolerance source type. It can be either local or general."""

    LOCAL = "LOCAL"
    GENERAL = "GENERAL"


class Measure(Block):
    """Class for measures in the technical drawing"""

    nominal_value: Decimal = Field(..., description="Nominal value of the measure")
    tolerance: Tolerance = Field(..., description="Tolerance of the measure")
    tolerance_source: ToleranceSourceType = Field(
        ToleranceSourceType.GENERAL,
        description="Source of the tolerance value, \
            local: meaning a tolerance is provided in the same block, \
            general: if no tolerance is provided in the same block, \
            you look at the general tolerance of the drawing to decide the tolerance.",
    )

    @field_validator("nominal_value", mode="before")  # Runs before Pydantic's conversion
    @classmethod
    def clean_decimal(cls, v):
        """Remove special symbols and leave only numerics."""
        if isinstance(v, str):
            clean_value = re.sub(r"[^\d.]", "", v)  # Remove non-numeric chars
            return Decimal(clean_value)
        return v  # If it's already a Decimal, return it unchanged


class Diameter(Measure):
    """Class for diameters in the technical drawing"""

    depth: Optional[Measure] = Field(None, description="Depth of the diameter or hole")


class FeatureControlFrameType(Enum):
    """Types for feature control frame"""

    POSITION = "POSITION"
    STRAIGHTNESS = "STRAIGHTNESS"
    FLATNESS = "FLATNESS"
    CIRCULARITY = "CIRCULARITY"
    CYLINDRICITY = "CYLINDRICITY"
    PROFILE_OF_A_LINE = "PROFILE_OF_A_LINE"
    PROFILE_OF_A_SURFACE = "PROFILE_OF_A_SURFACE"
    PERPENDICULARITY = "PERPENDICULARITY"
    ANGULARITY = "ANGULARITY"
    PARALLELISM = "PARALLELISM"
    SYMMETRY = "SYMMETRY"
    CONCENTRICITY = "CONCENTRICITY"
    CIRCULAR_RUNOUT = "CIRCULAR_RUNOUT"
    TOTAL_RUNOUT = "TOTAL_RUNOUT"


class FeatureControlFrame(Block):
    """Class for feature control frames in the technical drawing"""

    type_of_control: FeatureControlFrameType = Field(
        ..., description="Look at the symbol and determine the type of the control"
    )
    tolerance: Tolerance = Field(..., description="Tolerance of the control")
    datum_reference: Optional[str] = Field(None, description="Datum reference")
    modifier: Optional[str] = Field(None, description="Modifier of the control")
    modifier_symbol_as_unicode_character: Optional[str] = Field(
        None, description="Modifier symbol as unicode character"
    )


class RequirementType(Enum):
    """Enum type for requirement"""

    MASKING = "MASKING"
    GRINDING = "GRINDING"
    POLISHING = "POLISHING"
    SAND_BLASTING = "SAND_BLASTING"
    BRUSHING = "BRUSHING"
    SHOT_PINNING = "SHOT_PINNING"
    HONING = "HONING"
    ANODIZING = "ANODIZING"
    ELECTRO_PLATING = "ELECTRO_PLATING"
    ELECTROLESS_PLATING = "ELECTROLESS_PLATING"
    PASSIVATIOIN = "PASSIVATIOIN"
    ETCHING = "ETCHING"
    CHEMICAL_CONVERSION_COATING = "CHEMICAL_CONVERSION_COATING"
    GALVANIZING = "GALVANIZING"
    HEAT_TREATMENT = "HEAT_TREATMENT"
    CASE_HARDENING = "CASE_HARDENING"
    HOT_BLACKENING = "HOT_BLACKENING"
    ANNEALING = "ANNEALING"
    POWDER_COATING = "POWDER_COATING"
    PAINTING = "PAINTING"
    CERAMIC_COATING = "CERAMIC_COATING"
    EPOXY_COATING = "EPOXY_COATING"
    THERMAL_SPRAY = "THERMAL_SPRAY"
    LASER_MARKING_OR_ENGRAVING = "LASER_MARKING_OR_ENGRAVING"
    SCREEN_OR_SILK_PRINTING = "SCREEN_OR_SILK_PRINTING"
    CHEMICAL_CLEANING = "CHEMICAL_CLEANING"
    WATER_CLEANING = "WATER_CLEANING"
    ETCH_CLEANING = "ETCH_CLEANING"


class Requirement(BaseModel):
    """Class for requirements in the technical drawing"""

    type: RequirementType = Field(..., description="Look into the original text and determine a requirement type fits")
    description: str = Field(..., description="Original text content of the requirement type in the block")


class BoMItem(Block):
    """Class for Bill of Materials (BoM) items in the technical drawing"""

    item_number: Optional[int] = Field(
        None, description="Item number of the BoM item, this is a unique integer for each bom item."
    )
    part_number: Optional[str] = Field(None, description="Part number of the BoM item")
    description: Optional[str] = Field(None, description="Description of the BoM item")
    revision: Optional[str] = Field(None, description="Revision of the BoM item")
    quantity: Optional[int] = Field(None, description="Quantity of the BoM item")
    material: Optional[str] = Field(
        None,
        description="Material of the BoM item, if there is no explict 'material column',\
            look into the description to find the material",
    )
    tolerance: Optional[Tolerance] = Field(
        None, description="Look into the description to find the tightest tolerance of the BoM item"
    )
    requirements: Optional[List[Requirement]] = Field(
        None, description="Look into the description to find requirements of the BoM item"
    )


class GeneralTolerance(BaseModel):
    """Class for general tolerance in the technical drawing"""

    decimals: Optional[str] = Field(
        None, description="Decimals/linear of the general tolerance, usually in the format of 0.1, 0.01, 0.001"
    )
    angles: Optional[str] = Field(
        None, description="Angles of the general tolerance, usually in the format of 1, 0.1, 0.01"
    )
    surfaces: Optional[str] = Field(
        None, description="Surfaces of the general tolerance, usually next to the surface roughness symbol"
    )
    description: str = Field(..., description="Original text content of the general tolerance")


class TitleBlock(Block):
    """Class for title block in the technical drawing"""

    title: Optional[str] = Field(None, description="Title in the title block")
    revision: Optional[str] = Field(None, description="Revision in the title block")
    part_number: Optional[str] = Field(None, description="Part number in the title block")
    tolerance: Optional[GeneralTolerance] = Field(None, description="General tolerance in the title block")
    material: Optional[str] = Field(None, description="Material in the title block")
    description: Optional[str] = Field(None, description="Description in the title block")
    unit: Optional[str] = Field(None, description="Unit in the title block")
    requirements: Optional[List[Requirement]] = Field(None, description="Requirements in the title block")


class Note(Block):
    """Class for note in the technical drawing"""

    material: Optional[str] = Field(None, description="Material in the note")
    tolerance: Optional[Tolerance] = Field(None, description="Tightest tolerance in the note")
    unit: Optional[str] = Field(None, description="Unit in the note")
    requirements: Optional[List[Requirement]] = Field(
        None, description="Look at the original text and decide if they belong to one of the requirements."
    )


class Page(BaseModel):
    """Class for pages in the technical drawing"""

    page_number: int = Field(..., description="Page number of the technical drawing")
    title_block: Optional[TitleBlock] = Field(None, description="Title block of the current page")
    note: Optional[Note] = Field(None, description="Note of the current page")
    bom_table: Optional[List[BoMItem]] = Field(
        None,
        description="Bill of materials table of the current page,\
            some tables are read from top to bottom,\
            some tables are read from bottom to top.",
    )
    threads: Optional[List[Thread]] = Field(None, description="Threads of the current page")
    feature_control_frames: Optional[List[FeatureControlFrame]] = Field(
        None, description="Feature control frames of the current page"
    )
    diameters: Optional[List[Diameter]] = Field(None, description="Diameters of the current page")
    measures: Optional[List[Measure]] = Field(None, description="Measures of the current page")


class TechnicalDrawing(BaseModel):
    """Class for technical drawing"""

    pages: List[Page] = Field(..., description="Pages of the technical drawing")
