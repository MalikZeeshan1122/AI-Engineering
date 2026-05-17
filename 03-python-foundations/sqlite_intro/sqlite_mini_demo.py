"""Minimal sqlite3 workflow: temp file DB + parameterized INSERT."""

from __future__ import annotations

import sqlite3
import tempfile
from pathlib import Path


def main() -> None:
    with tempfile.TemporaryDirectory() as td:
        db_path = Path(td) / "chunks.sqlite"
        conn = sqlite3.connect(db_path)
        conn.execute(
            """
            CREATE TABLE chunks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                doc_id TEXT NOT NULL,
                body TEXT NOT NULL
            )
            """
        )
        conn.execute(
            "INSERT INTO chunks(doc_id, body) VALUES (?, ?)",
            ("doc:azure", "latency spike during rollout"),
        )
        conn.execute(
            "INSERT INTO chunks(doc_id, body) VALUES (?, ?)",
            ("doc:aws", "healthy steady state"),
        )
        conn.commit()
        rows = conn.execute(
            "SELECT doc_id, substr(body, 1, 24) FROM chunks ORDER BY doc_id"
        ).fetchall()
        print(rows)
        conn.close()


if __name__ == "__main__":
    main()
