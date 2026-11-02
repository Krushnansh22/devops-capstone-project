"""
Flask CLI Command Extensions
"""
from datetime import date

from service import app
from service.models import db, Account


######################################################################
# Command to force tables to be rebuilt
# Usage:
#   flask db-create
######################################################################
@app.cli.command("db-create")
def db_create():
    """
    Recreates a local database. You probably should not use this on
    production. ;-)
    """
    db.drop_all()
    db.create_all()
    db.session.commit()
    print("Database recreated.")


######################################################################
# Command to seed the database with sample accounts
# Usage:
#   flask seed-db
######################################################################
@app.cli.command("seed-db")
def seed_db():
    """Seeds the database with sample accounts"""
    samples = [
        {
            "name": "John Doe",
            "email": "john@doe.com",
            "address": "123 Main St.",
            "phone_number": "555-1212",
        },
        {
            "name": "Jane Smith",
            "email": "jane@smith.com",
            "address": "456 Oak Ave.",
            "phone_number": "555-3434",
        },
        {
            "name": "Ravi Kumar",
            "email": "ravi@kumar.com",
            "address": "789 Pine Rd.",
            "phone_number": "555-5656",
        },
    ]
    for sample in samples:
        account = Account()
        account.deserialize(sample)
        account.date_joined = date.today()
        account.create()
        print(f"Created account {account.id}: {account.name}")
    print(f"Seeded {len(samples)} accounts.")
