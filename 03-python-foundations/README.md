# Python foundations

Core and **advanced** Python for AI engineering—before leaning hard on frameworks.

## Learn interactively — beginner → advanced notebook

Open **`python-foundations-beginner-to-advanced.ipynb`** in Jupyter / VS Code / Cursor:

- Markdown **Explanation** cells + runnable **Examples**
- Parts **1–3**: core Python → intermediate → typing, dataclasses, decorators, generators, protocols, asyncio
- Part **4**: **Practice exercises** (`# YOUR CODE HERE`, assertions)
- Part **5**: **Solutions** — open only after you try Part 4

Run cells **top to bottom**. If the asyncio cell fails on `await`, use `asyncio.run(main())` instead (see the note cell below it).

## Day 3 — advanced A→Z spine

Open **[`CURRICULUM-A-Z.md`](CURRICULUM-A-Z.md)** for the full alphabet (why each topic matters for LLMs/RAG/agents + drills).

Suggested layout:

```
03-python-foundations/
├── python-foundations-beginner-to-advanced.ipynb   ← guided path + examples
├── CURRICULUM-A-Z.md   ← drill checklist / deeper map
├── oop/
├── async/
├── decorators/
├── generators/
├── typing/
└── exercises/
```

Work pattern: pick 1–2 letters per session, implement the **ship-sized drill** under `exercises/` (create `exercises/day-03-*` files as you go), and log outcomes in `01-daily-log/`.
