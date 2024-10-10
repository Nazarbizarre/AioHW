
import asyncio

from sqlalchemy import Column
from sqlalchemy import MetaData
from sqlalchemy import select
from sqlalchemy import delete
from sqlalchemy import String, Integer
from sqlalchemy import Table
from sqlalchemy.ext.asyncio import create_async_engine
from users_get import getusers

ids = []
engine = None

meta = MetaData()
users = Table("users", meta, Column("name", String(50)), Column("id", Integer, primary_key=True))
engine = None

async def async_main() -> None:
    global engine
    engine = create_async_engine("sqlite+aiosqlite://", echo=True)
    async with engine.begin() as conn:
        await conn.run_sync(meta.drop_all)
        await conn.run_sync(meta.create_all)


asyncio.run(async_main())


async def add_users(u_id: int, name: str):
    
    async with engine.connect() as conn:
        await conn.execute(
            users.insert(), [{"id": u_id, "name": name}]
        )




async def add_json():
    async with engine.connect() as conn:
        needed_users = await getusers()
        for user in needed_users:
            await conn.execute(
            users.insert(), [{"id": user.get("id"), "name": user.get("name")}]
        )



async def delete_users(U_id: int):
    
    async with engine.connect() as conn:
        delete = users.delete().where(users.c.id == U_id)
        await conn.execute(delete)
    


async def show_users():
    async with engine.connect() as conn:
        all_u = await conn.execute(select(users))
        return all_u
    
async def show_spec_users(U_id:int):
    async with engine.connect() as conn:
        spec = await conn.execute(select(users).where(users.c.id == U_id))
        return spec


async def close_engine():
    await engine.dispose()
