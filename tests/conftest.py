import asyncio

import pytest
from httpx import AsyncClient

from app.main import app


@pytest.fixture(scope='function')
async def client():
    async with AsyncClient(app=app, base_url='http://test') as client:
        yield client


@pytest.fixture(scope='session')
def event_loop():
    return asyncio.get_event_loop()

