# Profiling intro (`tracemalloc`)

## Purpose

Letter **M** in **[`../CURRICULUM-A-Z.md`](../CURRICULUM-A-Z.md)** — peek at allocator-backed usage before blaming “Python is slow.”

## Pair with

- **[`../exercises/16-numpy-embeddings-shape.ipynb`](../exercises/16-numpy-embeddings-shape.ipynb)** (batch RAM intuition)

## Files

| Script | Notes |
|--------|--------|
| **`tracemalloc_demo.py`** | Start/stop **`tracemalloc`**, print current vs peak RSS-ish heap traces |

## Run

```bash
cd 03-python-foundations
python profiling_intro/tracemalloc_demo.py
```

**Dependencies:** stdlib only.
