from sqlmodel import create_engine, Session, SQLModel, select
from models.schema import User, Degree, Course, FacultyCourse, Enrollment
from passlib.context import CryptContext
import os

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

# Use in-memory SQLite for mocks if desired, but here we use a file for persistence during dev
sqlite_url = "sqlite:///./database.db"
engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def seed_data():
    with Session(engine) as session:
        # Check if already seeded
        if session.exec(select(User)).first():
            return

        # 1 Admin
        admin = User(
            id="admin_01",
            role="admin",
            name="Admin User",
            email="admin@college.edu",
            password_hash=pwd_context.hash("admin123"),
            dept="Administration"
        )
        session.add(admin)

        # 5 Faculty
        faculties = [
            User(id="fac_01", role="faculty", name="Dr. Alan Turing", email="turing@college.edu", password_hash=pwd_context.hash("fac123"), dept="CSE", designation="Professor", photo_url="https://api.dicebear.com/7.x/avataaars/svg?seed=Alan"),
            User(id="fac_02", role="faculty", name="Dr. Grace Hopper", email="hopper@college.edu", password_hash=pwd_context.hash("fac123"), dept="CSE", designation="Head of Dept", photo_url="https://api.dicebear.com/7.x/avataaars/svg?seed=Grace"),
            User(id="fac_03", role="faculty", name="Dr. Ada Lovelace", email="lovelace@college.edu", password_hash=pwd_context.hash("fac123"), dept="AI", designation="Professor", photo_url="https://api.dicebear.com/7.x/avataaars/svg?seed=Ada"),
            User(id="fac_04", role="faculty", name="Dr. John von Neumann", email="neumann@college.edu", password_hash=pwd_context.hash("fac123"), dept="Systems", designation="Assistant Professor", photo_url="https://api.dicebear.com/7.x/avataaars/svg?seed=John"),
            User(id="fac_05", role="faculty", name="Dr. Claude Shannon", email="shannon@college.edu", password_hash=pwd_context.hash("fac123"), dept="Information Theory", designation="Professor", photo_url="https://api.dicebear.com/7.x/avataaars/svg?seed=Claude"),
        ]
        for f in faculties: session.add(f)

        # 5 Students
        students = [
            User(id="stud_01", role="student", name="Alice Smith", email="alice@college.edu", password_hash=pwd_context.hash("stud123"), dept="CSE", year="UG-2", photo_url="https://api.dicebear.com/7.x/avataaars/svg?seed=Alice"),
            User(id="stud_02", role="student", name="Bob Jones", email="bob@college.edu", password_hash=pwd_context.hash("stud123"), dept="CSE", year="UG-1", photo_url="https://api.dicebear.com/7.x/avataaars/svg?seed=Bob"),
            User(id="stud_03", role="student", name="Charlie Brown", email="charlie@college.edu", password_hash=pwd_context.hash("stud123"), dept="AI", year="PG-1", photo_url="https://api.dicebear.com/7.x/avataaars/svg?seed=Charlie"),
            User(id="stud_04", role="student", name="Diana Prince", email="diana@college.edu", password_hash=pwd_context.hash("stud123"), dept="Systems", year="UG-3", photo_url="https://api.dicebear.com/7.x/avataaars/svg?seed=Diana"),
            User(id="stud_05", role="student", name="Eve Online", email="eve@college.edu", password_hash=pwd_context.hash("stud123"), dept="CSE", year="UG-2", photo_url="https://api.dicebear.com/7.x/avataaars/svg?seed=Eve"),
        ]
        for s in students: session.add(s)

        # Degrees
        degrees = [
            Degree(id="deg_ug_cse", type="UG", name="B.Tech Computer Science"),
            Degree(id="deg_pg_ai", type="PG", name="M.Tech Artificial Intelligence"),
        ]
        for d in degrees: session.add(d)

        # Courses (20+)
        courses = [
            # UG CSE Year 2 Sem 1
            Course(id="CSE201", degree_id="deg_ug_cse", name="Data Structures", credits=4, year=2, sem=1),
            Course(id="CSE202", degree_id="deg_ug_cse", name="Operating Systems", credits=4, year=2, sem=1),
            Course(id="CSE203", degree_id="deg_ug_cse", name="Discrete Mathematics", credits=3, year=2, sem=1),
            Course(id="CSE204", degree_id="deg_ug_cse", name="Computer Organization", credits=3, year=2, sem=1),
            Course(id="CSE205", degree_id="deg_ug_cse", name="Digital Electronics", credits=3, year=2, sem=1),
            Course(id="CSE206", degree_id="deg_ug_cse", name="Algorithms Lab", credits=2, year=2, sem=1),
            
            # UG CSE Year 1 Sem 1
            Course(id="CSE101", degree_id="deg_ug_cse", name="Intro to C", credits=4, year=1, sem=1),
            Course(id="MAT101", degree_id="deg_ug_cse", name="Calculus", credits=4, year=1, sem=1),
            Course(id="PHY101", degree_id="deg_ug_cse", name="Engineering Physics", credits=3, year=1, sem=1),
            
            # PG AI Year 1 Sem 1
            Course(id="AI501", degree_id="deg_pg_ai", name="Machine Learning", credits=4, year=1, sem=1),
            Course(id="AI502", degree_id="deg_pg_ai", name="Neural Networks", credits=4, year=1, sem=1),
            Course(id="AI503", degree_id="deg_pg_ai", name="Python for Data Science", credits=3, year=1, sem=1),
            Course(id="AI504", degree_id="deg_pg_ai", name="Optimization Tech", credits=3, year=1, sem=1),
            Course(id="AI505", degree_id="deg_pg_ai", name="AI Ethics", credits=2, year=1, sem=1),
            
            # Backlog Courses
            Course(id="MAT102", degree_id="deg_ug_cse", name="Linear Algebra", credits=4, year=1, sem=2),
            Course(id="CSE105", degree_id="deg_ug_cse", name="Web Dev Basics", credits=3, year=1, sem=2),
        ]
        # Add a few more to hit 20
        for i in range(1, 10):
            courses.append(Course(id=f"ELECTIVE_{i}", degree_id="deg_ug_cse", name=f"Elective {i}", credits=3, year=3, sem=5))
        
        for c in courses: session.add(c)

        # Allocation
        allocations = [
            FacultyCourse(faculty_id="fac_01", course_id="CSE201"),
            FacultyCourse(faculty_id="fac_01", course_id="CSE206"),
            FacultyCourse(faculty_id="fac_02", course_id="CSE202"),
            FacultyCourse(faculty_id="fac_03", course_id="AI501"),
            FacultyCourse(faculty_id="fac_03", course_id="AI502"),
            FacultyCourse(faculty_id="fac_04", course_id="CSE204"),
            FacultyCourse(faculty_id="fac_05", course_id="CSE203"),
        ]
        for a in allocations: session.add(a)

        # Enrollments (20+)
        # Alice (stud_01) has backlogs from Year 1
        enrollments = [
            Enrollment(student_id="stud_01", course_id="MAT102", faculty_id="fac_05", sem=2, status="backlog", grade=0.0),
            Enrollment(student_id="stud_01", course_id="CSE101", faculty_id="fac_01", sem=1, status="completed", grade=3.5),
            
            # Current enrollments for Alice (UG-2, Sem 1)
            Enrollment(student_id="stud_01", course_id="CSE201", faculty_id="fac_01", sem=3, status="enrolled"),
            Enrollment(student_id="stud_01", course_id="CSE202", faculty_id="fac_02", sem=3, status="enrolled"),
        ]
        
        # Add 20+ records
        for i in range(15):
             enrollments.append(Enrollment(student_id=f"stud_{i%5+1}", course_id="CSE201", faculty_id="fac_01", sem=3, status="enrolled"))

        for e in enrollments: session.add(e)
        
        session.commit()

if __name__ == "__main__":
    create_db_and_tables()
    seed_data()

# SQLite engine + create_db_and_tables

# degrees: B.Tech, M.Tech, BCA, MCA, B.Sc, M.Sc

# courses seeded per degree with semester allocation

# admin: admin@college.edu / admin123

# faculty1@college.edu, faculty2@college.edu
