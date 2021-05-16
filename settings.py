from utils import getenv

APP_HOST = getenv(str, 'APP_HOST', '0.0.0.0')
APP_PORT = getenv(int, 'APP_PORT', 8000)
APP_RELOAD = getenv(bool, 'APP_RELOAD', False)

MONGO_HOST = getenv(str, 'MONGO_HOST')
MONGO_PORT = getenv(int, 'MONGO_PORT')
MONGO_DB = getenv(str, 'MONGO_DB')
