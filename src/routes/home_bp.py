from dao import TodoDao
from quart import Blueprint, render_template, current_app

home_bp = Blueprint('home', __name__)

@home_bp.get('/')
async def home():
    todo_dao: TodoDao = current_app.config['TODO_DAO']
    todos = await todo_dao.select_todos()
    return await render_template('index.html', todos=todos)
