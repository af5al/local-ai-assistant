from fastapi import FastAPI
from src.provider import OllamaProvider, GroqProvider
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from src.schemas import ChatRequest
from dotenv import load_dotenv
import os

app = FastAPI()

load_dotenv()

provider_type = os.getenv("LLM_PROVIDER", "ollama")
if provider_type == "groq" and os.getenv("GROQ_API_KEY"):
    provider = GroqProvider()
else:
    provider = OllamaProvider()


raw_origins = os.getenv("ALLOWED_ORIGINS", "*")
origins = [o.strip() for o in raw_origins.split(",")] if raw_origins != "*" else ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/health')
def check_health():
    return {
        "status": "healthy",
        "environment": os.getenv("ENVIRONMENT", "development")
    }

@app.post("/chat")
def chat(req: ChatRequest):
    messages = [m.model_dump() for m in req.messages]
    return StreamingResponse(provider.chat_stream(req.model, messages), media_type="text/plain")

 

@app.get('/models')
def list_models():
    return {"models": provider.get_models()}

@app.get('/benchmarks')
def get_benchmarks_report():
    return {"benchmarks": provider.get_benchmark_reports()}