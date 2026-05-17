#!/usr/bin/env python3
"""
Generate progressive Jupyter notebooks for the Python foundations track.
Run: python build_curriculum_notebooks.py

Format: industry-style learning module (objectives, TOC, demos, progressive drills, exercises, solutions).
Writes notebooks **01–15** (core 01–10 + stdlib extensions 11–15) as sibling `.ipynb` files in this directory.
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


def drill_header(blurb: str) -> dict[str, Any]:
    """Section divider before graded micro-examples."""
    return cell_md(f"---\n\n## Progressive drills — **easy → harder**\n\n{blurb}\n")


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
            [
                "Expressions & variables",
                "Strings & f-strings",
                "Booleans & guards",
                "Progressive drills — literals → format specs → conditional SYSTEM blocks",
                "Exercise — mini prompt builder",
            ],
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

    cells.append(
        drill_header(
            "These drills mirror **prompt assembly**: glue strings, control numeric display, toggle instructions without spaghetti."
        )
    )
    cells.append(
        cell_md(
            """### A · Easiest — stitch role strings

Concatenate simple pieces — same idea as joining `system` + delimiter + `user`."""
        )
    )
    cells.append(
        cell_code(
            '''system = "You cite sources."
user_turn = "Summarize this incident."
delimiter = "\\n---\\n"
print(system + delimiter + user_turn)'''
        )
    )

    cells.append(
        cell_md(
            """### B · Medium — control numeric display (`:.2f`, widths)

API docs often pin temperatures/top-k — formatting avoids `"0.256789"` noise in logs."""
        )
    )
    cells.append(
        cell_code(
            '''temperature = 0.256789
top_k = 5
print(f"sampling temp={temperature:.2f}, top_k={top_k:>3}")'''
        )
    )

    cells.append(
        cell_md(
            """### C · Harder — conditional SYSTEM blocks

Turn flags into bullet lists — mirrors production prompts where **debug/reasoning** sections toggle per environment."""
        )
    )
    cells.append(
        cell_code(
            '''debug_trace = True
rules = ["Answer concisely.", "Refuse harmful requests."]
if debug_trace:
    rules.append("Show intermediate checklist internally before answering.")

system_prompt = "SYSTEM RULES:\\n- " + "\\n- ".join(rules)
print(system_prompt)'''
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
            [
                "Lists & messages",
                "Dicts & hyperparameters",
                "Comprehensions for cleaning",
                "Progressive drills — tuples → nested tool JSON → filtered IDs",
                "Exercise — dedupe doc IDs",
            ],
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

    cells.append(
        drill_header(
            "Collections power **retrieval pipelines**: pairing roles, drilling into nested tool payloads, filtering IDs cheaply."
        )
    )
    cells.append(cell_md("### A · Easiest — unpack `(role, text)` tuples\n\nSDKs sometimes hand you pairs—unpack instead of indexing `[0]`/`[1]`.\n"))
    cells.append(cell_code('pair = ("system", "Be factual.")\nrole, directive = pair\nprint(role, directive[:2])'))

    cells.append(
        cell_md(
            "### B · Medium — safe drill into nested tool JSON\n\n`.get` avoids `KeyError` when model JSON is noisy.\n"
        )
    )
    cells.append(
        cell_code(
            '''payload = {"tool": {"name": "search", "args": {"q": "hybrid retrieval"}}}
query = payload.get("tool", {}).get("args", {}).get("q", "")
print("query:", query)'''
        )
    )

    cells.append(
        cell_md(
            "### C · Harder — comprehension filters chunk IDs\n\nKeep only IDs matching a prefix—cheap gate before hitting the vector DB.\n"
        )
    )
    cells.append(
        cell_code(
            '''ids = ["chunk_finance_01", "sidebar_ad", "chunk_finance_02"]
finance_chunks = [cid for cid in ids if cid.startswith("chunk_finance_")]
print(finance_chunks)'''
        )
    )

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
            [
                "Conditionals & loops",
                "Function arguments",
                "Avoid mutable defaults",
                "Progressive drills — routing → zip pairing → variadic prompts",
                "Exercise — clip list",
            ],
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

    cells.append(
        drill_header(
            "Control flow + functions orchestrate **routing logic**, **parallel structures**, and **prompt sandwiches**."
        )
    )
    cells.append(cell_md("### A · Easiest — confidence routing (`if / elif`)\n\nSend low-confidence generations to humans.\n"))
    cells.append(
        cell_code(
            '''def route_customer_ticket(confidence: float, urgent: bool) -> str:
    if urgent:
        return "page-oncall"
    if confidence >= 0.85:
        return "auto-resolve"
    elif confidence >= 0.55:
        return "human-review"
    return "escalate-security"


print(route_customer_ticket(0.9, False))
print(route_customer_ticket(0.4, True))'''
        )
    )

    cells.append(cell_md("### B · Medium — `zip` chunks + scores together\n\nParallel lists appear constantly when pairing retrieval hits with logits.\n"))
    cells.append(
        cell_code(
            '''chunks = ["chunk-a", "chunk-b"]
scores = [0.91, 0.42]
for text, score in zip(chunks, scores):
    print(text, "score=", round(score, 3))'''
        )
    )

    cells.append(cell_md("### C · Harder — variadic turns (`*parts`)\n\nBuild prompts without manually stitching uncertain arity lists.\n"))
    cells.append(
        cell_code(
            '''def sandwich(system: str, *user_turns: str, sep: str = "\\n---\\n") -> str:
    body = sep.join(user_turns)
    return sep.join([system, body])


print(sandwich("SYSTEM: cite sources.", "USER: summarize invoice", "USER: focus on totals"))'''
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
            [
                "Imports & __main__",
                "JSON payloads",
                "Path & text files",
                "Progressive drills — JSON types → extensions → pretty dumps",
                "Exercise — JSONL count",
            ],
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

    cells.append(
        drill_header(
            "Files + JSON underpin **every ingestion pipeline**. Ramp from typed parsing → filesystem hygiene → readable logs."
        )
    )
    cells.append(cell_md("### A · Easiest — detect JSON container types\n\nTool outputs might be arrays **or** objects—branch safely.\n"))
    cells.append(
        cell_code(
            '''import json

samples = ["[]", '{"hits":["a"]}', '"plain"']
for raw in samples:
    obj = json.loads(raw)
    kind = "array" if isinstance(obj, list) else "object" if isinstance(obj, dict) else "scalar"
    print(raw, "->", kind)'''
        )
    )

    cells.append(cell_md("### B · Medium — filter ingestion candidates by suffix\n\nSkip `.png`, ingest `.jsonl` only.\n"))
    cells.append(
        cell_code(
            '''from pathlib import Path

paths = [Path("notes.txt"), Path("dataset.jsonl"), Path("manifest.JSON")]
targets = [p for p in paths if p.suffix.lower() == ".jsonl"]
print([p.name for p in targets])'''
        )
    )

    cells.append(cell_md("### C · Harder — stable JSON logs (`sort_keys`, `indent`)\n\nDiff-friendly dumps help observability.\n"))
    cells.append(
        cell_code(
            '''import json

payload = {"model": "mini", "params": {"temperature": 0.2, "top_k": 8}}
print(json.dumps(payload, sort_keys=True, indent=2))'''
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
            [
                "Minimal service class",
                "Composition",
                "Progressive drills — counters → static helpers → reranked pipeline",
                "Exercise — `TextSplitter`",
            ],
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

    cells.append(
        drill_header(
            "Classes bundle **telemetry**, **pure helpers**, and **pluggable stages** exactly like modular AI microservices."
        )
    )
    cells.append(cell_md("### A · Easiest — rolling keyword counts (`Bag`-lite)\n\nTrack token frequencies before throwing tensors at anything.\n"))
    cells.append(
        cell_code(
            '''class KeywordCounter:
    def __init__(self) -> None:
        self.freq: dict[str, int] = {}

    def observe(self, token: str) -> None:
        self.freq[token] = self.freq.get(token, 0) + 1


counter = KeywordCounter()
for tok in ["embedding", "chunk", "embedding"]:
    counter.observe(tok)
print(counter.freq)'''
        )
    )

    cells.append(cell_md("### B · Medium — `@staticmethod` pure normalizers\n\nKeep unicode cleanup deterministic without constructing helper objects.\n"))
    cells.append(
        cell_code(
            '''class TextCleanup:
    @staticmethod
    def slug(label: str) -> str:
        return "-".join(label.lower().split())


print(TextCleanup.slug("Hybrid Vector Store"))'''
        )
    )

    cells.append(cell_md("### C · Harder — inject a reranker strategy\n\nComposition grows when retrieval feeds ranking modules.\n"))
    cells.append(
        cell_code(
            '''class ReverseRanker:
    def reorder(self, hits: list[str]) -> list[str]:
        return list(reversed(hits))


class ServedPipeline:
    def __init__(self, retriever: Retriever, ranker: ReverseRanker | None = None) -> None:
        self.retriever = retriever
        self.ranker = ranker or ReverseRanker()

    def answer(self, q: str) -> str:
        hits = self.retriever.search(q, k=5)
        hits = self.ranker.reorder(hits)
        return " | ".join(hits)


docs = Retriever(["alpha rag doc", "beta sql doc", "gamma rag advanced"])
print(ServedPipeline(docs).answer("rag"))'''
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
            [
                "Try / except patterns",
                "Chaining exceptions",
                "`contextmanager` timer",
                "Progressive drills — coercion → chained causes → class CM",
                "Exercise — `nullsafe_get`",
            ],
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

    cells.append(
        drill_header(
            "Failures are control flow in AI stacks—practice **narrow catches**, **cause chains**, and **scoped teardown**."
        )
    )
    cells.append(cell_md("### A · Easiest — coerce tool ints safely\n\nLLMs emit `\"24\"` strings—convert defensively.\n"))
    cells.append(
        cell_code(
            '''def coerce_positive_int(raw: str) -> int:
    try:
        value = int(raw)
    except ValueError as exc:
        raise ValueError(f"not an int: {raw!r}") from exc
    if value <= 0:
        raise ValueError("must be positive")
    return value


print(coerce_positive_int("128"))
try:
    coerce_positive_int("twelve")
except ValueError as err:
    print("blocked:", err)'''
        )
    )

    cells.append(cell_md("### B · Medium — translate KeyErrors into domain errors\n\nNested dict navigation mirrors messy JSON tool payloads.\n"))
    cells.append(
        cell_code(
            '''def extract_tool_name(payload: dict) -> str:
    try:
        return payload["tool"]["name"]
    except KeyError as exc:
        raise ValueError("payload missing tool.name path") from exc


sample = {"tool": {"name": "calculator", "args": {}}}
print(extract_tool_name(sample))
try:
    extract_tool_name({"tool": {}})
except ValueError as err:
    print("blocked:", err.__cause__)'''
        )
    )

    cells.append(cell_md("### C · Harder — class-based context manager\n\nBeyond `@contextmanager`, explicit `__enter__`/`__exit__` maps to SDK sessions.\n"))
    cells.append(
        cell_code(
            '''class TraceSpan:
    def __init__(self, label: str) -> None:
        self.label = label

    def __enter__(self) -> "TraceSpan":
        print("OPEN", self.label)
        return self

    def __exit__(self, exc_type, exc, tb) -> bool:
        print("CLOSE", self.label)
        return False  # propagate exceptions


with TraceSpan("embed-batch"):
    print("doing work...")'''
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
            [
                "Decorator anatomy",
                "Parameterized decorators",
                "Generators for chunks",
                "Progressive drills — partial factories → yield delegation → logging decorators",
                "Exercise — repeat decorator",
            ],
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

    cells.append(
        drill_header(
            "Decorators + generators instrument **latency**, reuse **embedding math**, and stitch **streaming iterators**."
        )
    )
    cells.append(cell_md("### A · Easiest — `functools.partial` for biased transforms\n\nFreeze hyper-parameters once—reuse everywhere.\n"))
    cells.append(
        cell_code(
            '''from functools import partial


def scale_vector(values: list[float], factor: float) -> list[float]:
    return [v * factor for v in values]


double = partial(scale_vector, factor=2.0)
print(double([0.1, 0.25]))'''
        )
    )

    cells.append(cell_md("### B · Medium — `yield from` stitches iterators\n\nConcatenate chapter iterators without building mega-lists.\n"))
    cells.append(
        cell_code(
            '''def intro_chunks():
    yield from ["preface", "setup"]

def body_chunks():
    yield from ["experiment", "results"]

def all_chunks():
    yield from intro_chunks()
    yield from body_chunks()


print(list(all_chunks()))'''
        )
    )

    cells.append(cell_md("### C · Harder — parameterized decorator emits telemetry prefix\n\nSame pattern LangChain middleware uses under the hood.\n"))
    cells.append(
        cell_code(
            '''import functools


def log_calls(prefix: str):
    def deco(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            print(f"{prefix} >> {fn.__name__}")
            return fn(*args, **kwargs)

        return wrapper

    return deco


@log_calls("LLM")
def completion(tokens: int) -> str:
    return f"{tokens}-tok-response"


print(completion(512))'''
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
            [
                "Annotations & generics lite",
                "Dataclass configs",
                "`Protocol` interfaces",
                "Progressive drills — TypedDict payloads → Literal states → Callable aliases",
                "Exercise — typed `clamp`",
            ],
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

    cells.append(
        drill_header(
            "Typing turns fuzzy JSON blobs into **contracts** engineers can grep—critical once agents multiply."
        )
    )
    cells.append(cell_md("### A · Easiest — `TypedDict` for tool payloads\n\nDocument keys editors understand.\n"))
    cells.append(
        cell_code(
            '''from typing import TypedDict

class ToolPayload(TypedDict):
    tool: str
    query: str


def summarize_tool_call(payload: ToolPayload) -> str:
    return f'{payload["tool"]} :: {payload["query"]}'


sample: ToolPayload = {"tool": "search", "query": "policy updates"}
print(summarize_tool_call(sample))'''
        )
    )

    cells.append(cell_md("### B · Medium — `Literal` for job states\n\nAnnotates allowed strings—IDE + pyright catch typos early.\n"))
    cells.append(
        cell_code(
            '''from typing import Literal

Status = Literal["queued", "running", "done"]


def badge(state: Status) -> str:
    icons = {"queued": "[Q]", "running": "[>>]", "done": "[OK]"}
    return icons[state]


print(badge("running"))'''
        )
    )

    cells.append(cell_md("### C · Harder — `Callable` type aliases\n\nSwap embedding backends without rewriting orchestration.\n"))
    cells.append(
        cell_code(
            '''from collections.abc import Callable

EmbedBatch = Callable[[list[str]], list[list[float]]]


def batch_embed_stub(texts: list[str]) -> list[list[float]]:
    return [[float(len(t)), 1.0] for t in texts]


def run_job(embedder: EmbedBatch, corpus: list[str]) -> int:
    return len(embedder(corpus))


print(run_job(batch_embed_stub, ["rag", "agents"]))'''
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
            [
                "Coroutines recap",
                "`gather` parallelism",
                "`asyncio.to_thread` offload",
                "Progressive drills — seq vs parallel → timeouts → tolerant gather",
                "Exercise — first successful coroutine",
            ],
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

    cells.append(
        drill_header(
            "Async separates **latency-bound** waits—practice measuring overlap, enforcing deadlines, and isolating flaky vendors."
        )
    )
    cells.append(cell_md("### A · Easiest — sequential vs overlapping sleeps\n\nWall-clock drops when I/O overlaps—this is why FastAPI loves `async`.\n"))
    cells.append(
        cell_code(
            '''import asyncio
import time


async def sequential_sleeps() -> float:
    t0 = time.perf_counter()
    await asyncio.sleep(0.06)
    await asyncio.sleep(0.06)
    return time.perf_counter() - t0


async def parallel_sleeps() -> float:
    t0 = time.perf_counter()
    await asyncio.gather(asyncio.sleep(0.06), asyncio.sleep(0.06))
    return time.perf_counter() - t0


async def bench_sleep() -> None:
    print("sequential ~", round(await sequential_sleeps(), 3), "s")
    print("parallel   ~", round(await parallel_sleeps(), 3), "s")


await bench_sleep()'''
        )
    )

    cells.append(cell_md("### B · Medium — hard deadlines with `wait_for`\n\nStop runaway vendor calls politely.\n"))
    cells.append(
        cell_code(
            '''import asyncio


async def slow_vendor() -> str:
    await asyncio.sleep(1.0)
    return "never"


try:
    await asyncio.wait_for(slow_vendor(), timeout=0.07)
except asyncio.TimeoutError:
    print("cancelled slow vendor")'''
        )
    )

    cells.append(cell_md("### C · Harder — `gather(..., return_exceptions=True)`\n\nOne poisoned task shouldn't nuke an entire fan-out batch.\n"))
    cells.append(
        cell_code(
            '''import asyncio


async def flaky_shard() -> str:
    raise ValueError("timeout from AZ-1")

async def healthy_shard() -> str:
    return "chunk-42"


mixed = await asyncio.gather(flaky_shard(), healthy_shard(), return_exceptions=True)
print(mixed)'''
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
            "`11-collections-itertools-functools.ipynb` (extended track); then `../python-foundations-beginner-to-advanced.ipynb`",
            [
                "Write assertions for pure helpers.",
                "Isolate filesystem tests with tmp paths.",
                "Think about pytest adoption next.",
            ],
            [
                "Assertions & param tables",
                "Tmp paths",
                "Debugging hooks",
                "Progressive drills — expected failures → float tolerances → canonical dict hashes",
                "Exercise — test `truncate`",
            ],
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

    cells.append(
        drill_header(
            "Testing mindset prevents regressions when prompts/tools change hourly—practice **negative paths**, **float fuzz**, **snapshot comparisons**."
        )
    )
    cells.append(cell_md("### A · Easiest — expect failures (`pytest` preview)\n\nGuard rails should explode loudly when inputs violate contracts.\n"))
    cells.append(
        cell_code(
            '''def budget_tokens(tokens: int) -> None:
    if tokens <= 0:
        raise ValueError("tokens must be positive")


try:
    budget_tokens(-5)
except ValueError:
    print("caught invalid budget")'''
        )
    )

    cells.append(cell_md("### B · Medium — floating comparisons\n\nNever assert raw `==` on uninformed embeddings analog math.\n"))
    cells.append(
        cell_code(
            '''def approx_eq(a: float, b: float, eps: float = 1e-9) -> bool:
    return abs(a - b) <= eps


assert approx_eq(0.1 + 0.2, 0.3)
print("float guard ok")'''
        )
    )

    cells.append(cell_md("### C · Harder — canonical JSON fingerprints\n\nStable dumps detect accidental dict reorder regressions.\n"))
    cells.append(
        cell_code(
            '''import json


def canonical_json(payload: dict) -> str:
    return json.dumps(payload, sort_keys=True)


left = {"model": "mini", "kwargs": {"top_k": 8}}
right = {"kwargs": {"top_k": 8}, "model": "mini"}
assert canonical_json(left) == canonical_json(right)
print("snapshots match")'''
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


def nb11() -> None:
    cells: list[dict[str, Any]] = []
    cells.extend(
        banner(
            "11",
            "Collections, itertools & functools",
            "Intermediate",
            "`10-testing-debugging.ipynb`",
            "`12-logging-for-pipelines.ipynb`",
            [
                "Choose `Counter`, `defaultdict`, and `deque` for ingestion-shaped code.",
                "Compose iterators with `itertools` instead of nested loops.",
                "Memoize pure lookups with `functools.lru_cache` where appropriate.",
            ],
            [
                "`collections` recipes",
                "`itertools` building blocks",
                "`functools` helpers",
                "Progressive drills — grouping → chaining iterators → cached stubs",
                "Exercise — overlapping windows generator",
            ],
        )
    )

    cells.append(
        section_header(
            "1 · `collections` recipes",
            "*Explanation:* **`defaultdict`** drops boilerplate when bucketing retrieval hits by `doc_id`. **`Counter`** answers “top noisy tokens” questions without manual dict increments.",
        )
    )
    cells.append(
        cell_code(
            '''from collections import Counter, defaultdict

hits = [
    {"doc_id": "wiki:42", "score": 0.9},
    {"doc_id": "ticket:7", "score": 0.4},
    {"doc_id": "wiki:42", "score": 0.8},
]
by_doc: dict[str, list[float]] = defaultdict(list)
for h in hits:
    by_doc[h["doc_id"]].append(h["score"])

tokens = "chunk chunk tokens tokens tokens".split()
print(dict(by_doc))
print(Counter(tokens).most_common(2))'''
        )
    )

    cells.append(
        section_header(
            "2 · `itertools` building blocks",
            "*Explanation:* **`chain`** flattens batches; **`islice`** trims infinite iterators — patterns that mirror streaming corpora.",
        )
    )
    cells.append(
        cell_code(
            '''from itertools import chain, islice

batch_a = ["doc-a1", "doc-a2"]
batch_b = ["doc-b1"]
for doc_id in chain(batch_a, batch_b):
    print("ingest", doc_id)


def backoff_seconds():
    """Yield suggested retry delays without storing the whole schedule."""
    base = 0.05
    while True:
        yield base
        base = min(base * 2, 2.0)


print(list(islice(backoff_seconds(), 5)))'''
        )
    )

    cells.append(
        section_header(
            "3 · `functools` helpers",
            "*Explanation:* **`lru_cache`** caches immutable-key lookups — useful for stub embedding dictionaries during offline tests.",
        )
    )
    cells.append(
        cell_code(
            '''from functools import lru_cache


@lru_cache(maxsize=256)
def fake_embed_dimension(text: str) -> int:
    # Pretend expensive tokenizer lookup
    return len(text.split()) * 4


print(fake_embed_dimension("rag pipeline"))
print(fake_embed_dimension("rag pipeline"))  # hits cache'''
        )
    )

    cells.append(
        drill_header(
            "Bridge **tabular ingestion** utilities with lazy iterators — memory stays flat while sophistication rises."
        )
    )
    cells.append(cell_md("### A · Easiest — bucket lines by prefix\n\nRoute stderr vs stdout-shaped records without nested `if` chains.\n"))
    cells.append(
        cell_code(
            '''from collections import defaultdict

rows = ["OUT: ok", "ERR: timeout", "OUT: shipped"]
bucket = defaultdict(list)
for row in rows:
    kind, _, msg = row.partition(": ")
    bucket[kind].append(msg)

print(dict(bucket))'''
        )
    )

    cells.append(cell_md("### B · Medium — flatten nested IDs\n\nMirror merging shards before dedupe.\n"))
    cells.append(
        cell_code(
            '''from itertools import chain

nested = [["u1", "u2"], ["u3"], ["u4", "u5"]]
flat = list(chain.from_iterable(nested))
print(flat)'''
        )
    )

    cells.append(cell_md("### C · Harder — bounded batches without storing everything\n\nChunk embedding batches from any iterable.\n"))
    cells.append(
        cell_code(
            '''from collections.abc import Iterator


def batched_lines(lines: Iterator[str], size: int):
    batch: list[str] = []
    for line in lines:
        batch.append(line)
        if len(batch) >= size:
            yield batch
            batch = []
    if batch:
        yield batch


demo = batched_lines(iter(["a", "b", "c", "d", "e"]), 2)
print(list(demo))'''
        )
    )

    cells.append(
        cell_md(
            "### Exercise — overlapping windows\n\nImplement `windowed(text: str, k: int)` as a **generator** yielding each substring of length `k` with stride `1`. Raise `ValueError` if `k < 1` or `k > len(text)`.\n\nExample: `list(windowed(\"abcd\", 2)) == [\"ab\", \"bc\", \"cd\"]`.\n"
        )
    )
    cells.append(
        cell_code(
            '''from collections.abc import Iterator


def windowed(text: str, k: int) -> Iterator[str]:
    raise NotImplementedError


assert list(windowed("abcd", 2)) == ["ab", "bc", "cd"]
assert list(windowed("hi", 2)) == ["hi"]
print("OK")'''
        )
    )
    cells.append(
        solution_md(
            "windowed",
            'from collections.abc import Iterator\n\ndef windowed(text: str, k: int) -> Iterator[str]:\n    if k < 1 or k > len(text):\n        raise ValueError("bad window")\n    for i in range(len(text) - k + 1):\n        yield text[i : i + k]',
        )
    )

    write_nb("11-collections-itertools-functools.ipynb", cells)


def nb12() -> None:
    cells: list[dict[str, Any]] = []
    cells.extend(
        banner(
            "12",
            "Logging for pipelines & services",
            "Intermediate",
            "`11-collections-itertools-functools.ipynb`",
            "`13-regex-text-extraction.ipynb`",
            [
                "Configure module-level loggers instead of sprinkling `print`.",
                "Attach correlation-style fields without bespoke format strings everywhere.",
                "Understand propagation — avoid duplicate handlers during experiments.",
            ],
            [
                "Logger hierarchy",
                "`LoggerAdapter` patterns",
                "Propagation pitfall",
                "Progressive drills — basic emit → retry banner → suppress noisy libraries",
                "Exercise — timing helper logs duration",
            ],
        )
    )

    cells.append(section_header("1 · Logger hierarchy", "*Explanation:* **`logging.getLogger(__name__)`** preserves module paths in logs — grep-friendly once files multiply."))
    cells.append(
        cell_code(
            '''import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s %(message)s")
log = logging.getLogger(__name__)

log.info("pipeline_start")
log.warning("high_latency_bucket", extra={"shard": "east", "p95_ms": 842})'''
        )
    )

    cells.append(section_header("2 · `LoggerAdapter` for correlation IDs", "*Explanation:* **`LoggerAdapter`** prefixes repeated fields (`rid`, `tenant`) without rewriting every call site — JSON formatters plug in later."))
    cells.append(
        cell_code(
            '''import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")


class RidAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        rid = self.extra.get("rid", "-")
        return f"[rid={rid}] {msg}", kwargs


base = logging.getLogger("ingest.worker")
adapted = RidAdapter(base, {"rid": "trace-884"})
adapted.info("embedding_batch_started docs=%s tokens=%s", 128, 40_192)'''
        )
    )

    cells.append(
        section_header(
            "3 · Propagation pitfall",
            "*Explanation:* Child loggers bubble to parents — duplicate handlers cause duplicate lines; attach handlers at **one** level during notebooks.",
        )
    )
    cells.append(
        cell_code(
            '''import logging

root = logging.getLogger()
root.handlers.clear()
logging.basicConfig(level=logging.INFO)

inner = logging.getLogger("outer.shard")
inner.info("single_line_only")'''
        )
    )

    cells.append(
        drill_header(
            "Production debugging rides on **consistent fields** — practice emitting retries, timeouts, and vendor IDs."
        )
    )
    cells.append(cell_md("### A · Easiest — severity routing\n\nReserve WARNING for anomalies operators page on.\n"))
    cells.append(
        cell_code(
            '''import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger("demo")

log.debug("tokenizer_cache_hit")
log.info("request_complete status=200")'''
        )
    )

    cells.append(cell_md("### B · Medium — retry transcript\n\nStructured retries explain flaky vendors faster than prose.\n"))
    cells.append(
        cell_code(
            '''import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger("vendor")

for attempt in range(1, 4):
    sleep_s = round(0.2 * attempt, 3)
    log.warning("retry_schedule attempt=%s sleep_s=%s", attempt, sleep_s)'''
        )
    )

    cells.append(cell_md("### C · Harder — silence chatty third-party logs\n\nFlip libraries down to WARNING during demos.\n"))
    cells.append(
        cell_code(
            '''import logging

logging.basicConfig(level=logging.INFO)
logging.getLogger("urllib3").setLevel(logging.WARNING)

root = logging.getLogger()
root.info("your_signal_remains_visible")'''
        )
    )

    cells.append(
        cell_md(
            "### Exercise — log timed block\n\nImplement `log_duration(log: logging.Logger, label: str)` as a **context manager** (using `contextlib.contextmanager`) that logs `START label` / `END label ms=...` at INFO using `time.perf_counter()`.\n"
        )
    )
    cells.append(
        cell_code(
            '''import logging
from collections.abc import Iterator
from contextlib import contextmanager

logging.basicConfig(level=logging.INFO, format="%(message)s")


@contextmanager
def log_duration(log: logging.Logger, label: str) -> Iterator[None]:
    raise NotImplementedError


demo_log = logging.getLogger("timing")

with log_duration(demo_log, "fake_embed"):
    sum(range(1000))

print("done")'''
        )
    )
    cells.append(
        solution_md(
            "log_duration",
            "import logging\nimport time\nfrom collections.abc import Iterator\nfrom contextlib import contextmanager\n\n@contextmanager\ndef log_duration(log: logging.Logger, label: str) -> Iterator[None]:\n    log.info(\"START %s\", label)\n    t0 = time.perf_counter()\n    try:\n        yield\n    finally:\n        ms = (time.perf_counter() - t0) * 1000\n        log.info(\"END %s ms=%.2f\", label, ms)",
        )
    )

    write_nb("12-logging-for-pipelines.ipynb", cells)


def nb13() -> None:
    cells: list[dict[str, Any]] = []
    cells.extend(
        banner(
            "13",
            "Regex & text hygiene",
            "Intermediate",
            "`12-logging-for-pipelines.ipynb`",
            "`14-bytes-encoding-files.ipynb`",
            [
                "Compile patterns once when reused.",
                "Prefer parsers over regex for HTML — but regex shines at fence/tag hygiene.",
                "Know greedy vs non-greedy boundaries around citations.",
            ],
            [
                "Compiled patterns",
                "Citation-shaped extraction",
                "Fence stripping mindset",
                "Progressive drills — digits → bracket tags → fenced JSON blocks",
                "Exercise — strip loose citations",
            ],
        )
    )

    cells.append(section_header("1 · Compiled patterns", "*Explanation:* **`re.compile`** amortizes parsing cost across thousands of chunks."))
    cells.append(
        cell_code(
            '''import re

MODEL_REF = re.compile(r"model[=:]\\s*(\\w+)", re.I)

text = "Retry model=gpt-mini then Model: opus"
print(MODEL_REF.findall(text))'''
        )
    )

    cells.append(section_header("2 · Citation-shaped extraction", "*Explanation:* Retrieval QA answers often emit `[source: doc]` snippets — normalize before persistence."))
    cells.append(
        cell_code(
            '''import re

CITE = re.compile(r"\\[source:\\s*([^\\]]+)\\]", re.I)

answer = "Latency dropped [source: runbook section 4] after caching."
print(CITE.findall(answer))'''
        )
    )

    cells.append(section_header("3 · Fence stripping mindset", "*Explanation:* Models wrap JSON inside markdown fences — peel fences before `json.loads`."))
    cells.append(
        cell_code(
            '''import json
import re

FENCE = re.compile(r"```(?:json)?\\s*(.*?)```", re.S | re.I)


def loads_maybe_fenced(blob: str) -> dict:
    m = FENCE.search(blob)
    core = m.group(1) if m else blob
    return json.loads(core.strip())


fence_json = "```json"
body = '{"tool": "search", "query": "logs"}'
raw = "Here you go:\\n" + fence_json + "\\n" + body + "\\n" + "```" + "\\n"
print(loads_maybe_fenced(raw))'''
        )
    )

    cells.append(
        drill_header(
            "**Messy strings** arrive hourly — drills tighten hygiene without brittle copy/paste parsers."
        )
    )
    cells.append(cell_md("### A · Easiest — grab integers\n\nPull numeric budgets out of prose instructions.\n"))
    cells.append(
        cell_code(
            '''import re

budget = re.findall(r"max_tokens[=:]\\s*(\\d+)", "please cap max_tokens: 2048 please")
print(budget)'''
        )
    )

    cells.append(cell_md("### B · Medium — normalize whitespace collapse\n\nCollapse accidental double spaces before hashing prompts.\n"))
    cells.append(
        cell_code(
            '''import re

messy = "hello   world\\n\\tagain"
clean = re.sub(r"\\s+", " ", messy.strip())
print(clean)'''
        )
    )

    cells.append(cell_md("### C · Harder — capture balanced-ish bullet IDs\n\nMirror extracting `[chunk::uuid]` markers.\n"))
    cells.append(
        cell_code(
            '''import re

tag = re.compile(r"\\[chunk::([a-z0-9\\-]{8,})\\]", re.I)
text = "See [chunk::ab12cd34-eeee] for detail."
print(tag.findall(text))'''
        )
    )

    cells.append(
        cell_md(
            "### Exercise — citations only\n\nImplement `strip_citations(answer: str) -> str` removing every `[source: ...]` substring (including brackets), leaving single spaces where multiples collapsed.\n"
        )
    )
    cells.append(
        cell_code(
            '''import re


def strip_citations(answer: str) -> str:
    raise NotImplementedError


dirty = "OK [source: a] maybe [SOURCE: second]"
assert strip_citations(dirty).strip() == "OK maybe"
print("OK")'''
        )
    )
    cells.append(
        solution_md(
            "strip_citations",
            'import re\n\n_CITES = re.compile(r"\\[source:\\s*[^\\]]+\\]", re.I)\n\ndef strip_citations(answer: str) -> str:\n    return re.sub(r"\\s+", " ", _CITES.sub("", answer)).strip()',
        )
    )

    write_nb("13-regex-text-extraction.ipynb", cells)


def nb14() -> None:
    cells: list[dict[str, Any]] = []
    cells.extend(
        banner(
            "14",
            "Bytes, encoding & binary-shaped files",
            "Intermediate → Advanced",
            "`13-regex-text-extraction.ipynb`",
            "`15-subprocess-and-archives.ipynb`",
            [
                "Treat encode/decode as explicit boundaries around APIs and disk.",
                "Decode safely when vendors emit malformed UTF-8.",
                "Peek binary headers without loading entire artifacts.",
            ],
            [
                "UTF-8 encode/decode",
                "Error handlers (`errors=`)",
                "`pathlib` bytes paths",
                "Progressive drills — literals → sloppy bytes → sniff magic header",
                "Exercise — stable SHA256 chunks reader",
            ],
        )
    )

    cells.append(section_header("1 · UTF-8 encode/decode", "*Explanation:* HTTP bodies and protobuf-adjacent workflows hop between **`str`** and **`bytes`**."))
    cells.append(
        cell_code(
            '''utf8 = "prompt €".encode()
print(utf8, utf8.decode())'''
        )
    )

    cells.append(section_header("2 · Error handlers (`errors=`)", "*Explanation:* Offline scrapes often contain broken sequences — **`replace`** or **`ignore`** beats crashing ingestion."))
    cells.append(
        cell_code(
            '''broken = b"hello \\xff world"
print(broken.decode("utf-8", errors="replace"))'''
        )
    )

    cells.append(section_header("3 · `pathlib` byte slices", "*Explanation:* Inspect tiny prefixes (magic numbers) before committing parsers."))
    cells.append(
        cell_code(
            '''from pathlib import Path

tmp = Path("sample_blob.bin")
tmp.write_bytes(b"PK\\x03\\x04fake-zip-prefix")

try:
    header = tmp.read_bytes()[:4]
    print(header)
finally:
    tmp.unlink(missing_ok=True)'''
        )
    )

    cells.append(
        drill_header(
            "**Embedding caches** and **audio chunks** frequently arrive as bytes — boundary discipline prevents mysterious Unicode crashes."
        )
    )
    cells.append(cell_md("### A · Easiest — hex fingerprints\n\nCompare checksum prefixes quickly.\n"))
    cells.append(
        cell_code(
            '''blob = b"abc"
print(blob.hex())'''
        )
    )

    cells.append(cell_md("### B · Medium — newline normalization bytes-side\n\nSometimes normalize `\\r\\n` before decoding.\n"))
    cells.append(
        cell_code(
            '''raw = b"line\\r\\nline\\r\\n"
text = raw.replace(b"\\r\\n", b"\\n").decode()
print(text.splitlines())'''
        )
    )

    cells.append(cell_md("### C · Harder — `memoryview` zero-copy slice\n\nLarge buffers benefit from slicing without copying immediately.\n"))
    cells.append(
        cell_code(
            '''payload = bytearray(b"HEADERPAYLOADTRAILER")
view = memoryview(payload)
chunk = view[6:13]
print(bytes(chunk))'''
        )
    )

    cells.append(
        cell_md(
            "### Exercise — chunked hex digest\n\nImplement `sha256_hex_chunks(path: Path, chunk_size: int = 65536) -> str` returning lowercase hex SHA256 of **file contents** reading in chunks (use `hashlib.sha256`). Works for empty files.\n"
        )
    )
    cells.append(
        cell_code(
            '''from hashlib import sha256
from pathlib import Path


def sha256_hex_chunks(path: Path, chunk_size: int = 65536) -> str:
    raise NotImplementedError


p = Path("_tmp_digest_demo.bin")
p.write_bytes(b"hello-world")
try:
    assert sha256_hex_chunks(p) == sha256(b"hello-world").hexdigest()
finally:
    p.unlink(missing_ok=True)
print("OK")'''
        )
    )
    cells.append(
        solution_md(
            "sha256_hex_chunks",
            "from hashlib import sha256\nfrom pathlib import Path\n\ndef sha256_hex_chunks(path: Path, chunk_size: int = 65536) -> str:\n    h = sha256()\n    with path.open(\"rb\") as fh:\n        while True:\n            chunk = fh.read(chunk_size)\n            if not chunk:\n                break\n            h.update(chunk)\n    return h.hexdigest()",
        )
    )

    write_nb("14-bytes-encoding-files.ipynb", cells)


def nb15() -> None:
    cells: list[dict[str, Any]] = []
    cells.extend(
        banner(
            "15",
            "Subprocess safety & zip archives",
            "Advanced",
            "`14-bytes-encoding-files.ipynb`",
            "`../python-foundations-beginner-to-advanced.ipynb` + `../CURRICULUM-A-Z.md`",
            [
                "Invoke CLI tools with argv lists — avoid `shell=True` defaults.",
                "Capture stdout/stderr with timeouts that match ops expectations.",
                "Inspect `.zip` artifacts without blindly extracting trees.",
            ],
            [
                "`subprocess.run` patterns",
                "Timeouts & error surfaces",
                "`zipfile` introspection",
                "Progressive drills — argv vs shell → failing commands → largest member listing",
                "Exercise — bounded `git` revision helper",
            ],
        )
    )

    cells.append(
        section_header(
            "1 · `subprocess.run` patterns",
            "*Explanation:* Wrap **`git`**, **`ffmpeg`**, or codegen CLIs — pass **`list[str]`** argv so shells never interpolate secrets oddly.",
        )
    )
    cells.append(
        cell_code(
            '''import subprocess

completed = subprocess.run(
    ["python", "-c", "print('hello-from-cli')"],
    capture_output=True,
    text=True,
    check=True,
)
print(completed.stdout.strip())'''
        )
    )

    cells.append(section_header("2 · Timeouts & error surfaces", "*Explanation:* Hanging CLI calls stall workers — **`timeout=`** converts hangs into actionable exceptions."))
    cells.append(
        cell_code(
            '''import subprocess

try:
    subprocess.run(["python", "-c", "import time; time.sleep(10)"], timeout=0.05)
except subprocess.TimeoutExpired as exc:
    print("stopped:", type(exc).__name__)'''
        )
    )

    cells.append(section_header("3 · `zipfile` introspection", "*Explanation:* Dataset bundles arrive zipped — **`ZipFile.infolist`** exposes sizes before extraction."))
    cells.append(
        cell_code(
            '''from pathlib import Path
import zipfile

bundle = Path("_demo_bundle.zip")
with zipfile.ZipFile(bundle, "w") as zf:
    zf.writestr("small.txt", "x")
    zf.writestr("folder/big.bin", "y" * 200)

try:
    with zipfile.ZipFile(bundle) as zf:
        infos = sorted(zf.infolist(), key=lambda i: i.file_size, reverse=True)
        print([(i.filename, i.file_size) for i in infos[:2]])
finally:
    bundle.unlink(missing_ok=True)'''
        )
    )

    cells.append(
        drill_header(
            "**Glue code** orchestrates binaries — drills reinforce safety habits before wiring agents to local tools."
        )
    )
    cells.append(cell_md("### A · Easiest — argv list quoting\n\nPython receives arguments cleanly — no manual escaping.\n"))
    cells.append(
        cell_code(
            '''import subprocess

out = subprocess.run(
    ["python", "-c", "import sys; print(sys.argv[1])", "multi word argument"],
    capture_output=True,
    text=True,
    check=True,
)
print(out.stdout.strip())'''
        )
    )

    cells.append(cell_md("### B · Medium — tolerate nonzero exits\n\nSometimes stderr carries signal — inspect **`returncode`** instead of crashing silently.\n"))
    cells.append(
        cell_code(
            '''import subprocess

completed = subprocess.run(["python", "-c", "raise SystemExit(2)"], capture_output=True)
print("code", completed.returncode)'''
        )
    )

    cells.append(cell_md("### C · Harder — zip-slip mindset\n\nNormalize-member paths mentally — refuse `..` escapes before extracting.\n"))
    cells.append(
        cell_code(
            '''from pathlib import PurePosixPath


def safe_member(name: str) -> bool:
    dest = PurePosixPath(name)
    return dest.parts and not dest.is_absolute() and ".." not in dest.parts


print(safe_member("../evil.txt"), safe_member("data/file.txt"))'''
        )
    )

    cells.append(
        cell_md(
            "### Exercise — `git_head`\n\nImplement `git_head(repo: Path | None = None, timeout: float = 2.0) -> str` running `git rev-parse HEAD` via **`subprocess.run`**. If `repo` is given, pass **`cwd=str(repo)`**. On failure (**nonzero exit** or **`TimeoutExpired`**), return `\"unknown\"`. Trim whitespace from stdout.\n"
        )
    )
    cells.append(
        cell_code(
            '''from pathlib import Path
import subprocess


def git_head(repo: Path | None = None, timeout: float = 2.0) -> str:
    raise NotImplementedError


print(git_head())'''
        )
    )
    cells.append(
        solution_md(
            "git_head",
            'from pathlib import Path\nimport subprocess\n\ndef git_head(repo: Path | None = None, timeout: float = 2.0) -> str:\n    cmd = ["git", "rev-parse", "HEAD"]\n    kw = {"cwd": str(repo)} if repo else {}\n    try:\n        proc = subprocess.run(\n            cmd,\n            capture_output=True,\n            text=True,\n            timeout=timeout,\n            check=False,\n            **kw,\n        )\n    except subprocess.TimeoutExpired:\n        return "unknown"\n    if proc.returncode != 0:\n        return "unknown"\n    return proc.stdout.strip()',
        )
    )

    write_nb("15-subprocess-and-archives.ipynb", cells)


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
    nb11()
    nb12()
    nb13()
    nb14()
    nb15()
    print("Done. Generated 15 notebooks in", OUT_DIR)


if __name__ == "__main__":
    main()
