from fastapi import FastAPI
from src.provider import OllamaProvider
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from src.schemas import ChatRequest

app = FastAPI()

provider = OllamaProvider()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
def chat(req: ChatRequest):
    messages = [m.model_dump() for m in req.messages]
    return StreamingResponse(provider.chat_stream(req.model, messages), media_type="text/plain")

 

@app.get('/models')
def list_models():
    return {"models": provider.get_models()}