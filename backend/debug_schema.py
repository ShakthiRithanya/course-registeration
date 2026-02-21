from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship, create_engine, Session, select
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(SQLModel, table=True):
    id: str = Field(primary_key=True)
    role: str 
    name: str
    email: str
    password_hash: str
    photo_url: Optional[str] = None
    dept: str
    year: Optional[str] = None
    designation: Optional[str] = None
    
    enrollments: List["Enrollment"] = Relationship(
        back_populates="student",
        sa_relationship_kwargs={"foreign_keys": "[Enrollment.student_id]"}
    )
    taught_courses: List["FacultyCourse"] = Relationship(back_populates="faculty")

class Degree(SQLModel, table=True):
    id: str = Field(primary_key=True)
    type: str 
    name: str 

class Course(SQLModel, table=True):
    id: str = Field(primary_key=True)
    degree_id: str = Field(foreign_key="degree.id")
    name: str
    credits: int
    max_enroll: int = 30
    year: int
    sem: int
    
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
    status: str 
    grade: Optional[float] = None 

    student: User = Relationship(
        back_populates="enrollments",
        sa_relationship_kwargs={"foreign_keys": "[Enrollment.student_id]"}
    )
    course: Course = Relationship(back_populates="enrollments")

sqlite_url = "sqlite:///./test.db"
engine = create_engine(sqlite_url)

if __name__ == "__main__":
    SQLModel.metadata.create_all(engine)
    print("Success!")
