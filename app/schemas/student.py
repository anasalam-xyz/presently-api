from sqlmodel import SQLModel
from datetime import date

from app.models.student import StudentBase


class StudentCreate(StudentBase):
    password: str


class StudentRead(StudentBase):
    id: int


class StudentUpdate(SQLModel):
    email: str | None = None
    password: str | None = None
    name: str | None = None
    roll: int | None = None
    semester: int | None = None
    dob: date | None = None
