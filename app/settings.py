from app.utils import getenv

MONGO_HOST = getenv(str, 'MONGO_HOST')
MONGO_PORT = getenv(int, 'MONGO_PORT')
MONGO_DB = getenv(str, 'MONGO_DB')
