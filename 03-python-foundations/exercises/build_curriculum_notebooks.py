#!/usr/bin/env python3
"""
Generate progressive Jupyter notebooks for the Python foundations track.
Run: python build_curriculum_notebooks.py

Format: industry-style learning module (objectives, TOC, demos, exercises, solutions).
Output: sibling .ipynb files in this directory.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

OUT_DIR = Path(__file__).resolve().parent

NB_BASE: dict[str, Any] = {
    "nbformat": 4,
    "nbformat_minor": 5,
    "metadata": {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "pygments_lexer": "ipython3", "version": "3.11.0"},
    },
}


def cell_md(text: str) -> dict[str, Any]:
    if not text.endswith("\n"):
        text += "\n"
    return {"cell_type": "markdown", "metadata": {}, "source": text.splitlines(True)}


def cell_code(text: str) -> dict[str, Any]:
    if not text.endswith("\n"):
        text += "\n"
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": text.splitlines(True),
    }


def banner(
    num: str,
    title: str,
    level: str,
    prereq: str,
    next_nb: str,
    objectives: list[str],
    toc: list[str],
) -> list[dict[str, Any]]:
    objs = "\n".join(f"- {o}" for o in objectives)
    tlines = "\n".join(f"{i + 1}. **{t}**" for i, t in enumerate(toc))
    body = f"""# Notebook {num} — {title}

| | |
|---|---|
| **Track** | AI Engineering · `03-python-foundations/exercises/` |
| **Level** | {level} |
| **Pattern** | *Concept* → *Runnable demo* → *Your turn* → *Solution* |

**Prerequisites:** {prereq}

**Next up:** {next_nb}

---

## Learning objectives

{objs}

## Table of contents

{tlines}

---

## How to use this notebook

1. Run cells **top to bottom** the first time through.
2. Re-run and **change values** to test your understanding.
3. Do **Your turn** cells before opening solutions (HTML `<details>` blocks or later cells).

---
"""
    return [cell_md(body)]


def section_header(title: str, blurb: str) -> dict[str, Any]:
    return cell_md(f"## {title}\n\n{blurb}\n")


def solution_md(title: str, code: str) -> dict[str, Any]:
    return cell_md(
        f"### Solution — {title}\n\n<details>\n<summary>Click to expand</summary>\n\n```python\n{code.strip()}\n```\n\n</details>\n"
    )


def write_nb(name: str, cells: list[dict[str, Any]]) -> None:
    path = OUT_DIR / name
    nb = dict(NB_BASE)
    nb["cells"] = cells
    path.write_text(json.dumps(nb, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("Wrote", path.name)


def nb01() -> None:
    cells: list[dict[str, Any]] = []
    cells.extend(
        banner(
            "01",
            "Syntax, values & prompt-shaped strings",
            "Beginner",
            "None — start here.",
            "`02-collections-comprehensions.ipynb`",
            [
                "Use variables and core operators confidently.",
                "Format strings with **f-strings** for LLM prompts.",
                "Normalize booleans and comparisons for flags.",
            ],
            ["Expressions & variables", "Strings & f-strings", "Booleans & guards"],
        )
    )
    cells.append(section_header("1 · Expressions & variables", "*Explanation:* Python binds **names** to **objects**. AI code passes integers for batch sizes, floats for temperatures, strings for prompts."))
    cells.append(
        cell_code(
            """batch_size = 8
temperature = 0.7
max_tokens = 2_048  # underscores for readability (Python 3.6+)

print(batch_size * 2, temperature < 1.0, max_tokens)"""
        )
    )

    cells.append(section_header("2 · Strings & f-strings", "*Explanation:* **f-strings** interpolate values — you will live inside them while logging and prompting."))
    cells.append(
        cell_code(
            '''task = "summarize"
doc_title = "On-call playbook"

prompt = f"""\
TASK: {task}
DOCUMENT: {doc_title}
RULES:
- Bullet points only
- Max {batch_size} bullets
"""
print(prompt)'''
        )
    )

    cells.append(section_header("3 · Booleans & guards", "*Explanation:* Combine comparisons with `and` / `or`. Prefer explicit checks instead of abusing truthiness."))
    cells.append(
        cell_code(
            '''enabled = True
score = 0.82

def should_route_to_human(enabled: bool, score: float) -> bool:
    return enabled and score < 0.5

print("route?", should_route_to_human(enabled, score))'''
        )
    )

    cells.append(cell_md("### Exercise — mini prompt builder\n\nImplement `build_classifier_prompt(labels)` returning one string:\n\n- Line 1 exactly: `CLASSIFIER: multi-label`\n- Line 2: `LABELS: ` + comma-separated **sorted** labels\n\nThen `assert \"LABELS: a, b, c\" in build_classifier_prompt([\"c\", \"a\", \"b\"])`.\n"))
    cells.append(cell_code("# Your code here\ndef build_classifier_prompt(labels: list[str]) -> str:\n    raise NotImplementedError\n\n\nassert \"LABELS: a, b, c\" in build_classifier_prompt([\"c\", \"a\", \"b\"])\nprint(\"OK\")"))

    cells.append(solution_md("mini prompt builder", "def build_classifier_prompt(labels: list[str]) -> str:\n    ordered = \", \".join(sorted(labels))\n    return f\"CLASSIFIER: multi-label\\nLABELS: {ordered}\"\n"))

    write_nb("01-syntax-values-and-io.ipynb", cells)


def nb02() -> None:
    cells: list[dict[str, Any]] = []
    cells.extend(
        banner(
            "02",
            "Collections & comprehensions",
            "Beginner → intermediate",
            "`01-syntax-values-and-io.ipynb`",
            "`03-control-flow-functions.ipynb`",
            [
                "Choose list / dict / tuple / set appropriately.",
                "Use dict merges and safe access.",
                "Write readable list comprehensions for text prep.",
            ],
            ["Lists & messages", "Dicts & hyperparameters", "Comprehensions for cleaning"],
        )
    )

    cells.append(section_header("1 · Lists for chat traces", "*Explanation:* Chat history is a **list** of dicts — order matters."))
    cells.append(
        cell_code(
            '''messages = [
    {"role": "system", "content": "Be concise."},
    {"role": "user", "content": "Hello"},
]
messages.append({"role": "assistant", "content": "Hi — how can I help?"})
print(messages[-1])'''
        )
    )

    cells.append(section_header("2 · Dicts for configs", "*Explanation:* Merge defaults with overrides via `|` (Python 3.9+)."))
    cells.append(cell_code("defaults = {\"temperature\": 0.7, \"top_k\": 5}\nuser_prefs = {\"temperature\": 0.2}\ncfg = defaults | user_prefs\nprint(cfg)"))

    cells.append(section_header("3 · Comprehensions", "*Explanation:* Compact loops for normalization — prefer readable over clever."))
    cells.append(cell_code('messy = [" Rag ", "", "chunk\\n", "docs "]\nclean = [s.strip().lower() for s in messy if s.strip()]\nprint(clean)'))

    cells.append(cell_md("### Exercise — dedupe doc IDs\n\nGiven `doc_ids: list[str]`, return a **sorted list** of **unique** IDs using `set`, without mutating the original list.\n"))
    cells.append(
        cell_code(
            """def unique_sorted_ids(doc_ids: list[str]) -> list[str]:
    raise NotImplementedError


assert unique_sorted_ids(["b", "a", "b"]) == ["a", "b"]
print("OK")"""
        )
    )
    cells.append(solution_md("dedupe doc IDs", "def unique_sorted_ids(doc_ids: list[str]) -> list[str]:\n    return sorted(set(doc_ids))"))

    write_nb("02-collections-comprehensions.ipynb", cells)


def nb03() -> None:
    cells: list[dict[str, Any]] = []
    cells.extend(
        banner(
            "03",
            "Control flow & functions",
            "Intermediate",
            "`02-collections-comprehensions.ipynb`",
            "`04-modules-json-pathlib.ipynb`",
            [
                "Branch and loop idiomatically.",
                "Design function signatures with defaults & `**kwargs`.",
                "Understand mutability pitfalls with default arguments.",
            ],
            ["Conditionals & loops", "Function arguments", "Avoid mutable defaults"],
        )
    )

    cells.append(section_header("1 · Enumerate chunks", "*Explanation:* `enumerate` pairs index + value — chunk numbering."))
    cells.append(cell_code('chunks = ["alpha", "beta"]\nfor idx, text in enumerate(chunks):\n    print(idx, len(text))'))

    cells.append(section_header("2 · `*args` & `**kwargs`", "*Explanation:* Forwarding unknown keyword parameters mirrors SDK wrappers."))
    cells.append(
        cell_code(
            '''def invoke_tool(name: str, **params):
    return {"tool": name, "params": params}

print(invoke_tool("search", query="rag", top_k=3))'''
        )
    )

    cells.append(section_header("3 · Mutable default trap", "*Explanation:* Never use `list()`/`dict()` as defaults — use `None` + factory."))
    cells.append(
        cell_code(
            '''def append_doc(wrong_bad=[], item=\"x\"):  # anti-pattern shown conceptually only
    \"\"\"Demo idea — don't copy this pattern into prod code.\"\"\"
    wrong_bad.append(item)
    return wrong_bad


def append_doc_good(acc: list | None = None, item: str = \"x\") -> list:
    acc = [] if acc is None else acc
    acc.append(item)
    return acc'''
        )
    )

    cells.append(cell_md("### Exercise — clip list\n\nImplement `clip_texts(texts, max_len)` returning a **new** list where every string longer than `max_len` is truncated to its first `max_len` characters. Empty strings removed.\n"))
    cells.append(
        cell_code(
            '''def clip_texts(texts: list[str], max_len: int) -> list[str]:
    raise NotImplementedError


assert clip_texts(["hi", "toolongword", ""], 3) == ["hi", "too"]
print("OK")'''
        )
    )
    cells.append(
        solution_md(
            "clip list",
            "def clip_texts(texts: list[str], max_len: int) -> list[str]:\n    out: list[str] = []\n    for t in texts:\n        if not t:\n            continue\n        out.append(t if len(t) <= max_len else t[:max_len])\n    return out",
        )
    )

    write_nb("03-control-flow-functions.ipynb", cells)


def nb04() -> None:
    cells: list[dict[str, Any]] = []
    cells.extend(
        banner(
            "04",
            "Modules, JSON & pathlib",
            "Intermediate",
            "`03-control-flow-functions.ipynb`",
            "`05-classes-oop.ipynb`",
            [
                "Import cleanly and guard `main` execution.",
                "Parse and emit JSON safely.",
                "Use `pathlib.Path` for portable IO — RAG ingestion starts here.",
            ],
            ["Imports & __main__", "JSON payloads", "Path & text files"],
        )
    )

    cells.append(section_header("1 · Import discipline", "*Explanation:* `if __name__ == \"__main__\":` keeps modules importable from tests."))
    cells.append(cell_code("import json\nfrom pathlib import Path\n\nprint(Path.cwd())"))

    cells.append(section_header("2 · JSON for tool calls", "*Explanation:* Models return JSON-shaped tool calls — practice `loads`/`dumps`."))
    cells.append(cell_code('payload = {"tool": "search", "args": {"q": "vector db"}}\nraw = json.dumps(payload, ensure_ascii=False)\nprint(raw, "->", json.loads(raw)["tool"])'))

    cells.append(section_header("3 · Path read/write", "*Explanation:* Always pass `encoding=\"utf-8\"` explicitly for text."))
    cells.append(
        cell_code(
            '''p = Path("_nb_tmp_demo.txt")
p.write_text("hello\\nworld", encoding="utf-8")
print(p.read_text(encoding="utf-8").splitlines())
p.unlink(missing_ok=True)'''
        )
    )

    cells.append(cell_md("### Exercise — JSONL count\n\nImplement `count_objects(path: Path) -> int`: number of lines that are non-empty **and** valid JSON **objects** (`dict`).\n"))
    cells.append(
        cell_code(
            '''import json
from pathlib import Path


def count_objects(path: Path) -> int:
    raise NotImplementedError


tmp = Path("_nb_jsonl_demo.jsonl")
tmp.write_text('{"k":1}\n\n[1,2]\n{"ok":true}\n', encoding="utf-8")
assert count_objects(tmp) == 2
tmp.unlink(missing_ok=True)
print("OK")'''
        )
    )
    cells.append(
        solution_md(
            "JSONL count",
            "def count_objects(path: Path) -> int:\n    n = 0\n    for line in path.read_text(encoding=\"utf-8\").splitlines():\n        if not line.strip():\n            continue\n        try:\n            val = json.loads(line)\n        except json.JSONDecodeError:\n            continue\n        if isinstance(val, dict):\n            n += 1\n    return n",
        )
    )

    write_nb("04-modules-json-pathlib.ipynb", cells)


def nb05() -> None:
    cells: list[dict[str, Any]] = []
    cells.extend(
        banner(
            "05",
            "Classes & OOP patterns",
            "Intermediate",
            "`04-modules-json-pathlib.ipynb`",
            "`06-exceptions-context-managers.ipynb`",
            [
                "Model services as classes with explicit state.",
                "Know when `@staticmethod` / `@classmethod` helps.",
                "Prefer composition for small components (retriever, reranker).",
            ],
            ["Minimal service class", "Composition", "`TextSplitter` exercise"],
        )
    )

    cells.append(section_header("1 · Service class", "*Explanation:* Bundle config + methods — e.g., embedder client, chunker."))
    cells.append(
        cell_code(
            '''class FakeEmbedder:
    def __init__(self, dim: int = 3) -> None:
        self.dim = dim

    def embed(self, texts: list[str]) -> list[list[float]]:
        return [[float(len(t) % self.dim)] * self.dim for t in texts]

print(FakeEmbedder(2).embed(["ab", "abc"]))'''
        )
    )

    cells.append(section_header("2 · Composition", "*Explanation:* Small classes working together beat deep inheritance trees."))
    cells.append(
        cell_code(
            '''class Retriever:
    def __init__(self, docs: list[str]) -> None:
        self.docs = docs

    def search(self, q: str, k: int = 2) -> list[str]:
        return [d for d in self.docs if q.lower() in d.lower()][:k]

class Pipeline:
    def __init__(self, retriever: Retriever) -> None:
        self.r = retriever

    def answer(self, q: str) -> str:
        return " | ".join(self.r.search(q))

print(Pipeline(Retriever(["RAG basics", "Vector DB"])).answer("rag"))'''
        )
    )

    cells.append(cell_md("### Exercise — `TextSplitter`\n\nClass `TextSplitter(max_chars)` with method `split(text: str) -> list[str]` splitting contiguous slices ≤ `max_chars`.\n"))
    cells.append(
        cell_code(
            '''class TextSplitter:
    def __init__(self, max_chars: int) -> None:
        self.max_chars = max_chars

    def split(self, text: str) -> list[str]:
        raise NotImplementedError


assert TextSplitter(4).split("abcdefghi") == ["abcd", "efgh", "i"]
print("OK")'''
        )
    )
    cells.append(
        solution_md(
            "TextSplitter",
            "class TextSplitter:\n    def __init__(self, max_chars: int) -> None:\n        self.max_chars = max_chars\n\n    def split(self, text: str) -> list[str]:\n        step = self.max_chars\n        return [text[i : i + step] for i in range(0, len(text), step)]",
        )
    )

    write_nb("05-classes-oop.ipynb", cells)


def nb06() -> None:
    cells: list[dict[str, Any]] = []
    cells.extend(
        banner(
            "06",
            "Exceptions & context managers",
            "Intermediate → advanced",
            "`05-classes-oop.ipynb`",
            "`07-decorators-generators.ipynb`",
            [
                "Raise and catch exceptions narrowly.",
                "Preserve tracebacks with `raise ... from`.",
                "Author reusable setup/teardown with context managers.",
            ],
            ["Try / except patterns", "Chaining exceptions", "`contextmanager` timer"],
        )
    )

    cells.append(section_header("1 · Narrow catches", "*Explanation:* Catch `json.JSONDecodeError`, not blanket `Exception`, unless at process boundary."))
    cells.append(
        cell_code(
            '''import json

def loads_obj(raw: str) -> dict:
    try:
        val = json.loads(raw)
    except json.JSONDecodeError as e:
        raise ValueError("bad json") from e
    if not isinstance(val, dict):
        raise TypeError("expected object")
    return val'''
        )
    )

    cells.append(section_header("2 · Context manager timer", "*Explanation:* Mirrors dependency scopes in FastAPI — acquire, yield, release."))
    cells.append(
        cell_code(
            '''import time
from contextlib import contextmanager

@contextmanager
def span(name: str):
    t0 = time.perf_counter()
    yield
    print(f"[{name}] {1000*(time.perf_counter()-t0):.1f} ms")

with span("retrieval"):
    time.sleep(0.02)'''
        )
    )

    cells.append(cell_md("### Exercise — `nullsafe_get`\n\nFunction `nullsafe_get(d, key)` returns `d[key]` if `key` exists **and** value is not `None`; otherwise returns `\"\"`. Raises **nothing**.\n"))
    cells.append(
        cell_code(
            '''def nullsafe_get(d: dict, key: str) -> str:
    raise NotImplementedError


assert nullsafe_get({"a": None}, "a") == ""
assert nullsafe_get({"a": "x"}, "a") == "x"
assert nullsafe_get({}, "missing") == ""
print("OK")'''
        )
    )
    cells.append(solution_md("nullsafe_get", "def nullsafe_get(d: dict, key: str) -> str:\n    if key not in d:\n        return \"\"\n    val = d[key]\n    return \"\" if val is None else val"))

    write_nb("06-exceptions-context-managers.ipynb", cells)


def nb07() -> None:
    cells: list[dict[str, Any]] = []
    cells.extend(
        banner(
            "07",
            "Decorators & generators",
            "Advanced",
            "`06-exceptions-context-managers.ipynb`",
            "`08-advanced-typing-protocols-dataclasses.ipynb`",
            [
                "Implement decorators with `functools.wraps`.",
                "Write memory-efficient iterators with `yield`.",
                "Compose timing/logging cross-cutting concerns.",
            ],
            ["Decorator anatomy", "Parameterized decorators", "Generators for chunks"],
        )
    )

    cells.append(section_header("1 · Timing decorator", "*Explanation:* Wrap functions without rewriting bodies."))
    cells.append(
        cell_code(
            '''import functools
import time

def timed(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        out = fn(*args, **kwargs)
        print(f"{fn.__name__}: {(time.perf_counter()-t0)*1000:.1f} ms")
        return out
    return wrapper

@timed
def slow(n: int = 100_000) -> int:
    return sum(range(n))

slow()'''
        )
    )

    cells.append(section_header("2 · Chunk generator", "*Explanation:* Yield windows — backbone of streaming ingestion."))
    cells.append(
        cell_code(
            '''from collections.abc import Iterator

def char_windows(text: str, n: int, step: int) -> Iterator[str]:
    i = 0
    while i + n <= len(text):
        yield text[i : i + n]
        i += step

print(list(char_windows("abcdefghij", 4, 3)))'''
        )
    )

    cells.append(cell_md("### Exercise — repeat decorator\n\n`@repeat_times(n)` runs underlying function `n` times, returns **list** of results (assume no exceptions).\n"))
    cells.append(
        cell_code(
            '''import functools


def repeat_times(n: int):
    def deco(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            raise NotImplementedError

        return wrapper

    return deco


counter = {"v": 0}

@repeat_times(3)
def bump():
    counter["v"] += 1
    return counter["v"]

assert bump() == [1, 2, 3]
print("OK")'''
        )
    )
    cells.append(
        solution_md(
            "repeat decorator",
            "import functools\n\ndef repeat_times(n: int):\n    def deco(fn):\n        @functools.wraps(fn)\n        def wrapper(*args, **kwargs):\n            return [fn(*args, **kwargs) for _ in range(n)]\n        return wrapper\n    return deco",
        )
    )

    write_nb("07-decorators-generators.ipynb", cells)


def nb08() -> None:
    cells: list[dict[str, Any]] = []
    cells.extend(
        banner(
            "08",
            "Typing, Protocols & dataclasses",
            "Advanced",
            "`07-decorators-generators.ipynb`",
            "`09-async-io.ipynb`",
            [
                "Annotate functions for readability and tooling.",
                "Model configuration with `@dataclass(frozen=True)`.",
                "Define `Protocol` interfaces for swap-in components.",
            ],
            ["Annotations & generics lite", "Dataclass configs", "`Protocol` interfaces"],
        )
    )

    cells.append(section_header("1 · Dataclass config", "*Explanation:* Immutable config objects prevent accidental mutation in long chains."))
    cells.append(
        cell_code(
            '''from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class ModelConfig:
    name: str
    temperature: float = 0.2

cfg = ModelConfig(name="mini")
print(cfg)'''
        )
    )

    cells.append(section_header("2 · Protocol", "*Explanation:* Structural subtyping — mock-friendly abstractions."))
    cells.append(
        cell_code(
            '''from typing import Protocol, runtime_checkable

@runtime_checkable
class VectorStore(Protocol):
    def query(self, q: str, k: int) -> list[str]: ...

class MemoryVS:
    def __init__(self, docs: list[str]) -> None:
        self.docs = docs
    def query(self, q: str, k: int) -> list[str]:
        return [d for d in self.docs if q in d][:k]

vs: VectorStore = MemoryVS(["vector search", "sql db"])
print(isinstance(vs, VectorStore), vs.query("vector", 1))'''
        )
    )

    cells.append(cell_md("### Exercise — typed `clamp`\n\n`clamp(x: float, lo: float, hi: float) -> float`. If `lo > hi`, raise `ValueError`.\n"))
    cells.append(
        cell_code(
            '''def clamp(x: float, lo: float, hi: float) -> float:
    raise NotImplementedError


assert clamp(1.5, 0.0, 1.0) == 1.0
assert clamp(-1.0, 0.0, 1.0) == 0.0
print("OK")'''
        )
    )
    cells.append(
        solution_md(
            "clamp",
            "def clamp(x: float, lo: float, hi: float) -> float:\n    if lo > hi:\n        raise ValueError(\"lo > hi\")\n    return max(lo, min(hi, x))",
        )
    )

    write_nb("08-advanced-typing-protocols-dataclasses.ipynb", cells)


def nb09() -> None:
    cells: list[dict[str, Any]] = []
    cells.extend(
        banner(
            "09",
            "Async IO for AI services",
            "Advanced",
            "`08-advanced-typing-protocols-dataclasses.ipynb`",
            "`10-testing-debugging.ipynb`",
            [
                "Overlap I/O-bound waits with `asyncio`.",
                "Use `gather` for parallel fetches.",
                "Know blocking vs async boundaries before FastAPI.",
            ],
            ["Coroutines recap", "`gather` parallelism", "`asyncio.to_thread` offload"],
        )
    )

    cells.append(section_header("1 · Concurrent sleeps", "*Explanation:* Replace sleeps with HTTP clients later — structure identical."))
    cells.append(
        cell_code(
            '''import asyncio

async def fetch(name: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"{name}-done"

async def main():
    out = await asyncio.gather(
        fetch("a", 0.15),
        fetch("b", 0.15),
        fetch("c", 0.15),
    )
    print(out)

await main()'''
        )
    )

    cells.append(cell_md("> If `await main()` fails in your runtime, run `asyncio.run(main())` instead.\n"))

    cells.append(section_header("2 · Semaphore limiting", "*Explanation:* Bound concurrency — critical when calling rate-limited APIs."))
    cells.append(
        cell_code(
            '''import asyncio

async def bounded_gather(items: list[int], limit: int):
    sem = asyncio.Semaphore(limit)

    async def work(i: int) -> int:
        async with sem:
            await asyncio.sleep(0.05)
            return i * i

    return await asyncio.gather(*(work(i) for i in items))

print(await bounded_gather(list(range(6)), limit=2))'''
        )
    )

    cells.append(
        section_header(
            "3 · `asyncio.to_thread` offload",
            "*Explanation:* Use a thread pool for **blocking** CPU or C-extension work so the event loop can still schedule other coroutines — common when bridging `requests`, file parsing, or numpy inside async services.",
        )
    )
    cells.append(
        cell_code(
            '''import asyncio

def blocking_sum(n: int) -> int:
    return sum(range(n))

async def run_offload():
    return await asyncio.to_thread(blocking_sum, 200_000)

print(await run_offload())'''
        )
    )

    cells.append(cell_md("### Exercise — first successful\n\n`async def first_done(coro_a, coro_b)` schedules both coroutines and returns the **result** of whichever finishes first. Use `asyncio.create_task`, `asyncio.wait(..., return_when=asyncio.FIRST_COMPLETED)`, cancel the slower one, then `await` the winner.\n"))
    cells.append(
        cell_code(
            '''import asyncio

async def slow_return(val: int, delay: float) -> int:
    await asyncio.sleep(delay)
    return val

async def first_done(a, b):
    raise NotImplementedError


print(await first_done(slow_return(1, 0.05), slow_return(2, 0.2)))'''
        )
    )
    cells.append(
        solution_md(
            "first_done",
            "async def first_done(a, b):\n    t1 = asyncio.create_task(a)\n    t2 = asyncio.create_task(b)\n    done, pending = await asyncio.wait({t1, t2}, return_when=asyncio.FIRST_COMPLETED)\n    winner = done.pop()\n    for p in pending:\n        p.cancel()\n    return await winner",
        )
    )

    write_nb("09-async-io.ipynb", cells)


def nb10() -> None:
    cells: list[dict[str, Any]] = []
    cells.extend(
        banner(
            "10",
            "Testing & debugging mindset",
            "Advanced",
            "`09-async-io.ipynb`",
            "`python-foundations-beginner-to-advanced.ipynb` (full spiral)",
            [
                "Write assertions for pure helpers.",
                "Isolate filesystem tests with tmp paths.",
                "Think about pytest adoption next.",
            ],
            ["Assertions & param tables", "Tmp paths", "Debugging hooks"],
        )
    )

    cells.append(section_header("1 · Assertions", "*Explanation:* Notebook-friendly checks — migrate to `pytest` later."))
    cells.append(
        cell_code(
            '''def add(a: int, b: int) -> int:
    return a + b

assert add(2, 3) == 5
print("assertions pass")'''
        )
    )

    cells.append(section_header("2 · Table-driven checks", "*Explanation:* Loop over cases — preview of parametrization."))
    cells.append(
        cell_code(
            '''cases = [
    ("{}", {}),
    ('{"a":1}', {"a": 1}),
]
import json
for raw, expected in cases:
    assert json.loads(raw) == expected
print("table OK")'''
        )
    )

    cells.append(cell_md("### Exercise — test `truncate`\n\nDefine `truncate(s, n)` returning `s` if `len(s) <= n` else `s[:n] + \"…\"`. Add **three** `assert` lines: one for a string shorter than `n`, one equal to `n`, and one longer than `n`.\n"))
    cells.append(
        cell_code(
            '''def truncate(s: str, n: int) -> str:
    raise NotImplementedError


# Your asserts here'''
        )
    )
    cells.append(
        solution_md(
            "truncate",
            'def truncate(s: str, n: int) -> str:\n    if len(s) <= n:\n        return s\n    return s[:n] + "…"\n\nassert truncate("hi", 5) == "hi"\nassert truncate("abcd", 4) == "abcd"\nassert truncate("abcdefghij", 4) == "abcd…"',
        )
    )

    write_nb("10-testing-debugging.ipynb", cells)


def main() -> None:
    nb01()
    nb02()
    nb03()
    nb04()
    nb05()
    nb06()
    nb07()
    nb08()
    nb09()
    nb10()
    print("Done. Generated 10 notebooks in", OUT_DIR)


if __name__ == "__main__":
    main()
