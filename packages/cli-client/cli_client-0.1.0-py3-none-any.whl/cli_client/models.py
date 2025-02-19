from pydantic import BaseModel, Field
from typing import List, Optional, Union

class TextGenerationRequest(BaseModel):
    message: str
    provider: str
    model: Optional[str] = None
    max_tokens: int = Field(default=150, ge=1)
    temperature: float = Field(default=0.7, ge=0, le=1)
    stream: bool = False
    system: Optional[str] = ""
    messages: Optional[List[dict]] = []
    reasoning_effort: Optional[str] = None
    image_bytes: Optional[Union[str, bytes]] = None