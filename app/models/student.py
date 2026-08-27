from sqlmodel import SQLModel, Field
from datetime import date


class StudentBase(SQLModel):
    email: str = Field(unique=True)
    name: str
    roll: int
    semester: int
    dob: date


class Student(StudentBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    password: str
