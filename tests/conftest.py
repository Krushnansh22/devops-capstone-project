"""
Pytest configuration: point the service at a local SQLite database before the
service package is imported.
"""
import os
import pathlib

TEST_DB = pathlib.Path(__file__).parent / "test_accounts.db"
os.environ.setdefault("DATABASE_URI", f"sqlite:///{TEST_DB}")
os.environ.setdefault("TESTING", "true")
os.environ.setdefault("SECRET_KEY", "test-secret")

if TEST_DB.exists():
    TEST_DB.unlink()
