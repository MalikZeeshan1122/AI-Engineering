# Datetime & timezones (`datetime`, `zoneinfo`)

## Purpose

Parse ISO timestamps from APIs/logs and convert safely across zones — avoids silent “UTC vs local” bugs in ingestion pipelines.

## Pair with

- **[`../exercises/04-modules-json-pathlib.ipynb`](../exercises/04-modules-json-pathlib.ipynb)** (structured payloads often embed timestamps)

## Files

| Script | Notes |
|--------|--------|
| **`timezone_demo.py`** | `datetime.fromisoformat` + **`ZoneInfo`** |

## Run

```bash
cd 03-python-foundations
python datetime_intro/timezone_demo.py
```

**Dependencies:** stdlib (**`zoneinfo`** requires timezone data — bundled on Python **3.9+** on Windows/macOS/Linux modern builds).
