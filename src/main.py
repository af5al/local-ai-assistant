from fastapi import FastAPI, Request
from src.provider import OllamaProvider, GroqProvider
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from src.schemas import ChatRequest
from dotenv import load_dotenv
import os
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler

app = FastAPI()

load_dotenv()

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

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
@limiter.limit("5/minute") # Max 5 requests per minute IP
def chat(request: Request, req: ChatRequest):
    messages = [m.model_dump() for m in req.messages]
    return StreamingResponse(provider.chat_stream(req.model, messages), media_type="text/plain")

@app.get('/models')
def list_models():
    return {"models": provider.get_models()}

@app.get('/benchmarks')
def get_benchmarks_report():
    return {"benchmarks": provider.get_benchmark_reports()}