# Python foundations — step-by-step notebooks (`exercises/`)

This folder is the **main guided path**: **22 Jupyter notebooks** from beginner syntax through HTTP, HTML parsing, **NumPy**, **pytest**, and **asyncio** queues.

---

## What this folder contains

| Kind | Role |
|------|------|
| **`01-*.ipynb` … `22-*.ipynb`** | Student-facing notebooks (metadata, objectives, TOC, concepts, runnable demos). |
| **`build_curriculum_notebooks.py`** | **Generator**: editing this script and running it **rewrites all** numbered `.ipynb` files—keep changes here unless you intentionally edit a notebook by hand once. |

Everything else in **`03-python-foundations`** supports these notebooks (practice scripts, LeetCode drills, OOP spiral).

---

## Inside each notebook

1. Module metadata table — track, difficulty, workflow (**concept → demo → drills → exercise → solution**).
2. Learning objectives.
3. Table of contents aligned to numbered sections.
4. Concept sections grounded in **AI-style workflows** (prompts, JSON, retrieval-shaped tasks).
5. Runnable demos.
6. **Progressive drills — easy → harder (A → B → C)** on the same topic.
7. Formative exercises (`assert` checks where helpful).
8. Solutions in collapsed HTML `<details>` blocks.

That matches common **MOOC / bootcamp** rhythm: predictable structure, short assessments, explicit prerequisites.

---

## Recommended path (run in order)

| # | Notebook | Focus |
|---|----------|--------|
| 01 | [`01-syntax-values-and-io.ipynb`](01-syntax-values-and-io.ipynb) | Variables, strings/f-strings, booleans |
| 02 | [`02-collections-comprehensions.ipynb`](02-collections-comprehensions.ipynb) | Lists/dicts/messages, comprehensions |
| 03 | [`03-control-flow-functions.ipynb`](03-control-flow-functions.ipynb) | Loops, functions, kwargs, mutable-default trap |
| 04 | [`04-modules-json-pathlib.ipynb`](04-modules-json-pathlib.ipynb) | Imports, JSON, `pathlib`, JSONL drill |
| 05 | [`05-classes-oop.ipynb`](05-classes-oop.ipynb) | Classes, composition, chunking exercise |
| 06 | [`06-exceptions-context-managers.ipynb`](06-exceptions-context-managers.ipynb) | Exceptions, `contextmanager` |
| 07 | [`07-decorators-generators.ipynb`](07-decorators-generators.ipynb) | Decorators, generators |
| 08 | [`08-advanced-typing-protocols-dataclasses.ipynb`](08-advanced-typing-protocols-dataclasses.ipynb) | Dataclasses, `Protocol`, typed helpers |
| 09 | [`09-async-io.ipynb`](09-async-io.ipynb) | `asyncio`, `gather`, semaphore, `to_thread`, races |
| 10 | [`10-testing-debugging.ipynb`](10-testing-debugging.ipynb) | Assertions, table-driven checks |
| 11 | [`11-collections-itertools-functools.ipynb`](11-collections-itertools-functools.ipynb) | `Counter`, `defaultdict`, `itertools`, `lru_cache`, batching patterns |
| 12 | [`12-logging-for-pipelines.ipynb`](12-logging-for-pipelines.ipynb) | Module loggers, `LoggerAdapter`, propagation, noisy-library tuning |
| 13 | [`13-regex-text-extraction.ipynb`](13-regex-text-extraction.ipynb) | `re.compile`, citations, fenced JSON extraction |
| 14 | [`14-bytes-encoding-files.ipynb`](14-bytes-encoding-files.ipynb) | UTF-8 boundaries, decode `errors=`, chunked hashing |
| 15 | [`15-subprocess-and-archives.ipynb`](15-subprocess-and-archives.ipynb) | Safe `subprocess.run`, timeouts, `zipfile`, zip-slip awareness |
| 16 | [`16-numpy-embeddings-shape.ipynb`](16-numpy-embeddings-shape.ipynb) | NumPy shapes, norms, vectorized cosine scoring (`pip install numpy`) |
| 17 | [`17-pytest-fixtures-parametrize.ipynb`](17-pytest-fixtures-parametrize.ipynb) | `tmp_path`-style temps, parametrized tables (`pip install pytest`) |
| 18 | [`18-asyncio-queue-pipelines.ipynb`](18-asyncio-queue-pipelines.ipynb) | `asyncio.Queue`, bounded queues, sentinel shutdown, fan-in merge |
| 19 | [`19-httpx-http-clients.ipynb`](19-httpx-http-clients.ipynb) | Sync **`httpx`** clients, timeouts, JSON GETs, HTTP vs transport errors (`pip install httpx`) |
| 20 | [`20-positional-keyword-only-signatures.ipynb`](20-positional-keyword-only-signatures.ipynb) | Positional-only **`/`**, keyword-only **`*`**, SDK-shaped wrappers |
| 21 | [`21-venv-and-dependency-pins.ipynb`](21-venv-and-dependency-pins.ipynb) | **`venv`** workflow, **`pip`** introspection, parsing **`requirements`** pins |
| 22 | [`22-html-parser-text.ipynb`](22-html-parser-text.ipynb) | **`html.parser`**, strip **`script`/`style`**, visible text for RAG-ish cleanup |

**Extended notebooks (11 → 22)** line up with topics in [`../CURRICULUM-A-Z.md`](../CURRICULUM-A-Z.md) (collections, logging, regex, bytes, subprocess/zip, NumPy, pytest, queues, HTTP, **`/`/`*`**, pins/**venv**, HTML).

---

## Sister folders under `03-python-foundations`

| Folder | Why open it |
|--------|-------------|
| [`../leetcode_practice/`](../leetcode_practice/README.md) | Classic coding patterns + **`unittest`** (easy / medium / hard). |
| [`../oop/`](../oop/README.md) | OOP-only spiral with everyday analogies. |
| [`../async/`](../async/README.md), [`../decorators/`](../decorators/README.md), [`../generators/`](../generators/README.md), [`../typing/`](../typing/README.md), [`../logging/`](../logging/README.md), [`../text_processing/`](../text_processing/README.md) | Runnable **stdlib** scripts after specific notebooks—each README lists commands. |
| [`../../01-daily-log/README.md`](../../01-daily-log/README.md) | One Markdown file per day — pairs with **[`CURRICULUM-A-Z.md`](../CURRICULUM-A-Z.md)** practice loop. |

Then cross-check the **single-volume** spiral [`../python-foundations-beginner-to-advanced.ipynb`](../python-foundations-beginner-to-advanced.ipynb).

---

## Regenerating notebooks

After editing **`build_curriculum_notebooks.py`**:

```bash
cd exercises
python build_curriculum_notebooks.py
```

Requires Python **3.10+** (`|` unions, `list[str]` in snippets). Extra installs where noted: **`numpy`** (16), **`pytest`** (17), **`httpx`** (19).

---

## LeetCode-style drills (`leetcode_practice/`)

See **[`../leetcode_practice/README.md`](../leetcode_practice/README.md)** — stubs vs solutions vs **`unittest`**.

Sanity-check reference solutions from **`03-python-foundations`**:

```bash
cd 03-python-foundations
python -m unittest discover -s leetcode_practice/tests -p "test_reference*.py" -v
```
