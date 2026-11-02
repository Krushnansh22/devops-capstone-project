"""
Account Service

This microservice handles the lifecycle of Accounts.
"""
from flask import jsonify, request, make_response, abort, url_for

from service.models import Account, DataValidationError
from service.common import status  # HTTP Status Codes
from . import app  # Import Flask application


############################################################
# Health Endpoint
############################################################
@app.route("/health")
def health():
    """Health Status"""
    return jsonify(dict(status="OK")), status.HTTP_200_OK


######################################################################
# GET INDEX
######################################################################
@app.route("/")
def index():
    """Root URL response"""
    return (
        jsonify(
            name="Account REST API Service",
            version="1.0",
            paths=url_for("list_accounts", _external=True),
        ),
        status.HTTP_200_OK,
    )


######################################################################
# CREATE A NEW ACCOUNT
######################################################################
@app.route("/accounts", methods=["POST"])
def create_accounts():
    """
    Creates an Account
    This endpoint will create an Account based on the data in the body
    that is posted.
    """
    app.logger.info("Request to create an Account")
    check_content_type("application/json")

    account = Account()
    try:
        account.deserialize(request.get_json())
    except DataValidationError as error:
        abort(status.HTTP_400_BAD_REQUEST, str(error))

    account.create()
    message = account.serialize()
    location_url = url_for("get_accounts", account_id=account.id, _external=True)
    return make_response(
        jsonify(message), status.HTTP_201_CREATED, {"Location": location_url}
    )


######################################################################
# LIST ALL ACCOUNTS
######################################################################
@app.route("/accounts", methods=["GET"])
def list_accounts():
    """List all Accounts"""
    app.logger.info("Request to list all Accounts")
    accounts = Account.all()
    results = [account.serialize() for account in accounts]
    app.logger.info("Returning %d accounts", len(results))
    return jsonify(results), status.HTTP_200_OK


######################################################################
# READ AN ACCOUNT
######################################################################
@app.route("/accounts/<int:account_id>", methods=["GET"])
def get_accounts(account_id):
    """Read an Account"""
    app.logger.info("Request to read Account with id: %s", account_id)
    account = Account.find(account_id)
    if not account:
        abort(
            status.HTTP_404_NOT_FOUND,
            f"Account with id '{account_id}' was not found.",
        )
    return jsonify(account.serialize()), status.HTTP_200_OK


######################################################################
# UPDATE AN EXISTING ACCOUNT
######################################################################
@app.route("/accounts/<int:account_id>", methods=["PUT"])
def update_accounts(account_id):
    """Update an Account"""
    app.logger.info("Request to update Account with id: %s", account_id)
    check_content_type("application/json")

    account = Account.find(account_id)
    if not account:
        abort(
            status.HTTP_404_NOT_FOUND,
            f"Account with id '{account_id}' was not found.",
        )

    try:
        account.deserialize(request.get_json())
    except DataValidationError as error:
        abort(status.HTTP_400_BAD_REQUEST, str(error))

    account.update()
    return jsonify(account.serialize()), status.HTTP_200_OK


######################################################################
# DELETE AN ACCOUNT
######################################################################
@app.route("/accounts/<int:account_id>", methods=["DELETE"])
def delete_accounts(account_id):
    """Delete an Account"""
    app.logger.info("Request to delete Account with id: %s", account_id)
    account = Account.find(account_id)
    if not account:
        abort(
            status.HTTP_404_NOT_FOUND,
            f"Account with id '{account_id}' was not found.",
        )
    account.delete()
    return "", status.HTTP_204_NO_CONTENT


######################################################################
#  U T I L I T Y   F U N C T I O N S
######################################################################
def check_content_type(media_type):
    """Checks that the media type is correct"""
    content_type = request.headers.get("Content-Type")
    if content_type and content_type.split(";")[0].strip() == media_type:
        return
    app.logger.error("Invalid Content-Type: %s", content_type)
    abort(
        status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
        f"Content-Type must be {media_type}",
    )
