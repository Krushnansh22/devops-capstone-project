"""
Account Model Test Suite
"""
from datetime import date
from unittest import TestCase

from service.models import Account, DataValidationError, db
from tests.factories import AccountFactory


class TestAccountModel(TestCase):
    """Account Model Tests"""

    @classmethod
    def setUpClass(cls):
        """Run once before all tests"""
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        """Run once after all tests"""
        db.session.remove()
        db.drop_all()

    def setUp(self):
        """Runs before each test"""
        db.session.query(Account).delete()
        db.session.commit()

    def tearDown(self):
        """Runs after each test"""
        db.session.remove()

    def test_create_account(self):
        """It should create an Account and add it to the database"""
        account = AccountFactory()
        account.create()
        self.assertIsNotNone(account.id)
        found = Account.find(account.id)
        self.assertEqual(found.name, account.name)

    def test_update_account(self):
        """It should update an Account in the database"""
        account = AccountFactory()
        account.create()
        account.address = "999 Updated St."
        account.update()
        found = Account.find(account.id)
        self.assertEqual(found.address, "999 Updated St.")

    def test_delete_account(self):
        """It should delete an Account from the database"""
        account = AccountFactory()
        account.create()
        account.delete()
        self.assertIsNone(Account.find(account.id))

    def test_list_all_accounts(self):
        """It should return every Account in the database"""
        for _ in range(5):
            AccountFactory().create()
        accounts = Account.all()
        self.assertEqual(len(accounts), 5)

    def test_find_by_name(self):
        """It should find Accounts by name"""
        account = AccountFactory(name="John Doe")
        account.create()
        found = Account.find_by_name("John Doe").all()
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0].id, account.id)

    def test_serialize(self):
        """It should serialize an Account into a dictionary"""
        account = AccountFactory()
        account.create()
        data = account.serialize()
        self.assertEqual(data["id"], account.id)
        self.assertEqual(data["name"], account.name)
        self.assertEqual(data["email"], account.email)
        self.assertEqual(data["address"], account.address)
        self.assertEqual(data["phone_number"], account.phone_number)
        self.assertEqual(data["date_joined"], account.date_joined.isoformat())

    def test_deserialize(self):
        """It should deserialize a dictionary into an Account"""
        data = {
            "name": "John Doe",
            "email": "john@doe.com",
            "address": "123 Main St.",
            "phone_number": "555-1212",
        }
        account = Account()
        account.deserialize(data)
        self.assertEqual(account.name, "John Doe")
        self.assertEqual(account.phone_number, "555-1212")
        self.assertEqual(account.date_joined, date.today())

    def test_deserialize_with_date(self):
        """It should accept an explicit date_joined"""
        account = Account()
        account.deserialize(
            {
                "name": "John Doe",
                "email": "john@doe.com",
                "address": "123 Main St.",
                "date_joined": "2024-01-15",
            }
        )
        self.assertEqual(account.date_joined, date(2024, 1, 15))

    def test_deserialize_missing_field(self):
        """It should raise DataValidationError when a required field is missing"""
        account = Account()
        with self.assertRaises(DataValidationError):
            account.deserialize({"name": "John Doe", "email": "john@doe.com"})

    def test_deserialize_bad_type(self):
        """It should raise DataValidationError when the body is not a dict"""
        account = Account()
        with self.assertRaises(DataValidationError):
            account.deserialize("not-a-dict")

    def test_deserialize_empty_name(self):
        """It should reject an empty name"""
        account = Account()
        with self.assertRaises(DataValidationError):
            account.deserialize(
                {"name": "   ", "email": "john@doe.com", "address": "123 Main St."}
            )

    def test_deserialize_long_name(self):
        """It should reject a name longer than the column"""
        account = Account()
        with self.assertRaises(DataValidationError):
            account.deserialize(
                {
                    "name": "x" * 65,
                    "email": "john@doe.com",
                    "address": "123 Main St.",
                }
            )

    def test_update_without_id(self):
        """It should refuse to update an Account with no id"""
        account = AccountFactory()
        account.id = None
        with self.assertRaises(DataValidationError):
            account.update()

    def test_repr(self):
        """It should have a useful repr"""
        account = AccountFactory(name="John Doe")
        account.id = 1
        self.assertIn("John Doe", repr(account))
