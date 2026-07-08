import asyncio
from dao import TodoDao
from pool_config import AsyncSessionLocal, async_engine


async def main():
    print("[INFO] Seeding DB...")

    todo_dao: TodoDao = TodoDao(AsyncSessionLocal)
    await todo_dao.insert_todo("Buy groceries")
    await todo_dao.insert_todo("Go to gym")
    await todo_dao.insert_todo("Sleep")

    print("[INFO] Seeded DB.")

    await async_engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())
