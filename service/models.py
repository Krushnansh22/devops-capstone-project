"""
Models for Account

All of the models are stored in this module.
"""
import logging
from datetime import date

from flask_sqlalchemy import SQLAlchemy

logger = logging.getLogger("flask.app")

# Create the SQLAlchemy object to be initialized later in init_db()
db = SQLAlchemy()


class DataValidationError(Exception):
    """Used for data validation errors when deserializing"""


def init_db(app):
    """Initialize the SQLAlchemy app"""
    Account.init_db(app)


######################################################################
#  P E R S I S T E N T   B A S E   M O D E L
######################################################################
class PersistentBase:
    """Base class added persistent methods"""

    def __init__(self):
        self.id = None  # pylint: disable=invalid-name

    def create(self):
        """Creates an Account in the database"""
        logger.info("Creating %s", self.name)
        self.id = None  # id must be none to generate next primary key
        db.session.add(self)
        db.session.commit()

    def update(self):
        """Updates an Account in the database"""
        logger.info("Updating %s", self.name)
        if not self.id:
            raise DataValidationError("Update called with empty ID field")
        db.session.commit()

    def delete(self):
        """Removes an Account from the data store"""
        logger.info("Deleting %s", self.name)
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def init_db(cls, app):
        """Initializes the database session"""
        logger.info("Initializing database")
        cls.app = app
        # This is where we initialize SQLAlchemy from the Flask app
        db.init_app(app)
        app.app_context().push()
        db.create_all()  # make our sqlalchemy tables

    @classmethod
    def all(cls):
        """Returns all of the records in the database"""
        logger.info("Processing all records")
        return cls.query.all()

    @classmethod
    def find(cls, by_id):
        """Finds a record by its ID"""
        logger.info("Processing lookup for id %s ...", by_id)
        return db.session.get(cls, by_id)


######################################################################
#  A C C O U N T   M O D E L
######################################################################
class Account(db.Model, PersistentBase):
    """
    Class that represents an Account
    """

    app = None

    # Table Schema
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    address = db.Column(db.String(256), nullable=False)
    phone_number = db.Column(db.String(32), nullable=True)
    date_joined = db.Column(db.Date(), nullable=False, default=date.today)

    def __repr__(self):
        return f"<Account {self.name} id=[{self.id}]>"

    def serialize(self):
        """Serializes an Account into a dictionary"""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "address": self.address,
            "phone_number": self.phone_number,
            "date_joined": self.date_joined.isoformat() if self.date_joined else None,
        }

    def deserialize(self, data):
        """
        Deserializes an Account from a dictionary

        Args:
            data (dict): A dictionary containing the resource data
        """
        if not isinstance(data, dict):
            raise DataValidationError(
                "Invalid Account: body of request contained bad or no data"
            )

        try:
            self.name = self._validate_string(data, "name", 64)
            self.email = self._validate_string(data, "email", 64)
            self.address = self._validate_string(data, "address", 256)
            self.phone_number = data.get("phone_number")
            if self.phone_number is not None:
                if not isinstance(self.phone_number, str):
                    raise DataValidationError("Invalid Account: phone_number must be a string")
                if len(self.phone_number) > 32:
                    raise DataValidationError("Invalid Account: phone_number is too long")

            date_joined = data.get("date_joined")
            if date_joined:
                self.date_joined = date.fromisoformat(date_joined)
            else:
                self.date_joined = date.today()
        except KeyError as error:
            raise DataValidationError("Invalid Account: missing " + error.args[0]) from error
        except (TypeError, ValueError) as error:
            raise DataValidationError(
                "Invalid Account: body of request contained bad or no data - "
                + str(error)
            ) from error

        return self

    @staticmethod
    def _validate_string(data, field, max_length):
        """Return a required, non-empty, length-checked string field"""
        value = data[field]
        if not isinstance(value, str):
            raise DataValidationError(f"Invalid Account: {field} must be a string")
        value = value.strip()
        if not value:
            raise DataValidationError(f"Invalid Account: {field} must not be empty")
        if len(value) > max_length:
            raise DataValidationError(
                f"Invalid Account: {field} must be {max_length} characters or less"
            )
        return value

    @classmethod
    def find_by_name(cls, name):
        """Returns all Accounts with the given name

        Args:
            name (string): the name of the Accounts you want to match
        """
        logger.info("Processing name query for %s ...", name)
        return cls.query.filter(cls.name == name)
