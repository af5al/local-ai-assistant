
---

### 3. Polish Root [README.md](file:///c:/imp-works/Job%20documents/2%20ai%20projects/local-ai-assistant/README.md) (Your Portfolio Showcase)

Update your root `README.md` with your **live URL** and **real measured benchmark data**:

```markdown
# Local AI Assistant 🤖⚡

A production-grade, full-stack AI Assistant featuring real-time token streaming, empirical hardware benchmarking, containerized deployment, and a hybrid edge-cloud architecture.

🌐 **Live Demo**: [https://local-ai-assistant-mu.vercel.app/](https://local-ai-assistant-mu.vercel.app/)  
📡 **Cloud API**: [https://local-ai-assistant-backend.onrender.com/health](https://local-ai-assistant-backend.onrender.com/health)

---

## Key Features

- **Real-Time Token Streaming**: Consumes Server-Sent Events via Python generators and browser `ReadableStream` for sub-200ms TTFT.
- **Hybrid Provider Pattern**: Automatically routes to local **Ollama** (offline/privacy) on localhost, or **Groq Cloud API** (high throughput) in production.
- **In-App Benchmarking Dashboard**: Real measured tokens/sec, latency, RAM usage (`psutil`), and JSON validation reliability.
- **Production Guardrails**: Rate-limited with `slowapi` (5 req/min) and type-validated via Pydantic v2.
- **Automated CI/CD**: GitHub Actions pipeline enforcing automated Pytest unit tests and TypeScript verification.

---

## Empirical Benchmark Results (8 GB RAM, CPU-Only Laptop)

| Model | Task | Duration | Speed (TPS) | RAM Footprint | Valid JSON? |
|---|---|---|---|---|---|
| **llama3.2:1b** | Chat / JSON | 15.5s / 3.4s | **20.7 – 24.2** | ~6.7 GB | ❌ Failed |
| **llama3.2:3b** | Chat / JSON | 20.7s / 5.3s | 8.5 – 11.0 | ~6.6 GB | ✅ Passed |
| **qwen2.5:3b** | Chat / JSON | 43.1s / 6.3s | 13.5 – 14.3 | ~7.0 GB | ✅ Passed |

> **Key Finding**: While `llama3.2:1b` delivers the fastest conversational throughput, 3B models (`llama3.2:3b`, `qwen2.5:3b`) are required for reliable structured JSON generation and tool-calling pipelines.

---

## Quick Start (Local Development)

### 1. Backend Setup
```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
uvicorn src.main:app --reload --port 8000
