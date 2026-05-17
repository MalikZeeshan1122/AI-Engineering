"""Strip ```json fences common in LLM replies, then parse JSON."""

from __future__ import annotations

import json
import re

_FENCE = re.compile(r"```(?:json)?\s*(.*?)```", re.S | re.I)


def loads_maybe_fenced(blob: str) -> dict:
    match = _FENCE.search(blob)
    core = match.group(1) if match else blob
    payload = json.loads(core.strip())
    if not isinstance(payload, dict):
        raise TypeError("expected JSON object")
    return payload


def main() -> None:
    fence_open = "```json"
    raw = (
        "Here is the tool call:\n"
        + fence_open
        + '\n{"tool": "search", "query": "error logs"}\n'
        + "```\n"
    )
    print(loads_maybe_fenced(raw))


if __name__ == "__main__":
    main()
