import unittest
from secureutils.database import DatabaseManager
import tempfile
import os
import threading
import time

class TestDatabaseManager(unittest.TestCase):
    def setUp(self):
        self.db_file = tempfile.mktemp()
        self.db = DatabaseManager(self.db_file)

    def tearDown(self):
        self.db.close()
        if os.path.exists(self.db_file):
            os.unlink(self.db_file)

    def test_create_table(self):
        """Test table creation and verification."""
        self.db.create_table(
            "test_table",
            {
                "id": "INTEGER PRIMARY KEY",
                "name": "TEXT",
                "age": "INTEGER"
            }
        )

        # Verify table exists
        result = self.db.fetch_one(
            "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
            ('test_table',)
        )
        self.assertIsNotNone(result)
        self.assertIn('name', result)
        self.assertEqual(result['name'], 'test_table')

    def test_insert_and_fetch(self):
        """Test data insertion and retrieval."""
        self.db.create_table(
            "test_table",
            {
                "id": "INTEGER PRIMARY KEY",
                "name": "TEXT",
                "age": "INTEGER"
            }
        )

        test_data = {"name": "John Doe", "age": 30}
        self.db.insert("test_table", test_data)

        result = self.db.fetch_one(
            "SELECT name, age FROM test_table WHERE name=?",
            ("John Doe",)
        )

        self.assertIsNotNone(result)
        self.assertIn('name', result)
        self.assertIn('age', result)
        self.assertEqual(result['name'], "John Doe")
        self.assertEqual(result['age'], 30)

    def test_fetch_all(self):
        """Test fetching multiple rows."""
        self.db.create_table(
            "test_table",
            {
                "id": "INTEGER PRIMARY KEY",
                "name": "TEXT"
            }
        )

        test_data = [
            {"name": "John"},
            {"name": "Jane"},
            {"name": "Bob"}
        ]

        for data in test_data:
            self.db.insert("test_table", data)

        results = self.db.fetch_all("SELECT name FROM test_table ORDER BY name")
        self.assertEqual(len(results), 3)
        self.assertEqual(results[0]["name"], "Bob")
        self.assertEqual(results[1]["name"], "Jane")
        self.assertEqual(results[2]["name"], "John")

    def test_fetch_non_existent(self):
        """Test fetching non-existent data."""
        self.db.create_table(
            "test_table",
            {
                "id": "INTEGER PRIMARY KEY",
                "name": "TEXT"
            }
        )

        result = self.db.fetch_one(
            "SELECT * FROM test_table WHERE name=?",
            ("NonExistent",)
        )
        self.assertIsNone(result)

    def test_concurrent_access(self):
        """Test concurrent database access."""
        self.db.create_table(
            "test_table",
            {
                "id": "INTEGER PRIMARY KEY",
                "counter": "INTEGER"
            }
        )

        def worker():
            for _ in range(10):
                self.db.insert("test_table", {"counter": 1})
                time.sleep(0.01)

        threads = [threading.Thread(target=worker) for _ in range(3)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        result = self.db.fetch_one("SELECT COUNT(*) as count FROM test_table")
        self.assertIsNotNone(result)
        self.assertEqual(result['count'], 30)

if __name__ == '__main__':
    unittest.main()