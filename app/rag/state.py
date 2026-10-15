from typing import List, Literal
from typing_extensions import TypedDict
from pydantic import BaseModel, Field
from langchain_core.documents import Document

# class RouteDecision(BaseModel):
#     route: Literal["kb", "direct"] = Field(description="kb for IT/support questions; direct for greetings/simple chat")

class EvidenceGrade(BaseModel):
    grade: Literal["good", "weak"] = Field(description="Whether evidence is sufficient to answer")

class AgentState(TypedDict):
    question: str
    current_query: str
    kb_docs: List[Document]
    web_results: str
    kb_grade: str
    web_grade: str
    answer: str
    source_used: str
    retry_count: int
    trace: List[str]
    citations: List[dict] 

class RouteDecision(BaseModel):
    route: Literal["kb", "direct"] = Field(
        description="kb for anything IT/support/factual/any personal uploaded knowledge; direct only for pure greetings/chit-chat"
    )
    confidence: float = Field(
        ge=0.0, le=1.0,
        description="0-1 confidence that this route is correct",
    )