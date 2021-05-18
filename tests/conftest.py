import asyncio

import pytest
from api.app import app
from httpx import AsyncClient


@pytest.fixture(scope='function')
async def client():
    async with AsyncClient(app=app, base_url='http://test') as client:
        yield client


@pytest.fixture(scope='session')
def event_loop():
    return asyncio.get_event_loop()
