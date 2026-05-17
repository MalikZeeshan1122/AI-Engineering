# Threading intro (`concurrent.futures`, `queue`)

## Purpose

**Sync concurrency** vs **`asyncio`**: thread pools for blocking calls, **`queue.Queue`** for producer/consumer — complements letter **Q** (async queues already in notebooks **18**).

## Pair with

- **[`../exercises/09-async-io.ipynb`](../exercises/09-async-io.ipynb)** (`asyncio.to_thread` bridge)
- **[`../exercises/18-asyncio-queue-pipelines.ipynb`](../exercises/18-asyncio-queue-pipelines.ipynb)**

## Files

| Script | Notes |
|--------|--------|
| **`executor_map_demo.py`** | **`ThreadPoolExecutor.map`** |
| **`queue_sync_demo.py`** | **`queue.Queue`** drain |

## Run

```bash
cd 03-python-foundations
python threading_intro/executor_map_demo.py
python threading_intro/queue_sync_demo.py
```

**Dependencies:** stdlib only.
