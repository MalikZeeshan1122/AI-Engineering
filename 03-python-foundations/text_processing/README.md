# `text_processing/` — LLM-shaped text hygiene

## Purpose

Models often wrap JSON in **markdown fences** (` ```json ... ``` `). This folder holds tiny parsers that strip fences safely before **`json.loads`**—same failure mode as notebook drills.

## Pair with notebooks

| Notebook | Topics echoed here |
|----------|---------------------|
| **[`../exercises/13-regex-text-extraction.ipynb`](../exercises/13-regex-text-extraction.ipynb)** | Compiled **`re`**, fence stripping |

## Files

| Script | What it demonstrates |
|--------|----------------------|
| **`extract_json_fence.py`** | Regex peel-fence → **`json.loads`** → validate **`dict`** |

## Run

```bash
cd 03-python-foundations
python text_processing/extract_json_fence.py
```

**Dependencies:** stdlib **`json`** + **`re`**.

## Next steps

Harden with citation stripping (`regex`), HTML parsing (**notebook 22** / **`html.parser`**), or schema validation libraries once payloads stabilize.
