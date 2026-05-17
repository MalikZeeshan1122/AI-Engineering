# Object-oriented Python — notebook track (`oop/`)

This folder is an **optional parallel track** focused purely on **object-oriented programming**, taught through **daily-life analogies** (recipes, piggy banks, checkout lanes). Use it when metaphors help more than abstract “design patterns.”

---

## What’s inside

| File | Role |
|------|------|
| **`01-oop-beginner-blueprints-and-objects.ipynb`** | Beginner OOP: objects as blueprints vs instances; drills ramp easy→medium. |
| **`02-oop-intermediate-house-rules.ipynb`** | Intermediate: encapsulation-style stories + staged drills. |
| **`03-oop-advanced-contracts-and-plugins.ipynb`** | Advanced: contracts, equality, composition/registry hooks + drills. |
| **`build_oop_notebooks.py`** | **Generator** for the three notebooks above—run it after edits instead of hand-maintaining duplicates. |

---

## Order to open

| Order | Notebook | Everyday hook |
|-------|----------|----------------|
| 1 | [`01-oop-beginner-blueprints-and-objects.ipynb`](01-oop-beginner-blueprints-and-objects.ipynb) | Recipes vs trays of cookies, alarm clocks, coffee makers + drills |
| 2 | [`02-oop-intermediate-house-rules.ipynb`](02-oop-intermediate-house-rules.ipynb) | Piggy banks, thermostats, bikes vs buses + staged drills |
| 3 | [`03-oop-advanced-contracts-and-plugins.ipynb`](03-oop-advanced-contracts-and-plugins.ipynb) | Library cards, checkout lanes, chargers + registry-style drills |

---

## Relationship to the rest of `03-python-foundations`

| Resource | When to use it |
|----------|----------------|
| **[`../exercises/05-classes-oop.ipynb`](../exercises/05-classes-oop.ipynb)** | **Single** notebook slice on classes/composition inside the main 01→22 path—finish this before or alongside **`oop/01`**. |
| **`oop/` track** | **Deeper** OOP storytelling + more drills—ideal after notebook **05** or whenever OOP feels fuzzy. |
| **[`../CURRICULUM-A-Z.md`](../CURRICULUM-A-Z.md)** | Letter **O** — composition / SOLID-lite for AI pipelines. |

Rephrase for AI code mentally: **Blueprint → Tool class**, **Protocol → swappable embedder**, **Composition → pipeline owns retriever**.

---

## Regenerate notebooks

From **`03-python-foundations`**:

```bash
python oop/build_oop_notebooks.py
```

Requires Python **3.10+**.
