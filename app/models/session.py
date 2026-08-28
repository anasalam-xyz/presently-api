from sqlmodel import SQLModel, Field
from datetime import datetime


class SessionBase(SQLModel):
    course_id: int = Field(foreign_key="course.id")
    unique_code: str
    expire_at: datetime
    latitude: float
    longitude: float
    start_time: datetime


class Session(SessionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
