"""UTC ISO string -> localized wall clock."""

from __future__ import annotations

from datetime import datetime
from zoneinfo import ZoneInfo


def main() -> None:
    utc = datetime.fromisoformat("2026-05-11T18:30:00+00:00")
    lon = utc.astimezone(ZoneInfo("Europe/London"))
    ny = utc.astimezone(ZoneInfo("America/New_York"))
    print("utc:", utc)
    print("Europe/London:", lon)
    print("America/New_York:", ny)


if __name__ == "__main__":
    main()
