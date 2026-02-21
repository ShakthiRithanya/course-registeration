from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship

class User(SQLModel, table=True):
    id: str = Field(primary_key=True)
    role: str # student, faculty, admin
    name: str
    email: str
    password_hash: str
    photo_url: Optional[str] = None
    dept: str
    year: Optional[str] = None # UG-1, PG-2
    designation: Optional[str] = None # Prof, Head
    
    # Relationships
    enrollments: List["Enrollment"] = Relationship(
        back_populates="student",
        sa_relationship_kwargs={"foreign_keys": "[Enrollment.student_id]"}
    )
    taught_courses: List["FacultyCourse"] = Relationship(back_populates="faculty")

class Degree(SQLModel, table=True):
    id: str = Field(primary_key=True)
    type: str # UG, PG
    name: str # B.Tech CSE, M.Tech AI

class Course(SQLModel, table=True):
    id: str = Field(primary_key=True)
    degree_id: str = Field(foreign_key="degree.id")
    name: str
    credits: int
    max_enroll: int = 30
    year: int
    sem: int
    
    # Relationships
    enrollments: List["Enrollment"] = Relationship(back_populates="course")
    faculties: List["FacultyCourse"] = Relationship(back_populates="course")

class FacultyCourse(SQLModel, table=True):
    faculty_id: str = Field(foreign_key="user.id", primary_key=True)
    course_id: str = Field(foreign_key="course.id", primary_key=True)
    
    faculty: User = Relationship(back_populates="taught_courses")
    course: Course = Relationship(back_populates="faculties")

class Enrollment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    student_id: str = Field(foreign_key="user.id")
    course_id: str = Field(foreign_key="course.id")
    faculty_id: str = Field(foreign_key="user.id")
    sem: int
    status: str # enrolled, backlog, completed
    grade: Optional[float] = None # 4.0(A) - 0.0(F)

    student: User = Relationship(
        back_populates="enrollments",
        sa_relationship_kwargs={"foreign_keys": "[Enrollment.student_id]"}
    )
    course: Course = Relationship(back_populates="enrollments")
    faculty: User = Relationship(
        sa_relationship_kwargs={"foreign_keys": "[Enrollment.faculty_id]"}
    )

# User: id, name, email, hashed_password, role
