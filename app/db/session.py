from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.core.config import settings

engine = create_async_engine(settings.DB_URL, echo=settings.DEBUG)
AsyncSessinLocal = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


async def get_session():
    async with AsyncSessinLocal() as session:
        yield session
