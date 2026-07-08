from models import Todo
from typing import Sequence
import asyncio
from dao import TodoDao
from pool_config import AsyncSessionLocal

async def main():
    todo_dao: TodoDao = TodoDao(AsyncSessionLocal)
    todos: Sequence[Todo] = await todo_dao.select_todos()
    for t in todos:
        print("=====")
        print(f"{t.id} | {t.content} | {t.created_at}")

if __name__ == "__main__":
    asyncio.run(main())
