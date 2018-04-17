import aiohttp

import pytest


@pytest.fixture
@pytest.mark.asyncio
async def protocol_1_2():
    async with aiohttp.ClientSession() as session:
        async with session.get('') as resp:
            return await resp.json()
