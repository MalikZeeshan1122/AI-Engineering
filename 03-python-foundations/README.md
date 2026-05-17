# Python foundations

Core and **advanced** Python for AI engineering—before leaning hard on frameworks.

## Step-by-step curriculum notebooks (`exercises/`)

**22 notebooks** (**01 → 22**): core **01–10**, stdlib-focused **11–15**, labs **16–18** (**`numpy`**, **`pytest`**, **`asyncio` queues**), then **19–22** (**`httpx`**, **`/` / `*`** signatures, pins / **`venv`**, **`html.parser`**) — **MOOC-style layout** (objectives, TOC, demos, progressive drills, exercises, collapsible solutions). Start here for structured daily progress:

**[`exercises/README.md`](exercises/README.md)** — open [`exercises/01-syntax-values-and-io.ipynb`](exercises/01-syntax-values-and-io.ipynb) first.

Regenerate all notebooks after editing the generator (from `03-python-foundations/`):

```bash
python exercises/build_curriculum_notebooks.py
```

## Object-oriented Python track (`oop/`)

Three notebooks (**beginner → advanced**) built around **daily-life analogies** (recipes, piggy banks, gym tiers, checkout lanes, charging kiosks):

**[`oop/README.md`](oop/README.md)**

Regenerate after editing:

```bash
python oop/build_oop_notebooks.py
```

## Single-volume spiral notebook

Open **`python-foundations-beginner-to-advanced.ipynb`** in Jupyter / VS Code / Cursor:

- Markdown **Explanation** cells + runnable **Examples**
- Parts **1–3**: core Python → intermediate → typing, dataclasses, decorators, generators, protocols, asyncio
- Part **4**: **Practice exercises** (`raise NotImplementedError` stubs, assertions)
- Part **5**: **Solutions** — open only after you try Part 4

Run cells **top to bottom**. If the asyncio cell fails on `await`, use `asyncio.run(main())` instead (see the note cell below it).

## Day 3+ — advanced A→Z spine

Open **[`CURRICULUM-A-Z.md`](CURRICULUM-A-Z.md)** for the full alphabet (why each topic matters for LLMs/RAG/agents + drills).

Suggested layout:

```
03-python-foundations/
├── exercises/           ← 01–22 curriculum notebooks (see exercises/README.md)
├── oop/                 ← 01–03 OOP-only spiral + daily-life stories
├── python-foundations-beginner-to-advanced.ipynb
├── CURRICULUM-A-Z.md
├── async/ · decorators/ · generators/ · typing/
└── README.md files inside exercises/ + oop/
```

Work pattern: follow **`exercises/`** notebooks first; deepen OOP with **`oop/`**; use **`CURRICULUM-A-Z.md`** for extra drills; log in **`01-daily-log/`**.
