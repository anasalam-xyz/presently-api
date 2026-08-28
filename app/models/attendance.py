from sqlmodel import SQLModel, Field
from datetime import datetime


class Attendance(SQLModel, table=True):
    student_id: int = Field(foreign_key="student.id", primary_key=True)
    session_id: int = Field(foreign_key="session.id", primary_key=True)
    latitude: float
    longitude: float
    timestamp: datetime = Field(default_factory=datetime.now)
