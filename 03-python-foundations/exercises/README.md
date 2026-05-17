# Python foundations — step-by-step notebooks (`exercises/`)

Progressive Jupyter notebooks from **beginner → advanced**, tuned for **AI engineering** (prompts, JSON, retrieval-shaped exercises).

**Inside each notebook:** after the main lesson cells you get **Progressive drills — easy → harder** — extra runnable examples that ramp difficulty *within* that topic (simple literals → richer patterns). Work through them before the capstone exercise when you want maximum coverage.

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

**Extended track (11 → 15)** maps to practical stdlib topics from [`../CURRICULUM-A-Z.md`](../CURRICULUM-A-Z.md): collections/itertools (**I**), logging (**L**), regex (**R**), bytes (**B**), subprocess/archives (**S**, **Z**).

Then open the **single-volume spiral**: [`../python-foundations-beginner-to-advanced.ipynb`](../python-foundations-beginner-to-advanced.ipynb) and cross-check with [`../CURRICULUM-A-Z.md`](../CURRICULUM-A-Z.md).

**OOP-only spiral** (daily-life analogies): [`../oop/README.md`](../oop/README.md).

---

## Notebook format (aligned with common MOOC / bootcamp modules)

Each notebook follows the same **instructional pattern**:

1. **Module metadata table** — track, difficulty, workflow type (concept → demo → exercise → solution).
2. **Learning objectives** — short, observable outcomes.
3. **Table of contents** — mapped to numbered sections inside the notebook.
4. **Concept sections** — short explanation grounded in AI workflows (prompts, tools, ingestion).
5. **Runnable demos** — minimal code that works end-to-end.
6. **Progressive drills** — graded **A → B → C** examples (easy → harder) on the same topic.
7. **Formative exercises** — small tasks with `assert`-based checks where helpful.
8. **Solutions** — collapsed HTML `<details>` blocks so you can avoid spoilers until ready.

This mirrors patterns used across platforms like **Coursera**, **edX**, and **DeepLearning.AI short courses**: predictable structure, bite-sized assessments, explicit prerequisites.

---

## Regenerating notebooks

If you edit [`build_curriculum_notebooks.py`](build_curriculum_notebooks.py), regenerate all `.ipynb` files:

```bash
cd exercises
python build_curriculum_notebooks.py
```

Requires Python **3.10+** for notebook cell snippets using modern typing syntax (`|` unions, `list[str]`).

---

## Related folders

Topic buckets (`../oop/`, `../async/`, …) are for **your own scripts** as you outgrow notebooks; keep notebooks here as the guided path.
