from sqlmodel import SQLModel, Field


class CourseBase(SQLModel):
    title: str
    desc: str
    subject: str
    semester: int


class Course(CourseBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    teacher_id: int = Field(foreign_key="teacher.id")
