from sqlmodel import SQLModel, Field
from datetime import datetime, timezone


class Attendance(SQLModel, table=True):
    student_id: int = Field(foreign_key="student.id", primary_key=True)
    session_id: int = Field(foreign_key="session.id", primary_key=True, index=True)
    latitude: float
    longitude: float
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
