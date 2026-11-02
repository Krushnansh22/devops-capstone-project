"""
Flask CLI Command Tests
"""
from unittest import TestCase

from click.testing import CliRunner

from service import app
from service.models import db, Account


class TestFlaskCLI(TestCase):
    """Test Flask CLI Commands"""

    @classmethod
    def setUpClass(cls):
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        db.session.remove()
        db.drop_all()

    def setUp(self):
        self.runner = CliRunner()
        db.session.query(Account).delete()
        db.session.commit()

    def test_db_create(self):
        """It should call the db-create command"""
        result = self.runner.invoke(app.cli, ["db-create"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Database recreated", result.output)

    def test_seed_db(self):
        """It should seed the database with sample accounts"""
        result = self.runner.invoke(app.cli, ["db-create"])
        self.assertEqual(result.exit_code, 0, result.output)

        result = self.runner.invoke(app.cli, ["seed-db"])
        self.assertEqual(result.exit_code, 0, result.output)
        self.assertEqual(Account.query.count(), 3)

    def test_seed_db_is_idempotent_per_run(self):
        """It should add exactly three accounts per seed run"""
        self.runner.invoke(app.cli, ["db-create"])
        self.runner.invoke(app.cli, ["seed-db"])
        self.runner.invoke(app.cli, ["seed-db"])
        self.assertEqual(Account.query.count(), 6)
