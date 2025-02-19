from typing import Optional, Union, List
from pydantic import BaseModel, Field
from enum import Enum


# Add new PatternEnum class
class PaicPatternEnum(str, Enum):
    list = "list"


class ModeEnum(str, Enum):
    architect = "architect"
    coder = "coder"


class SpecTask(BaseModel):
    title: Optional[str]
    prompt: str


class SpecFileList(BaseModel):
    plan_name: str
    pattern: PaicPatternEnum = PaicPatternEnum.list  # Changed from Literal to Enum
    architect: bool = True
    main_model: str
    editor_model: Optional[str]
    editable_context: List[str]
    readonly_context: List[str] = []
    high_level_objective: Optional[str] = None
    implementation_details: Optional[str] = None
    tasks: List[SpecTask]


class AICodeParams(BaseModel):
    architect: bool = True
    prompt: str
    model: str
    editor_model: Optional[str]
    editable_context: List[str]
    readonly_context: List[str] = []
    settings: Optional[dict]
    use_git: bool = True
