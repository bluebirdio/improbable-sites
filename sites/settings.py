from os import environ

LISTEN_HOST = environ.get("LISTEN_HOST", "0.0.0.0")
LISTEN_PORT = environ.get("LISTEN_PORT", 8000)

DATABASE_URL = environ.get("DATABASE_URL", "sqlite://")

if DATABASE_URL[:6] == "sqlite":
    default_arguments = {"check_same_thread": False}
else:
    default_arguments = {}

DATABASE_ARGS = environ.get("DATABASE_ARGS", default_arguments)
