from sqlmodel import SQLModel, Field
from datetime import datetime, timezone


class SessionBase(SQLModel):
    course_id: int = Field(foreign_key="course.id", index=True)
    unique_code: str = Field(index=True)
    latitude: float
    longitude: float
    start_time: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class Session(SessionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    expire_at: int
