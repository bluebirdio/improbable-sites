from os import environ

DATABASE_URL = environ.get('DATABASE_URL')
LISTEN_HOST = environ.get('LISTEN_HOST', "0.0.0.0")
LISTEN_PORT = environ.get('LISTEN_PORT', 8000)
