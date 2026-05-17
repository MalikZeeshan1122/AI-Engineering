# `decorators/` — cross-cutting wrappers

## Purpose

Shows how **decorators** attach reusable behavior (timing, retries) without copying boilerplate—directly relevant to timing LLM calls, caching embeddings in tests, or retrying flaky HTTP.

## Pair with notebooks

| Notebook | Topics echoed here |
|----------|---------------------|
| **[`../exercises/07-decorators-generators.ipynb`](../exercises/07-decorators-generators.ipynb)** | `functools.wraps`, decorator stacking mindset |

## Files

| Script | What it demonstrates |
|--------|----------------------|
| **`timed_call.py`** | Minimal **`@timed`** wrapper measuring milliseconds |
| **`retry_with_backoff.py`** | Retry decorator with capped exponential backoff + jitter |

## Run

```bash
cd 03-python-foundations
python decorators/timed_call.py
python decorators/retry_with_backoff.py
```

**Dependencies:** stdlib (**`functools`**, **`time`**, **`random`**).

## Next steps

Combine with **`logging/`** or **`httpx`** error classes once notebooks **12** and **19** are familiar.
