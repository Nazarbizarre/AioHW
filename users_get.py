import aiohttp
import asyncio

async def getusers():
    needed_users = []
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get('https://jsonplaceholder.typicode.com/users') as response:
                if response.status == 200:
                    users = await response.json()
                    for user in users:
                        needed_users.append({"id": user.get("id"), "name": user.get("name")})
    except aiohttp.ClientError as e:
        print(f"An error occurred: {e}")
    return needed_users
