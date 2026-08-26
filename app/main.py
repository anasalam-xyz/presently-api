from sqlmodel import create_engine
from sqlalchemy import text
from core.config import settings

DATABASE_URL = settings.DB_URL
engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    result = conn.execute(text("SELECT 1"))
    print(result.scalar())
