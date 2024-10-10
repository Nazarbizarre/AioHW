from db import MetaData, users, add_users, show_users, ids, delete_users, async_main, engine, add_json, show_spec_users
from users_get import getusers
import asyncio


json_data_loaded = False


async def add(u_id: int, u_name: str):
    if u_id not in ids:
        await add_users(id=u_id, name=u_name)
        ids.append(u_id)
        print(f"User {u_name} with ID {u_id} added successfully!")
    else:
        print(f"User with ID {u_id} already exists.")


async def delete(u_id: int):
    if u_id in ids:
        await delete_users(u_id)
        ids.remove(u_id)
        print(f"User with ID {u_id} deleted successfully!")
    else:
        print(f"User with ID {u_id} not found in the database.")


async def main():

    global json_data_loaded
    await async_main()
    
    if not json_data_loaded:
        await add_json()
        json_data_loaded = True
        print(json_data_loaded)
        
    w_type = input("Choose operation: 'show', 'show_all', 'add', or 'delete': ").lower()

    if w_type == "show_all":
        users = await show_users()
        if users:
            for user in users:
                print(f"ID: {user.id}, Name: {user.name}")
        else:
            print("No users found.")
    elif w_type == "show":
        u_id = int(input("Enter ID: "))
        user = await show_spec_users(u_id)
        if user:
            print(f"ID: {user.id}, Name: {user.name}")
        else:
            print(f"User with ID {u_id} not found.")
    elif w_type == "add":
        u_id = int(input("Enter ID: "))
        u_name = input("Enter Name: ")
        await add(u_id=u_id, u_name=u_name)
    elif w_type == "delete":
        u_id = int(input("Enter ID: "))
        await delete(u_id=u_id)
    else:
        print("Invalid operation type selected.")



if __name__ == "__main__":
    asyncio.run(main())
