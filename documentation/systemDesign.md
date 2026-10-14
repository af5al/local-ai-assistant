# System Design & Architecture

## Overview
A hybrid edge-cloud AI Assistant designed for dual-mode operation:
1. **Local Mode (Edge / Air-Gapped)**: Runs offline on consumer hardware using local Ollama models on CPU.
2. **Cloud Mode (Serverless Production)**: Deployed on Vercel and Render using high-speed serverless inference (Groq) with zero cloud infrastructure cost.

---

## Request Lifecycle & Guardrails

```mermaid
flowchart TD
    User["Client Request\n(Vercel Frontend)"] --> RateLimit["1. Rate Limiting\n(slowapi: 5 req/min)"]
    RateLimit --> Provider{"2. Hybrid LLM Provider\n(Factory Pattern)"}
    Provider -->|"Local (OLLAMA_BASE_URL)"| Ollama["Ollama Engine\n(llama3.2:1b / 3b on CPU)"]
    Provider -->|"Production (GROQ_API_KEY)"| Groq["Groq Cloud Inference\n(openai/gpt-oss-20b @ 300 TPS)"]
    Ollama -.-> Stream["StreamingResponse\n(Chunked Transfer Encoding)"]
    Groq -.-> Stream
    Stream --> Client["ReadableStream Reader\n(UI Message Bubbles)"]
