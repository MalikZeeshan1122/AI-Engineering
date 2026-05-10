# Start here — A → Z learning order

Follow this **linear path**. Folders sort by **`NN-name`** ([`README.md`](README.md) explains numbering). **[`ROADMAP.md`](ROADMAP.md)** has timelines and build ideas.

## Before day one (15 minutes)

1. Read **[`README.md`](README.md)** — how the repo works.
2. Skim **[`ROADMAP.md`](ROADMAP.md)** — five phases at a glance.
3. Seed **[`90-resources/`](90-resources/)** — add links/bookmarks as you discover them (ongoing).

## Habits — run in parallel forever

These are **not** phases; they accompany every phase.

| Order | Folder | What you do |
|-------|--------|--------------|
| A | [`01-daily-log/`](01-daily-log/) | Copy `TEMPLATE.md` → `YYYY-MM-DD.md` **every study day.** |
| B | [`02-notes/`](02-notes/) | 5–15 minutes after building: concepts, bugs, diagrams. |

---

## Phase 1 — Python + HTTP + APIs → “I can ship a small backend”

Learn core Python, then expose behavior over HTTP.

| Step | Folder | Aim |
|------|--------|-----|
| 1 | [`03-python-foundations/`](03-python-foundations/) | Functions, classes, async, typing, exercises in subfolders. |
| 2 | [`04-api-engineering/`](04-api-engineering/) | REST concepts, JSON, status codes, simple auth patterns, webhooks. |
| 3 | [`05-fastapi-projects/`](05-fastapi-projects/) | One **minimal** FastAPI service (routes, validation, `.env`). |

Optional practice: [`09-automations/`](09-automations/) — simple CLI/CSV/script once Python feels comfortable.

---

## Phase 2 — LLMs → “I can call models and ship a toy product”

| Step | Folder | Aim |
|------|--------|-----|
| 4 | [`06-llm-fundamentals/`](06-llm-fundamentals/) | Official SDKs, streaming, tokens, embeddings, tool/function calling. |
| 5 | [`07-prompt-engineering/`](07-prompt-engineering/) | Save prompts you reuse — summarize, extract, classify. |
| 6 | [`08-ai-applications/`](08-ai-applications/) | One small app end-to-end (chat + memory, or assistant). |

Sandwich messy spikes in [`92-experiments/`](92-experiments/) — promote stable code upward when it works.

---

## Phase 3 — RAG → “Retrieval systems I’d describe in an interview”

| Step | Folder | Aim |
|------|--------|-----|
| 7 | [`10-vector-databases/`](10-vector-databases/) | One local store deeply (Chroma/FAISS), then skim a hosted option if you want. |
| 8 | [`11-rag-systems/`](11-rag-systems/) | Chunk → embed → retrieve → inject → cite. |
| 9 | [`12-system-design/`](12-system-design/) | Short doc: your RAG architecture, trade-offs, failure modes. |

Begin light [`13-interview-prep/`](13-interview-prep/) here (“explain this RAG system in 5 minutes”) and keep adding through later phases.

---

## Phase 4 — Agents → “Orchestration and tools”

| Step | Folder | Aim |
|------|--------|-----|
| 10 | [`14-ai-agents/`](14-ai-agents/) | Tool loops, guardrails, simple state — **minimal framework** okay. |
| 11 | [`15-langchain/`](15-langchain/) | Chains, memory, tools/agents basics. |
| 12 | [`16-langgraph/`](16-langgraph/) | Stateful graphs, multi-step flows, optional human-in-the-loop. |
| 13 | [`17-crewai/`](17-crewai/) OR [`18-multi-agent-systems/`](18-multi-agent-systems/) | Pick one crew/pattern depth-first; sketch others in `02-notes/`. |

| Step | Folder | Aim |
|------|--------|-----|
| 14 | [`19-mcp-servers/`](19-mcp-servers/) | Build or extend one MCP server once HTTP + tools already feel familiar. |

---

## Phase 5 — Production + portfolio → “Hire-worthy”

| Step | Folder | Aim |
|------|--------|-----|
| 15 | [`20-deployment/`](20-deployment/) | Docker (or Compose), env config, logs, minimal CI idea. |
| 16 | [`05-fastapi-projects/`](05-fastapi-projects/) | **Harden** an API — auth, errors, timeouts, observability stubs. |
| 17 | [`21-portfolio-projects/`](21-portfolio-projects/) | **Only** polished pieces: README, run steps, demo link/repo link. |

| Ongoing | Folder | Aim |
|---------|--------|-----|
| — | [`09-automations/`](09-automations/) | Real integrations (email, CRM) anytime after Phase 2. |
| — | [`91-open-source/`](91-open-source/) | Log PRs/contributions whenever you contribute. |

---

## One-page cheat sheet — folder vs phase

```
PHASE 1 → 03-python-foundations → 04-api-engineering → 05-fastapi-projects
PHASE 2 → 06-llm-fundamentals → 07-prompt-engineering → 08-ai-applications
PHASE 3 → 10-vector-databases → 11-rag-systems → 12-system-design (+ 13-interview-prep light)
PHASE 4 → 14-ai-agents → 15-langchain → 16-langgraph → 17-crewai / 18-multi-agent-systems → 19-mcp-servers
PHASE 5 → 20-deployment → 05-fastapi-projects (hardened) → 21-portfolio-projects

PARALLEL → 01-daily-log, 02-notes, 90-resources (always); 92-experiments (anytime); 09-automations (≥ Phase 2)
```

Success looks like **small shipped artifacts** inside the right folders, not empty directories. Promote standout work into **`21-portfolio-projects/`** when it represents you well on a resume/GitHub profile.
