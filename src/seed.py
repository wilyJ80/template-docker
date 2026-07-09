from app import create_app
from quart import Quart
import asyncio
from dao import TodoDao


async def main():
    print("[INFO] Seeding DB...")

    app: Quart = create_app()
    todo_dao: TodoDao = TodoDao(app.config["POOL"])
    await todo_dao.insert_todo("Buy groceries")
    await todo_dao.insert_todo("Go to gym")
    await todo_dao.insert_todo("Sleep")

    print("[INFO] Seeded DB.")

    await app.config["ENGINE"].dispose()


if __name__ == "__main__":
    asyncio.run(main())
