# Workers mental model (async pipeline sketch)

## Purpose

Letter **W** in **[`../CURRICULUM-A-Z.md`](../CURRICULUM-A-Z.md)** — **producer → transformer → sink** stages without Redis/RQ yet. Treat this as the mental skeleton before **`04-api-engineering/`** job queues.

## Pair with

- **[`../exercises/18-asyncio-queue-pipelines.ipynb`](../exercises/18-asyncio-queue-pipelines.ipynb)**

## Files

| Script | Notes |
|--------|--------|
| **`async_pipeline_demo.py`** | Async generator producer + async stage (“embedding”) |

## Run

```bash
cd 03-python-foundations
python workers_intro/async_pipeline_demo.py
```

**Dependencies:** stdlib **`asyncio`** only.
