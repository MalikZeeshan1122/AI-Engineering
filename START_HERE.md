# Start here — A → Z learning order

Follow this **linear path**. Your folders stay organized by topic; **this file** defines the sequence. Keep **[`ROADMAP.md`](ROADMAP.md)** open for timelines and build ideas.

## Before day one (15 minutes)

1. Read **[`README.md`](README.md)** — how the repo works.
2. Skim **[`ROADMAP.md`](ROADMAP.md)** — five phases at a glance.
3. Seed **[`RESOURCES/`](RESOURCES/)** — add links/bookmarks as you discover them (ongoing).

## Habits — run in parallel forever

These are **not** phases; they accompany every phase.

| Order | Folder | What you do |
|-------|--------|--------------|
| A | [`DAILY_LOG/`](DAILY_LOG/) | Copy `TEMPLATE.md` → `YYYY-MM-DD.md` **every study day.** |
| B | [`NOTES/`](NOTES/) | 5–15 minutes after building: concepts, bugs, diagrams. |

---

## Phase 1 — Python + HTTP + APIs → “I can ship a small backend”

Learn core Python, then expose behavior over HTTP.

| Step | Folder | Aim |
|------|--------|-----|
| 1 | [`PYTHON_FOUNDATIONS/`](PYTHON_FOUNDATIONS/) | Functions, classes, async, typing, exercises in subfolders. |
| 2 | [`API_ENGINEERING/`](API_ENGINEERING/) | REST concepts, JSON, status codes, simple auth patterns, webhooks. |
| 3 | [`FASTAPI_PROJECTS/`](FASTAPI_PROJECTS/) | One **minimal** FastAPI service (routes, validation, `.env`). |

Optional practice: [`AUTOMATIONS/`](AUTOMATIONS/) simple CLI/CSV/script once Python feels comfortable.

---

## Phase 2 — LLMs → “I can call models and ship a toy product”

| Step | Folder | Aim |
|------|--------|-----|
| 4 | [`LLM_FUNDAMENTALS/`](LLM_FUNDAMENTALS/) | Official SDKs, streaming, tokens, embeddings, tool/function calling. |
| 5 | [`PROMPT_ENGINEERING/`](PROMPT_ENGINEERING/) | Save prompts you reuse — summarize, extract, classify. |
| 6 | [`AI_APPLICATIONS/`](AI_APPLICATIONS/) | One small app end-to-end (chat + memory, or assistant). |

Sandwich messy spikes in [`EXPERIMENTS/`](EXPERIMENTS/) — promote stable code upward when it works.

---

## Phase 3 — RAG → “Retrieval systems I’d describe in an interview”

| Step | Folder | Aim |
|------|--------|-----|
| 7 | [`VECTOR_DATABASES/`](VECTOR_DATABASES/) | One local store deeply (Chroma/FAISS), then skim a hosted option if you want. |
| 8 | [`RAG_SYSTEMS/`](RAG_SYSTEMS/) | Chunk → embed → retrieve → inject → cite. |
| 9 | [`SYSTEM_DESIGN/`](SYSTEM_DESIGN/) | Short doc: your RAG architecture, trade-offs, failure modes. |

Begin light [`INTERVIEW_PREP/`](INTERVIEW_PREP/) here (“explain this RAG system in 5 minutes”) and keep adding through later phases.

---

## Phase 4 — Agents → “Orchestration and tools”

| Step | Folder | Aim |
|------|--------|-----|
| 10 | [`AI_AGENTS/`](AI_AGENTS/) | Tool loops, guardrails, simple state — **minimal framework** okay. |
| 11 | [`LANGCHAIN/`](LANGCHAIN/) | Chains, memory, tools/agents basics. |
| 12 | [`LANGGRAPH/`](LANGGRAPH/) | Stateful graphs, multi-step flows, optional human-in-the-loop. |
| 13 | [`CREWAI/`](CREWAI/) OR [`MULTI_AGENT_SYSTEMS/`](MULTI_AGENT_SYSTEMS/) | Pick one crew/pattern depth-first; sketch others in NOTES. |

| Step | Folder | Aim |
|------|--------|-----|
| 14 | [`MCP_SERVERS/`](MCP_SERVERS/) | Build or extend one MCP server once HTTP + tools already feel familiar. |

---

## Phase 5 — Production + portfolio → “Hire-worthy”

| Step | Folder | Aim |
|------|--------|-----|
| 15 | [`DEPLOYMENT/`](DEPLOYMENT/) | Docker (or Compose), env config, logs, minimal CI idea. |
| 16 | [`FASTAPI_PROJECTS/`](FASTAPI_PROJECTS/) | **Harden** an API — auth, errors, timeouts, observability stubs. |
| 17 | [`PORTFOLIO_PROJECTS/`](PORTFOLIO_PROJECTS/) | **Only** polished pieces: README, run steps, demo link/repo link. |

| Ongoing | Folder | Aim |
|---------|--------|-----|
| — | [`AUTOMATIONS/`](AUTOMATIONS/) | Real integrations (email, CRM) anytime after Phase 2. |
| — | [`OPEN_SOURCE/`](OPEN_SOURCE/) | Log PRs/contributions whenever you contribute. |

---

## One-page cheat sheet — folder vs phase

```
PHASE 1  → PYTHON_FOUNDATIONS → API_ENGINEERING → FASTAPI_PROJECTS
PHASE 2  → LLM_FUNDAMENTALS → PROMPT_ENGINEERING → AI_APPLICATIONS
PHASE 3  → VECTOR_DATABASES → RAG_SYSTEMS → SYSTEM_DESIGN (+ INTERVIEW_PREP light)
PHASE 4  → AI_AGENTS → LANGCHAIN → LANGGRAPH → CREWAI / MULTI_AGENT_SYSTEMS → MCP_SERVERS
PHASE 5  → DEPLOYMENT → FASTAPI_PROJECTS (hardened) → PORTFOLIO_PROJECTS

PARALLEL → DAILY_LOG, NOTES, RESOURCES (always); EXPERIMENTS (anytime); AUTOMATIONS (≥ Phase 2)
```

Success looks like **small shipped artifacts** inside the right folders, not empty directories. Move work to **`PORTFOLIO_PROJECTS/`** when it represents you well on a resume/GitHub profile.
