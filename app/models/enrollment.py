from sqlmodel import SQLModel, Field


class Enrollment(SQLModel, table=True):
    course_id: int = Field(foreign_key="course.id", primary_key=True)
    student_id: int = Field(foreign_key="student.id", primary_key=True)
