# Advanced Python foundations — A → Z for AI engineers

Use this as **Day 3+ spine**: skim A→Z once, then drill topics **based on what your next project needs** (FastAPI, agents, RAG). Everything here ties to shipping reliable ML/LLM systems.

**Practice loop:** pick a letter below → write **20–40 lines** in **[`exercises/`](exercises/README.md)** notebooks, **[`leetcode_practice/`](leetcode_practice/README.md)** stubs, or a runnable script under **`async/`**, **`decorators/`**, **`generators/`**, **`typing/`**, **`logging/`**, **`text_processing/`** (see the **[hub `README.md`](README.md)** for the full map) → add **one bullet** to **[`01-daily-log/`](../01-daily-log/README.md)**.

**Quick links:** [Folder tour `README.md`](README.md) · [Notebooks `exercises/README.md`](exercises/README.md) · [Patterns `leetcode_practice/README.md`](leetcode_practice/README.md) · [Daily log `01-daily-log/README.md`](../01-daily-log/README.md)

---

## A — Async (`asyncio`, `async` / `await`)

**Why AI engineers:** streaming tokens from APIs, concurrent embeddings ingestion, HTTP + DB without blocking.

**Master:** event loop, `asyncio.gather`, task cancellation, timeouts (`asyncio.wait_for`), async context managers, **never mix blocking calls** inside async code without `asyncio.to_thread`.

**Ship-sized drill:** concurrent `httpx.AsyncClient` requests with a semaphore limit.

---

## B — Bytes & binary (`bytes`, `bytearray`, `memoryview`)

**Why:** protobuf / grpc touches, audio chunks, efficient buffer handling.

**Master:** encode/decode boundaries (UTF-8), slicing without copying where safe, reading streams.

**Ship-sized drill:** stream-read a large file in fixed-size chunks for hashing or parsing.

---

## C — Context managers (`with`, `contextlib`)

**Why:** sessions (HTTP, DB), temp files, locks, predictable teardown under errors.

**Master:** `@contextmanager`, async context managers (`async with`), composing contexts.

**Ship-sized drill:** a context that sets logging context vars (trace/request id) and restores them.

---

## D — Data modeling (`dataclasses`, `@dataclass`, frozen/slots)

**Why:** configs, messages between pipeline stages, typed payloads—precursor to Pydantic-heavy stacks.

**Master:** `frozen=True`, `slots=True`, field defaults vs factories (`default_factory`), `__post_init__`.

**Ship-sized drill:** immutable config object loaded from env + file override.

---

## E — Errors & resilience (`Exception`, custom exceptions, retries)

**Why:** flaky LLM APIs, rate limits, timeouts—production AI is mostly failure handling.

**Master:** exception hierarchies, **don’t blanket `except Exception`** without re-raise/logging, backoff vocabulary (retry vs circuit breaker concepts).

**Ship-sized drill:** wrapper that retries only idempotent GETs with jitter (concept level—libraries later).

---

## F — Functions at depth (`functools`, closures, decorators)

**Why:** cross-cutting concerns—timing, caching embeddings, auth checks—without clutter.

**Master:** `partial`, `wraps`, decorator stacking order, decorator factories.

**Ship-sized drill:** `@timed` decorator logging duration + structured extras.

---

## G — Generators & pipelines (`yield`, generator expressions)

**Why:** token/file/chunk iterators for RAG ingestion—constant memory.

**Master:** lazy evaluation, `yield from`, generator cleanup (`finally`), **chunk iterators**.

**Ship-sized drill:** generator that yields overlapping text windows for chunking.

---

## H — HTTP clients (`httpx` / `requests`)

**Why:** model APIs, vector DB REST, webhooks—your bread and butter.

**Master:** timeouts everywhere, session reuse, status checks, streaming responses (`iter_lines` / async streams).

**Ship-sized drill:** small client module with typed errors per HTTP band (4xx vs 5xx).

---

## I — Itertools & composition (`itertools`, `more-itertools`)

**Why:** batching, grouping, sliding windows—common in batch inference prep.

**Master:** `batched` (3.12+) or equivalent, `chain`, `groupby`, windowed iterators.

**Ship-sized drill:** batch iterator yielding lists of fixed size without storing whole dataset.

---

## J — JSON & schemas (`json`, `json.loads` strictness)

**Why:** APIs everywhere; structured outputs land as JSON.

**Master:** `model_validate`-style mindset even before Pydantic (validate shape manually once), handling NaN/datetime pitfalls.

**Ship-sized drill:** parse LLM JSON inside markdown fences safely (extract → parse → validate keys).

---

## K — Keyword-only & positional-only (`*, /`)

**Why:** APIs evolve—prevent accidental argument drift across refactors.

**Master:** `/` stops positional misuse; `*` forces clarity at call sites.

**Ship-sized drill:** refactor one public function signature using `/` and `*`.

---

## L — Logging (`logging`, structured logs)

**Why:** debugging prompts and pipelines in prod beats `print`.

**Master:** logger hierarchy, handlers vs formatters, **structured fields** (even if JSON logs later).

**Ship-sized drill:** logger per module + correlation id filter.

---

## M — Memory & scale (profiling mindset)

**Why:** embedding batches and token buffers blow up RAM fast.

**Master:** generators vs lists, shallow vs deep copies, knowing when to profile (`tracemalloc` snapshot basics).

**Ship-sized drill:** measure RSS before/after loading a large list vs streaming generator.

---

## N — NumPy essentials (`numpy`)

**Why:** embeddings as vectors, batch shapes `(batch, dim)`, cosine similarity speedups.

**Master:** dtypes, broadcasting rules, vectorized norms, avoiding Python loops over rows.

**Ship-sized drill:** cosine similarity matrix between query embedding and candidate matrix—vectorized.

---

## O — Object design (composition, SOLID-lite)

**Why:** agents/tools/plugins stay maintainable.

**Master:** prefer composition; thin inheritance; dependency injection style constructors.

**Ship-sized drill:** small “tool registry” pattern—register callables under string keys.

---

## P — Protocols & typing (`typing.Protocol`, structural typing)

**Why:** duck typing **with** static clarity—critical for teams and MCP-like interfaces.

**Master:** `@runtime_checkable` sparingly; Protocol vs ABC trade-offs.

**Ship-sized drill:** `Embedder` Protocol with `.embed(texts: list[str]) -> ndarray`.

---

## Q — Queues & workers (`asyncio.Queue`, `queue.Queue`)

**Why:** producer-consumer ingestion pipelines; bounded queues for backpressure.

**Master:** bounded queues, poison-pill shutdown patterns (concept).

**Ship-sized drill:** async producer embedding texts into queue; consumer drains with concurrency limit.

---

## R — Regex & text hygiene (`re`)

**Why:** preprocessing for retrieval and parsing messy logs/tool outputs.

**Master:** compiled patterns, raw strings, greed vs non-greed; **know when regex is wrong tool**.

**Ship-sized drill:** extract citations `[source: …]` patterns from generated answers.

---

## S — Shelling out safely (`subprocess`)

**Why:** calling CLI tools from pipelines—danger zone if mishandled.

**Master:** list argv vs shell=True (avoid shell=True), timeouts, capturing stderr.

**Ship-sized drill:** wrapper running `git rev-parse HEAD` with timeout + typed error.

---

## T — Advanced typing (`TypeVar`, `Generic`, `Literal`, `overload`)

**Why:** readable signatures for retrieval backends and generic repositories.

**Master:** bounded TypeVars, `ParamSpec`/`Concatenate` when wrapping functions (later skill).

**Ship-sized drill:** generic `Repository[T]` skeleton with protocol-backed storage.

---

## U — Unit testing (`pytest`)

**Why:** ML logic **does** regress—especially parsing and retrieval ranking.

**Master:** fixtures, parametrize, tmp paths, mocking HTTP at boundary (`responses`/`pytest-httpx` later).

**Ship-sized drill:** tests for JSON extraction helper from letter **J**.

---

## V — Virtual envs & reproducibility (`venv`, lockfiles mindset)

**Why:** “works on my machine” kills demos and prod.

**Master:** pinned deps philosophy (`uv pip compile`, poetry, pip-tools—pick one ecosystem).

**Ship-sized drill:** `requirements.txt` or `pyproject.toml` for one mini module + README run steps.

---

## W — Workers & jobs (mental model)

**Why:** bigger stacks use Redis/RQ/Celery—understand why queues exist.

**Master:** sync worker vs async web process separation; idempotent tasks.

**Ship-sized drill:** write pseudo-design doc in `02-notes/` for “embeddings refresh job.”

---

## X — Parsing markup (`html.parser`, optional `lxml`/`selectolax`)

**Why:** scraping docs for RAG sources—know basics even if you prefer libraries.

**Master:** DOM vs regex for HTML (prefer parsers).

**Ship-sized drill:** strip boilerplate navigation from saved HTML sample → plain text.

---

## Y — `yield` + async iteration (`async def` generators)

**Why:** streaming HTTP bodies and SSE-like flows.

**Master:** `async for`, async generators, closing generators properly.

**Ship-sized drill:** async iterator yielding fake tokens with small delays—mirror streaming UX.

---

## Z — Zip archives & artifacts (`zipfile`, layout hygiene)

**Why:** datasets and asset bundles ship as archives.

**Master:** Path-safe extraction (avoid zip-slip), listing contents without full extract.

**Ship-sized drill:** list largest files inside `.zip` without extracting entire tree.

---

## Cross-cutting checklist (what seniors actually expect)

| Skill | Signal |
|--------|--------|
| Types | Public APIs annotated; no mystery dict soup |
| Async discipline | No hidden blocking I/O in async routes |
| Errors | Mapped to HTTP/tool responses thoughtfully |
| Testing | Critical parsers & ranking logic covered |
| Packaging | Runnable README + pinned deps |

---

## Suggested order inside this folder (not alphabetical—learning order)

1. **T + P + K** — tight signatures & protocols  
2. **G + I + N** — pipelines + batches + vectors  
3. **A + H + Y** — async HTTP & streaming shape  
4. **E + L + U** — failures, logs, tests  
5. **D + J + R** — models & messy text boundaries  
6. Rest as projects demand  
7. **`leetcode_practice/`** — LeetCode-style pattern drills (`unittest`) alongside notebooks — [`leetcode_practice/README.md`](leetcode_practice/README.md)  
8. **Hub README** — full map of **`03-python-foundations/`** folders + script demos — [`README.md`](README.md)  

Return to **`START_HERE.md`** at repo root when moving to **`04-api-engineering/`**.
