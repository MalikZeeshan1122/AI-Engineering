# `generators/` — lazy iteration & chunking

## Purpose

**Generators** keep memory flat while streaming batches—natural fit for token streams, JSONL ingestion, and sliding chunk windows before embeddings.

## Pair with notebooks

| Notebook | Topics echoed here |
|----------|---------------------|
| **[`../exercises/07-decorators-generators.ipynb`](../exercises/07-decorators-generators.ipynb)** | `yield`, iterator pipelines |
| **[`../exercises/05-classes-oop.ipynb`](../exercises/05-classes-oop.ipynb)** | Chunk-shaped processing alongside classes |

## Files

| Script | What it demonstrates |
|--------|----------------------|
| **`read_chunks.py`** | **`batched`** generator—fixed-size lists from any iterable |
| **`overlapping_windows.py`** | Sliding windows over text (`stride` controls overlap) |

## Run

```bash
cd 03-python-foundations
python generators/read_chunks.py
python generators/overlapping_windows.py
```

**Dependencies:** stdlib only.

## Next steps

Wire **`batched`** into file readers (`pathlib`) after notebook **04**, or combine with **`async`** producers after **18**.
