"""LoggerAdapter adds a fake request id — preview of structured ops logs."""

from __future__ import annotations

import logging


class RidAdapter(logging.LoggerAdapter):
    def process(self, msg: str, kwargs: dict) -> tuple[str, dict]:
        rid = self.extra.get("rid", "-")
        return f"[rid={rid}] {msg}", kwargs


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    base = logging.getLogger("ingest.worker")
    log = RidAdapter(base, {"rid": "req-884"})
    log.info("batch_start docs=%s", 128)
    log.warning("retry vendor=%s attempt=%s", "east-shard", 2)


if __name__ == "__main__":
    main()
