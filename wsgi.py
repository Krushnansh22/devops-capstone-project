"""
WSGI entry point for gunicorn and the Flask CLI.
"""
from service import app  # noqa: F401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
