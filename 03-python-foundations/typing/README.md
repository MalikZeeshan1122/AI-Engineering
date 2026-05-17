# `typing/` — `Protocol` & dataclasses

## Purpose

Shows **static-shape APIs**: **`typing.Protocol`** for “anything that implements `.embed(...)`”, and **`dataclass(frozen=True)`** for immutable configs—patterns that scale before or beside Pydantic-heavy stacks.

## Pair with notebooks

| Notebook | Topics echoed here |
|----------|---------------------|
| **[`../exercises/08-advanced-typing-protocols-dataclasses.ipynb`](../exercises/08-advanced-typing-protocols-dataclasses.ipynb)** | `Protocol`, `@runtime_checkable`, dataclass flags |

## Files

| Script | What it demonstrates |
|--------|----------------------|
| **`embedder_protocol.py`** | **`Embedder` Protocol + toy backend + batch helper |
| **`model_config_dataclass.py`** | Frozen **`slots=True`** config objects |

## Run

```bash
cd 03-python-foundations
python typing/embedder_protocol.py
python typing/model_config_dataclass.py
```

**Dependencies:** stdlib (**`typing`**, **`dataclasses`**).

## Next steps

Adopt **`mypy`** / **`pyright`** on real modules; evolve configs toward **`pyproject.toml`** after notebook **21**.
