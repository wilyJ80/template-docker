from dao import TodoDao
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from settings import Settings
from quart import Quart

def create_app():
    app = Quart(__name__)

    # TODO: conftest
    
    settings: Settings = Settings()
    app.config['SETTINGS'] = settings
    app.url_map.strict_slashes = False

    # Postgres

    async_engine = create_async_engine(settings.DB_URL())
    AsyncSessionLocal = async_sessionmaker(
        bind=async_engine, class_=AsyncSession, expire_on_commit=False
    )
    app.config['POOL'] = AsyncSessionLocal

    # Services
    app.config['TODO_DAO'] = TodoDao(AsyncSessionLocal)

    @app.before_serving
    async def startup():
        async with async_engine.connect() as conn:
            await conn.exec_driver_sql("SELECT 1")

    @app.after_serving
    async def shutdown():
        await async_engine.dispose()

    # Blueprints
    
    from routes.home_bp import home_bp
    app.register_blueprint(home_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()
