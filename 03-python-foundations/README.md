# Python foundations

Core and **advanced** Python for AI engineering—before leaning hard on frameworks.

## Step-by-step curriculum notebooks (`exercises/`)

Ten notebooks (**01 → 10**) from beginner syntax through async and testing — **MOOC-style layout** (objectives, TOC, demos, exercises, collapsible solutions). Start here for structured daily progress:

**[`exercises/README.md`](exercises/README.md)** — open [`exercises/01-syntax-values-and-io.ipynb`](exercises/01-syntax-values-and-io.ipynb) first.

Regenerate all notebooks after editing the generator (from `03-python-foundations/`):

```bash
python exercises/build_curriculum_notebooks.py
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
├── exercises/                         ← 01–10 progressive notebooks + README
│   ├── build_curriculum_notebooks.py   ← regenerate .ipynb files
│   └── 01-syntax-values-and-io.ipynb … 10-testing-debugging.ipynb
├── python-foundations-beginner-to-advanced.ipynb   ← single spiral + Parts 4–5 drills
├── CURRICULUM-A-Z.md                  ← topic → drill map
├── oop/ · async/ · decorators/ · generators/ · typing/
└── exercises/README.md                ← curriculum table & format notes
```

Work pattern: follow **`exercises/`** notebooks in order; use **`CURRICULUM-A-Z.md`** for extra drills; drop standalone `.py` experiments into topic folders as you grow out of notebooks; log in **`01-daily-log/`**.
