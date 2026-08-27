from sqlmodel import SQLModel
from datetime import date

from app.models.teacher import TeacherBase


class TeacherCreate(TeacherBase):
    password: str


class TeacherRead(TeacherBase):
    id: int


class TeacherUpdate(SQLModel):
    email: str | None = None
    password: str | None = None
    name: str | None = None
    department: str | None = None
    dob: date | None = None
