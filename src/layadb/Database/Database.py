import sqlite3
from typing import Any, Dict, Optional, List

from .Schema import Entry

class Database:
    def __init__(self, db_path: str = "Penguinone.db") -> None:
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self._create_table()

    def _create_table(self) -> None:
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS entries (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                quantity INTEGER NOT NULL
            )
        """)

        self.connection.commit()

    def add_entry(self, entry: Entry) -> bool:
        self.cursor.execute(
            "INSERT OR REPLACE INTO entries (id, name, quantity) VALUES (?, ?, ?)",
            (entry.id, entry.name, entry.quantity)
        )

        self.connection.commit()

        return True

    def get_entry(self, primary_key: str) -> Optional[Entry]:
        self.cursor.execute(
            "SELECT id, name, quantity FROM entries WHERE id = ?",
            (primary_key,)
        )

        row = self.cursor.fetchone()

        if row is None:
            return None

        return Entry(id=row[0], name=row[1], quantity=row[2])

    def remove_entry(self, primary_key: str) -> bool:
        self.cursor.execute("DELETE FROM entries WHERE id = ?", (primary_key,))
        self.connection.commit()

        return self.cursor.rowcount > 0

    def patch_entry(self, primary_key: str, patch: Dict[str, Any]) -> bool:
        fields = [f"{key} = ?" for key in patch.keys()]
        values = list(patch.values()) + [primary_key]

        self.cursor.execute(
            f"UPDATE entries SET {', '.join(fields)} WHERE id = ?",
            values
        )

        self.connection.commit()

        return self.cursor.rowcount > 0

    def list_entries(self) -> List[Entry]:
        self.cursor.execute("SELECT id, name, quantity FROM entries")

        return [Entry(id=row[0], name=row[1], quantity=row[2]) for row in self.cursor.fetchall()]

    def close(self) -> None:
        self.connection.close()
