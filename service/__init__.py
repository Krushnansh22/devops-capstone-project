"""
Package: service

Creates and configures the Flask application, sets up logging, security
headers, CORS, and the SQL database.
"""
import os
import sys

from flask import Flask
from flask_cors import CORS
from flask_talisman import Talisman

from service import config
from service.common import log_handlers

# Create Flask application
app = Flask(__name__)
app.config.from_object(config)

# ---------------------------------------------------------------------------
# Security: secure headers + CORS (Sprint 2 "Add Security" story)
# ---------------------------------------------------------------------------
FORCE_HTTPS = os.getenv("FORCE_HTTPS", "false").lower() == "true"

talisman = Talisman(
    app,
    force_https=FORCE_HTTPS,
    force_https_permanent=False,
    frame_options="SAMEORIGIN",
    content_security_policy={
        "default-src": "'self'",
        "script-src": "'self'",
        "style-src": "'self'",
        "img-src": "'self' data:",
    },
    content_security_policy_nonce_in=None,
    strict_transport_security=FORCE_HTTPS,
    session_cookie_secure=FORCE_HTTPS,
)

CORS(
    app,
    resources={r"/*": {"origins": os.getenv("CORS_ORIGINS", "*")}},
    supports_credentials=False,
    expose_headers=["X-Request-Id"],
)

# Import the routes after the Flask app is created
# pylint: disable=wrong-import-position, cyclic-import, wrong-import-order
from service import routes, models  # noqa: F401 E402

# pylint: disable=wrong-import-position
from service.common import error_handlers, cli_commands  # noqa: F401 E402

# Set up logging for production
if not app.config.get("TESTING"):
    log_handlers.init_logging(app, "gunicorn.error")

app.logger.info(70 * "*")
app.logger.info("  A C C O U N T   S E R V I C E   R U N N I N G  ".center(70, "*"))
app.logger.info(70 * "*")

try:
    models.init_db(app)  # make our database tables
except Exception as error:  # pylint: disable=broad-except
    app.logger.critical("%s: Cannot continue", error)
    # gunicorn requires exit code 4 to stop spawning workers when they die
    sys.exit(4)

app.logger.info("Service initialized!")
