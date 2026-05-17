# `logging/` — structured-ish logs

## Purpose

Replace stray **`print`** with **`logging`** hierarchy + adapters that prepend correlation IDs—critical once pipelines fan out across vendors and shards.

## Pair with notebooks

| Notebook | Topics echoed here |
|----------|---------------------|
| **[`../exercises/12-logging-for-pipelines.ipynb`](../exercises/12-logging-for-pipelines.ipynb)** | `LoggerAdapter`, basic propagation hygiene |

## Files

| Script | What it demonstrates |
|--------|----------------------|
| **`correlation_log_demo.py`** | **`LoggerAdapter`** injecting a fake **`rid=`** prefix on INFO/WARNING lines |

## Run

```bash
cd 03-python-foundations
python logging/correlation_log_demo.py
```

**Dependencies:** stdlib **`logging`** only.

## Next steps

Add JSON **`Formatter`** handlers or bind **`contextvars`** for real trace IDs (see **`CURRICULUM-A-Z.md`** letter **L**).
