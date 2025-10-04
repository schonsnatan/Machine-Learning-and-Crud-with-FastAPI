from datetime import datetime
import aiohttp
import asyncio

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()    

async def main():
    ini = datetime.now()
    urls = ["https://example.com"]*10
    tasks = [fetch_url(url) for url in urls]
    responses = await asyncio.gather(*tasks)
    print(responses[:100])
    fim = datetime.now() - ini
    print(fim)

asyncio.run(main())