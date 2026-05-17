# Python foundations

Core through **advanced** Python aimed at **AI engineering** (prompts, JSON ingestion, HTTP, typing). This directory is self-contained: notebooks, runnable scripts, algorithm drills, and reading guides live side by side.

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

From **`03-python-foundations`**:

```bash
cd 03-python-foundations
python async/async_gather_demo.py
python decorators/timed_call.py
python generators/read_chunks.py
python typing/embedder_protocol.py
python logging/correlation_log_demo.py
python text_processing/extract_json_fence.py
```

Each folder has its own **`README.md`** with file-by-file notes.

---

## Suggested learning order

1. **`exercises/`** notebooks **01 → 22** in order (see [`exercises/README.md`](exercises/README.md)).
2. **`leetcode_practice/`** in parallel once **03–07** feel comfortable (loops, functions, collections).
3. **`oop/`** anytime after **`exercises/05`**—or whenever OOP clicks better with analogies.
4. **`python-foundations-beginner-to-advanced.ipynb`** for consolidation or interview refresh.
5. **`CURRICULUM-A-Z.md`** when you need a topic letter (async, bytes, queues, …).
6. **Script folders** (`async/`, `decorators/`, …) right **after** the linked notebook numbers above.

Track habits in **`01-daily-log/`** at the **repository root** if you keep a learning diary.

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
