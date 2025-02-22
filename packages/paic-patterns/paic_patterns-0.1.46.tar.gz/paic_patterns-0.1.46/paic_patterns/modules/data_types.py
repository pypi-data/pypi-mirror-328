from typing import Optional, Union, List, Literal
from pydantic import BaseModel
from enum import Enum


# Add new PatternEnum class
class PaicPatternEnum(str, Enum):
    list = "list"
    list_reflection = "list-reflection"


class ModeEnum(str, Enum):
    architect = "architect"
    coder = "coder"


class ReasoningEffortV1(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class SpecTask(BaseModel):
    title: Optional[str]
    prompt: str


class SpecTaskReflection(SpecTask):
    reflection_count: Optional[int] = None
    reflection_prompt_prefix: Optional[str] = None


class SpecFileList(BaseModel):
    plan_name: str
    pattern: Union[PaicPatternEnum, str] = "list"
    architect: bool = True
    main_model: str
    editor_model: Optional[str]
    editable_context: List[str]
    readonly_context: List[str] = []
    high_level_objective: Optional[str] = None
    implementation_details: Optional[str] = None
    tasks: List[SpecTask]
    reasoning_effort: Optional[ReasoningEffortV1] = None
    config_from_task_number: Optional[int] = None


class SpecFileListReflection(SpecFileList):
    tasks: List[SpecTaskReflection]


class AICodeParams(BaseModel):
    architect: bool = True
    prompt: str
    model: str
    editor_model: Optional[str]
    editable_context: List[str]
    readonly_context: List[str] = []
    settings: Optional[dict]
    use_git: bool = True


# Add new prepared prompt type
class PreparedPrompt(BaseModel):
    task_number: int
    prompt: str
    position_number: int


class ApiPaicApiKeyRequest(BaseModel):
    type: Literal["create", "update", "validate"]
    parentUserId: Optional[str] = None  # create + update
    paicApiKey: Optional[str] = None  # validate


class ApiPaicApiKeyResponse(BaseModel):
    type: Literal["create", "update", "validate"]
    success: bool  # all
    paicApiKey: Optional[str] = None  # create + update
    error: Optional[str] = None  # all


class ApiPaicReportIssueRequest(BaseModel):
    paicApiKey: str
    issue_description: str
    no_chat_history: bool = False
    log_file: Optional[str] = None
    chat_history_file: Optional[str] = None


class ApiPaicReportIssueResponse(BaseModel):
    success: bool
    error: Optional[str] = None
