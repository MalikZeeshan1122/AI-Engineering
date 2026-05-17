# `async/` — `asyncio` scripts

## Purpose

Small **terminal-runnable** examples for **`asyncio`**: overlapping waits, queues, blocking offload, and **async iteration**. They reinforce notebook concepts without opening Jupyter.

## Pair with notebooks

| Notebook | Topics echoed here |
|----------|---------------------|
| **[`../exercises/09-async-io.ipynb`](../exercises/09-async-io.ipynb)** | `gather`, parallelism vs sequential sleeps, semaphores, `asyncio.to_thread` |
| **[`../exercises/18-asyncio-queue-pipelines.ipynb`](../exercises/18-asyncio-queue-pipelines.ipynb)** | `asyncio.Queue`, bounds, sentinel shutdown |

## Files

| Script | What it demonstrates |
|--------|----------------------|
| **`async_gather_demo.py`** | Sequential `await` vs **`asyncio.gather`** wall-clock overlap |
| **`async_queue_demo.py`** | Producer + consumer + **`task_done`** / **`join`** shape |
| **`async_to_thread_demo.py`** | **`asyncio.to_thread`** for blocking CPU/sleep-style work |
| **`async_generator_demo.py`** | **`async for`** over an async generator (streaming-shaped tokens) |

## Run

Always **`cd`** into **`03-python-foundations`** first (paths assume that):

```bash
cd 03-python-foundations
python async/async_gather_demo.py
python async/async_queue_demo.py
python async/async_to_thread_demo.py
python async/async_generator_demo.py
```

**Dependencies:** stdlib **`asyncio`** only.

## Next steps

Move patterns into **`httpx.AsyncClient`** or FastAPI routes after notebooks **09**, **18**, and **19**.
