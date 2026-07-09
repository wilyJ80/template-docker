from typing import Sequence
from sqlalchemy import select
from models import Todo
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession


class TodoDao:
    def __init__(self, session: async_sessionmaker[AsyncSession]):
        self.session: async_sessionmaker[AsyncSession] = session

    async def insert_todo(self, content: str):
        async with self.session() as session:
            async with session.begin():
                new_todo = Todo(content=content)
                session.add(new_todo)

    async def select_todos(self) -> Sequence[Todo]:
        async with self.session() as session:
            stmt = select(Todo).order_by(Todo.created_at.desc())
            result = await session.scalars(stmt)
            todos = result.all()

            return todos
