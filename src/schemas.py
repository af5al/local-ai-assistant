from pydantic import BaseModel

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    model: str = "llama3.2:1b"
    messages: list[ChatMessage]
    stream: bool = False