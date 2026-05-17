# Foundations spine — full **A→Z** coverage map

This file answers: *“Where do I practice each letter from [`CURRICULUM-A-Z.md`](CURRICULUM-A-Z.md)?”*

**What “100%” means here:** every letter **A–Z** has at least one **primary artifact** (notebook and/or runnable script/folder) inside **`03-python-foundations/`** for the **AI-engineering foundations** scope this repo defines. Infinite depth (every library corner, every LeetCode problem, production SRE) still lives **outside** any finite course—that is normal.

| Letter | Topic | Primary artifacts | Supporting |
|--------|--------|-------------------|------------|
| **A** | Async | [`exercises/09-async-io.ipynb`](exercises/09-async-io.ipynb), [`exercises/18-asyncio-queue-pipelines.ipynb`](exercises/18-asyncio-queue-pipelines.ipynb) | [`async/`](async/README.md) |
| **B** | Bytes / binary | [`exercises/14-bytes-encoding-files.ipynb`](exercises/14-bytes-encoding-files.ipynb) | Spiral notebook bytes-shaped cells |
| **C** | Context managers | [`exercises/06-exceptions-context-managers.ipynb`](exercises/06-exceptions-context-managers.ipynb) | — |
| **D** | Dataclasses / configs | [`exercises/08-advanced-typing-protocols-dataclasses.ipynb`](exercises/08-advanced-typing-protocols-dataclasses.ipynb) | [`typing/model_config_dataclass.py`](typing/model_config_dataclass.py) |
| **E** | Errors / resilience | [`exercises/06-exceptions-context-managers.ipynb`](exercises/06-exceptions-context-managers.ipynb), [`decorators/retry_with_backoff.py`](decorators/retry_with_backoff.py) | [`leetcode_practice/`](leetcode_practice/README.md) edge cases |
| **F** | `functools` / decorators | [`exercises/07-decorators-generators.ipynb`](exercises/07-decorators-generators.ipynb), [`exercises/11-collections-itertools-functools.ipynb`](exercises/11-collections-itertools-functools.ipynb) | [`decorators/`](decorators/README.md) |
| **G** | Generators | [`exercises/07-decorators-generators.ipynb`](exercises/07-decorators-generators.ipynb) | [`generators/`](generators/README.md) |
| **H** | HTTP clients | [`exercises/19-httpx-http-clients.ipynb`](exercises/19-httpx-http-clients.ipynb) | Install **`httpx`** |
| **I** | Itertools / composition | [`exercises/11-collections-itertools-functools.ipynb`](exercises/11-collections-itertools-functools.ipynb) | Optional **`more-itertools`** on real projects |
| **J** | JSON | [`exercises/04-modules-json-pathlib.ipynb`](exercises/04-modules-json-pathlib.ipynb), [`text_processing/extract_json_fence.py`](text_processing/extract_json_fence.py) | [`exercises/13-regex-text-extraction.ipynb`](exercises/13-regex-text-extraction.ipynb) |
| **K** | `/` & `*` signatures | [`exercises/20-positional-keyword-only-signatures.ipynb`](exercises/20-positional-keyword-only-signatures.ipynb) | — |
| **L** | Logging | [`exercises/12-logging-for-pipelines.ipynb`](exercises/12-logging-for-pipelines.ipynb) | [`logging/`](logging/README.md) |
| **M** | Memory / profiling mindset | [`exercises/16-numpy-embeddings-shape.ipynb`](exercises/16-numpy-embeddings-shape.ipynb) (RAM-shaped thinking), [`profiling_intro/tracemalloc_demo.py`](profiling_intro/tracemalloc_demo.py) | [`generators/`](generators/README.md) streaming |
| **N** | NumPy | [`exercises/16-numpy-embeddings-shape.ipynb`](exercises/16-numpy-embeddings-shape.ipynb) | Install **`numpy`** |
| **O** | Object design | [`exercises/05-classes-oop.ipynb`](exercises/05-classes-oop.ipynb), [`oop/`](oop/README.md) | [`typing/embedder_protocol.py`](typing/embedder_protocol.py) composition |
| **P** | Protocols / typing | [`exercises/08-advanced-typing-protocols-dataclasses.ipynb`](exercises/08-advanced-typing-protocols-dataclasses.ipynb) | [`typing/`](typing/README.md) |
| **Q** | Queues | [`exercises/18-asyncio-queue-pipelines.ipynb`](exercises/18-asyncio-queue-pipelines.ipynb), [`async/async_queue_demo.py`](async/async_queue_demo.py) | [`threading_intro/queue_sync_demo.py`](threading_intro/queue_sync_demo.py) |
| **R** | Regex / text | [`exercises/13-regex-text-extraction.ipynb`](exercises/13-regex-text-extraction.ipynb) | [`text_processing/`](text_processing/README.md) |
| **S** | Subprocess | [`exercises/15-subprocess-and-archives.ipynb`](exercises/15-subprocess-and-archives.ipynb) | — |
| **T** | Advanced typing | [`exercises/08-advanced-typing-protocols-dataclasses.ipynb`](exercises/08-advanced-typing-protocols-dataclasses.ipynb) | — |
| **U** | Testing | [`exercises/10-testing-debugging.ipynb`](exercises/10-testing-debugging.ipynb), [`exercises/17-pytest-fixtures-parametrize.ipynb`](exercises/17-pytest-fixtures-parametrize.ipynb) | [`leetcode_practice/tests/`](leetcode_practice/README.md), **`pytest`** |
| **V** | Virtual envs / pins | [`exercises/21-venv-and-dependency-pins.ipynb`](exercises/21-venv-and-dependency-pins.ipynb) | — |
| **W** | Workers / jobs | [`workers_intro/README.md`](workers_intro/README.md), [`workers_intro/async_pipeline_demo.py`](workers_intro/async_pipeline_demo.py) | Letter **W** in CURRICULUM (queues + mental model → **`04-*`** stacks later) |
| **X** | HTML / markup | [`exercises/22-html-parser-text.ipynb`](exercises/22-html-parser-text.ipynb) | Optional **`lxml`** / **`selectolax`** off-repo |
| **Y** | Async iteration | [`async/async_generator_demo.py`](async/async_generator_demo.py), [`exercises/09-async-io.ipynb`](exercises/09-async-io.ipynb) | — |
| **Z** | Zip archives | [`exercises/15-subprocess-and-archives.ipynb`](exercises/15-subprocess-and-archives.ipynb) (`zipfile`) | — |

---

## Beyond A→Z (still “foundations adjacent”)

| Topic | Where |
|-------|--------|
| **SQLite** (stdlib persistence) | [`sqlite_intro/`](sqlite_intro/README.md) |
| **pandas** (tabular prelude to ML stacks) | [`pandas_intro/`](pandas_intro/README.md) (`pip install pandas`) |
| **Thread pools & sync queues** | [`threading_intro/`](threading_intro/README.md) |
| **Timezone-aware datetimes** | [`datetime_intro/`](datetime_intro/README.md) |
| **Classic coding patterns** | [`leetcode_practice/`](leetcode_practice/README.md) |

---

Return to **[`README.md`](README.md)** for the folder tour and **[`CURRICULUM-A-Z.md`](CURRICULUM-A-Z.md)** for prose drills per letter.
