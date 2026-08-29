from sqlmodel import SQLModel, Field


class CourseBase(SQLModel):
    teacher_id: int = Field(foreign_key="teacher.id", index=True)
    title: str
    desc: str
    subject: str = Field(index=True)
    semester: int


class Course(CourseBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
