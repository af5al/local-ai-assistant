```markdown
# CI/CD Pipeline & DevOps Architecture
## Overview
The CI/CD pipeline enforces code quality, type safety, and automated test execution before changes can be deployed to production.
---
## The Automated Workflow
```mermaid
flowchart LR
    Dev["Developer\ngit push / PR"] --> CI["Continuous Integration (CI)\nGitHub Actions Runner"]
    subgraph CI_Pipeline["Automated CI Verification"]
        direction TB
        Pytest["1. Backend Test Suite\n(pytest tests/ -v)"]
        Mock["2. Mock Isolation\n(monkeypatch external APIs)"]
        TS["3. Frontend Type Check\n(tsc -b)"]
        Vite["4. Production Bundle\n(vite build)"]
    end
    CI --> CI_Pipeline
    CI_Pipeline -->|All Pass ✅| Merge["Merge to Main"]
    CI_Pipeline -->|Fail ❌| Block["Block Merge\n(Protect Production)"]
    Merge --> CD["Continuous Deployment (CD)\nAuto-deploy to Render & Vercel"]
````