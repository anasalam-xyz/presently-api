from sqlmodel import SQLModel, Field
from datetime import date


class TeacherBase(SQLModel):
    email: str = Field(unique=True)
    name: str
    department: str
    dob: date


class Teacher(TeacherBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    password: str
