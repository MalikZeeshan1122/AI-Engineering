# Python foundations

Core through **advanced** Python aimed at **AI engineering** (prompts, JSON ingestion, HTTP, typing). This directory is self-contained: notebooks, runnable scripts, algorithm drills, and reading guides live side by side.

**Full spine checklist (A→Z → artifacts):** **[`FOUNDATIONS_COVERAGE.md`](FOUNDATIONS_COVERAGE.md)** — use this when you want **every CURRICULUM letter** mapped to a notebook or script in this repo.

---

## Map of everything here

Use this table to see **what each part is for** and **where to start**.

| Location | What it is | Best for | Start |
|----------|------------|----------|--------|
| **[`exercises/`](exercises/README.md)** | **22 Jupyter notebooks** (01→22): guided lessons, demos, progressive drills A→C, exercises, collapsible solutions. Single source is regenerated from `build_curriculum_notebooks.py`. | Daily structured learning **beginner → advanced** | [`01-syntax-values-and-io.ipynb`](exercises/01-syntax-values-and-io.ipynb) |
| **[`leetcode_practice/`](leetcode_practice/README.md)** | **Interview-style problems**: stubs in `problems/`, answers in `solutions/`, `unittest` in `tests/`. Stdlib only. | Algorithm **patterns**, repetition, testing habits | [`leetcode_practice/README.md`](leetcode_practice/README.md) |
| **[`oop/`](oop/README.md)** | **3 notebooks** with daily-life analogies (blueprints, house rules, contracts/plugins). Separate generator `build_oop_notebooks.py`. | People who learn **OOP** better with stories | [`oop/01-oop-beginner-blueprints-and-objects.ipynb`](oop/01-oop-beginner-blueprints-and-objects.ipynb) |
| **`python-foundations-beginner-to-advanced.ipynb`** | **One big spiral**: explanations + runnable examples + practice parts + solutions (Parts 1–5). | **Review / cram** when you already know Python bits | Open in Jupyter / VS Code |
| **`CURRICULUM-A-Z.md`** | **Alphabet spine**: why each topic matters for LLMs/RAG/agents + ship-sized drills. | **Pick-by-topic** after the core path | Read any letter you need |
| **`FOUNDATIONS_COVERAGE.md`** | **A→Z checklist**: maps letters **A–Z** (+ SQLite/pandas/threading extras) to notebooks/scripts here. | Verify **nothing is orphaned** from the spine | Read after notebooks **01→22** |

### Runnable script folders (stdlib demos)

These folders hold **small `.py` files** you run from the terminal after reading the matching notebooks. They are **not** a second curriculum—they cement notebook ideas in plain scripts.

| Folder | Topic | Pair with notebooks |
|--------|--------|---------------------|
| **[`async/`](async/README.md)** | `asyncio`: `gather`, queues, `to_thread`, async iteration | **09**, **18** |
| **[`decorators/`](decorators/README.md)** | `@timed`, retry/backoff decorators | **07** |
| **[`generators/`](generators/README.md)** | Batching iterators, overlapping windows (chunk-shaped) | **07**, **05** |
| **[`typing/`](typing/README.md)** | `Protocol`, frozen `dataclass` configs | **08** |
| **[`logging/`](logging/README.md)** | `LoggerAdapter`, correlation-style fields | **12** |
| **[`text_processing/`](text_processing/README.md)** | Fenced JSON extraction before `json.loads` | **13** |

### Extended labs (close remaining spine gaps)

| Folder | Topic | Pair with |
|--------|--------|-----------|
| **[`sqlite_intro/`](sqlite_intro/README.md)** | **`sqlite3`** persistence & parameterized SQL | **04**, ingestion mindset |
| **[`profiling_intro/`](profiling_intro/README.md)** | **`tracemalloc`** snapshots | **16**, CURRICULUM **M** |
| **[`pandas_intro/`](pandas_intro/README.md)** | **`pandas`** toy metrics (`pip install pandas`) | **16**, tabular prelude |
| **[`threading_intro/`](threading_intro/README.md)** | **`ThreadPoolExecutor`**, **`queue.Queue`** | **09**, **18**, CURRICULUM **Q** sync |
| **[`datetime_intro/`](datetime_intro/README.md)** | **`zoneinfo`** conversions | Logs/API timestamps |
| **[`workers_intro/`](workers_intro/README.md)** | Async pipeline sketch | CURRICULUM **W**, **18** |

From **`03-python-foundations`**:

```bash
cd 03-python-foundations
python async/async_gather_demo.py
python decorators/timed_call.py
python generators/read_chunks.py
python typing/embedder_protocol.py
python logging/correlation_log_demo.py
python text_processing/extract_json_fence.py
python sqlite_intro/sqlite_mini_demo.py
python profiling_intro/tracemalloc_demo.py
python pandas_intro/explore_frame.py
python threading_intro/executor_map_demo.py
python threading_intro/queue_sync_demo.py
python datetime_intro/timezone_demo.py
python workers_intro/async_pipeline_demo.py
```

Each folder has its own **`README.md`** with file-by-file notes.

---

## Suggested learning order

1. **`exercises/`** notebooks **01 → 22** in order (see [`exercises/README.md`](exercises/README.md)).
2. **`leetcode_practice/`** in parallel once **03–07** feel comfortable (loops, functions, collections).
3. **`oop/`** anytime after **`exercises/05`**—or whenever OOP clicks better with analogies.
4. **`python-foundations-beginner-to-advanced.ipynb`** for consolidation or interview refresh.
5. **`CURRICULUM-A-Z.md`** when you need a topic letter (async, bytes, queues, …).
6. **Core script folders** (`async/`, `decorators/`, …) right **after** the linked notebook numbers in their READMEs.
7. **Extended labs** (`sqlite_intro/`, `profiling_intro/`, `pandas_intro/`, `threading_intro/`, `datetime_intro/`, `workers_intro/`) — see hub **`README.md`** table.
8. **`FOUNDATIONS_COVERAGE.md`** once through **01→22** to confirm **every A→Z letter** has an artifact mapped.

Track habits in **[`01-daily-log/README.md`](../01-daily-log/README.md)** at the repository root if you keep a learning diary.

---

## Regenerate notebooks

**Curriculum (`exercises/`):**

```bash
cd 03-python-foundations
python exercises/build_curriculum_notebooks.py
```

**OOP track (`oop/`):**

```bash
cd 03-python-foundations
python oop/build_oop_notebooks.py
```

---

## Spiral notebook quick notes

Open **`python-foundations-beginner-to-advanced.ipynb`** top to bottom:

- Parts **1–3**: explanations + runnable examples (syntax → asyncio + typing-shaped topics).
- Part **4**: practice stubs (`raise NotImplementedError`).
- Part **5**: solutions—open **after** Part 4.

If `await` fails in your runtime, use `asyncio.run(main())` as noted inside the notebook.
