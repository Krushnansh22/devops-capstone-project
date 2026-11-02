"""
Account API Service Test Suite
"""
from unittest import TestCase

from service import app
from service.common import status
from service.models import db, Account
from tests.factories import AccountFactory

BASE_URL = "/accounts"


class TestAccountService(TestCase):
    """Account Service Tests"""

    @classmethod
    def setUpClass(cls):
        """Run once before all tests"""
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        app.logger.setLevel("CRITICAL")
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
        self.client = app.test_client()

    def tearDown(self):
        """Runs after each test"""
        db.session.remove()

    def _create_accounts(self, count):
        """Factory method to create accounts in bulk"""
        accounts = []
        for _ in range(count):
            account = AccountFactory()
            response = self.client.post(BASE_URL, json=account.serialize())
            self.assertEqual(
                response.status_code,
                status.HTTP_201_CREATED,
                "Could not create test Account",
            )
            accounts.append(response.get_json())
        return accounts

    # ------------------------------------------------------------------
    # Health and index
    # ------------------------------------------------------------------
    def test_health(self):
        """It should return a healthy status"""
        response = self.client.get("/health")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.get_json()["status"], "OK")

    def test_index(self):
        """It should return the service name and version"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.get_json()
        self.assertEqual(data["name"], "Account REST API Service")
        self.assertEqual(data["version"], "1.0")

    # ------------------------------------------------------------------
    # Create
    # ------------------------------------------------------------------
    def test_create_account(self):
        """It should create a new Account"""
        account = AccountFactory()
        response = self.client.post(BASE_URL, json=account.serialize())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data = response.get_json()
        self.assertIsNotNone(data["id"])
        self.assertEqual(data["name"], account.name)
        self.assertIn("Location", response.headers)

    def test_create_account_no_content_type(self):
        """It should reject a create without a JSON content type"""
        response = self.client.post(BASE_URL, data="name=John")
        self.assertEqual(
            response.status_code, status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
        )

    def test_create_account_bad_data(self):
        """It should reject a create with missing fields"""
        response = self.client.post(BASE_URL, json={"name": "John Doe"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # ------------------------------------------------------------------
    # List
    # ------------------------------------------------------------------
    def test_list_accounts(self):
        """It should list all Accounts"""
        self._create_accounts(5)
        response = self.client.get(BASE_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.get_json()), 5)

    def test_list_empty(self):
        """It should return an empty list when there are no Accounts"""
        response = self.client.get(BASE_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.get_json(), [])

    # ------------------------------------------------------------------
    # Read
    # ------------------------------------------------------------------
    def test_get_account(self):
        """It should read a single Account"""
        created = self._create_accounts(1)[0]
        response = self.client.get(f"{BASE_URL}/{created['id']}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.get_json()["id"], created["id"])

    def test_get_account_not_found(self):
        """It should return 404 for a missing Account"""
        response = self.client.get(f"{BASE_URL}/9999")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # ------------------------------------------------------------------
    # Update
    # ------------------------------------------------------------------
    def test_update_account(self):
        """It should update an existing Account"""
        created = self._create_accounts(1)[0]
        created["address"] = "999 Updated St."
        created["phone_number"] = "555-1111"
        response = self.client.put(f"{BASE_URL}/{created['id']}", json=created)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.get_json()["address"], "999 Updated St.")
        self.assertEqual(response.get_json()["phone_number"], "555-1111")

    def test_update_account_not_found(self):
        """It should return 404 when updating a missing Account"""
        response = self.client.put(
            f"{BASE_URL}/9999",
            json={
                "name": "John Doe",
                "email": "john@doe.com",
                "address": "123 Main St.",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_account_no_content_type(self):
        """It should reject an update without a JSON content type"""
        created = self._create_accounts(1)[0]
        response = self.client.put(f"{BASE_URL}/{created['id']}", data="x")
        self.assertEqual(
            response.status_code, status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
        )

    # ------------------------------------------------------------------
    # Delete
    # ------------------------------------------------------------------
    def test_delete_account(self):
        """It should delete an Account"""
        created = self._create_accounts(1)[0]
        response = self.client.delete(f"{BASE_URL}/{created['id']}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(self.client.get(f"{BASE_URL}/{created['id']}").status_code, 404)

    def test_delete_account_not_found(self):
        """It should return 404 when deleting a missing Account"""
        response = self.client.delete(f"{BASE_URL}/9999")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # ------------------------------------------------------------------
    # Security headers
    # ------------------------------------------------------------------
    def test_security_headers(self):
        """It should return secure headers and a CORS policy"""
        response = self.client.get("/health")
        self.assertEqual(response.headers.get("X-Content-Type-Options"), "nosniff")
        self.assertEqual(response.headers.get("X-Frame-Options"), "SAMEORIGIN")
        self.assertIsNotNone(response.headers.get("Content-Security-Policy"))
        self.assertEqual(response.headers.get("Access-Control-Allow-Origin"), "*")
