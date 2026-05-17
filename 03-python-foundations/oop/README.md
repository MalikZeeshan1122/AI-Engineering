# Object-oriented Python — notebook track

Three Jupyter notebooks from **beginner → advanced**. Each ties core ideas to **daily life**, then exercises.

| Order | Notebook | Everyday hook |
|-------|----------|----------------|
| 1 | [`01-oop-beginner-blueprints-and-objects.ipynb`](01-oop-beginner-blueprints-and-objects.ipynb) | Recipes vs trays of cookies, alarm clocks, coffee makers |
| 2 | [`02-oop-intermediate-house-rules.ipynb`](02-oop-intermediate-house-rules.ipynb) | Piggy banks, thermostats, bikes vs buses, backpacks |
| 3 | [`03-oop-advanced-contracts-and-plugins.ipynb`](03-oop-advanced-contracts-and-plugins.ipynb) | Library cards, checkout lanes, airport chargers, smart-home toggles |

## Regenerate notebooks

From `03-python-foundations/`:

```bash
python oop/build_oop_notebooks.py
```

Requires Python **3.10+**.

## Pair with

- [`../exercises/05-classes-oop.ipynb`](../exercises/05-classes-oop.ipynb) — lighter-weight single notebook slice.
- [`../CURRICULUM-A-Z.md`](../CURRICULUM-A-Z.md) — letter **O** (composition / SOLID-lite).

After exercises, rename mental models for AI code: **Blueprint → Tool class**, **Protocol → swap-in embedder**, **Composition → pipeline owns retriever**.
