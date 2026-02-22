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
            Degree(id="deg_ug_csbs", type="UG", name="B.Tech Computer Science and Business Systems"),
            Degree(id="deg_ug_aids", type="UG", name="B.Tech Artificial Intelligence and Data Science"),
            Degree(id="deg_ug_aiml", type="UG", name="B.E. CSE (Artificial Intelligence and Machine Learning)"),
            Degree(id="deg_ug_cse", type="UG", name="B.E. Computer Science and Engineering"),
            Degree(id="deg_ug_it", type="UG", name="B.Tech Information Technology"),
            Degree(id="deg_ug_cys", type="UG", name="B.E. Computer Science and Engineering (Cyber Security)"),
            Degree(id="deg_ug_ece", type="UG", name="B.E. Electronics and Communication Engineering"),
            Degree(id="deg_ug_mech", type="UG", name="B.E. Mechanical Engineering"),
        ]
        for d in degrees: session.add(d)

        # Courses
        courses = [
            # CSBS - Semester 1
            Course(id="24UTA161_CSBS", degree_id="deg_ug_csbs", name="Heritage of Tamils", credits=1, year=1, sem=1),
            Course(id="24UEN171_CSBS", degree_id="deg_ug_csbs", name="Communicative English for Engineers and Professionals - I", credits=3, year=1, sem=1),
            Course(id="24UMA161_CSBS", degree_id="deg_ug_csbs", name="Calculus and Matrix Algebra", credits=4, year=1, sem=1),
            Course(id="24UPY171_CSBS", degree_id="deg_ug_csbs", name="Physics for Engineering and Technology", credits=3, year=1, sem=1),
            Course(id="24UCH171_CSBS", degree_id="deg_ug_csbs", name="Engineering Chemistry", credits=3, year=1, sem=1),
            Course(id="24UCS161_CSBS", degree_id="deg_ug_csbs", name="Computational Thinking", credits=3, year=1, sem=1),
            Course(id="24UCS171_CSBS", degree_id="deg_ug_csbs", name="Python Programming", credits=4, year=1, sem=1),
            Course(id="24UME266_CSBS", degree_id="deg_ug_csbs", name="Engineering Practices Laboratory", credits=2, year=1, sem=1),
            
            # CSBS - Semester 2
            Course(id="24UTA261_CSBS", degree_id="deg_ug_csbs", name="Tamils and Technology", credits=1, year=1, sem=2),
            Course(id="24UMA261_CSBS", degree_id="deg_ug_csbs", name="Statistics and Linear Algebra", credits=4, year=1, sem=2),
            Course(id="24UPY271_CSBS", degree_id="deg_ug_csbs", name="Physics for Data Science", credits=3, year=1, sem=2),
            Course(id="24UCS271_CSBS", degree_id="deg_ug_csbs", name="Data Structures and Algorithms", credits=4, year=1, sem=2),
            Course(id="24UCB261_CSBS", degree_id="deg_ug_csbs", name="Fundamentals of Business Systems", credits=3, year=1, sem=2),
            Course(id="24UCB271_CSBS", degree_id="deg_ug_csbs", name="Business Systems Lab", credits=2, year=1, sem=2),

            # AIDS - Semester 1
            Course(id="24UTA161_AIDS", degree_id="deg_ug_aids", name="Heritage of Tamils", credits=1, year=1, sem=1),
            Course(id="24UEN171_AIDS", degree_id="deg_ug_aids", name="Communicative English for Engineers and Professionals - I", credits=3, year=1, sem=1),
            Course(id="24UMA161_AIDS", degree_id="deg_ug_aids", name="Calculus and Matrix Algebra", credits=4, year=1, sem=1),
            Course(id="24UPY171_AIDS", degree_id="deg_ug_aids", name="Physics for Engineering and Technology", credits=3, year=1, sem=1),
            Course(id="24UCH171_AIDS", degree_id="deg_ug_aids", name="Engineering Chemistry", credits=3, year=1, sem=1),
            Course(id="24UCS161_AIDS", degree_id="deg_ug_aids", name="Computational Thinking", credits=3, year=1, sem=1),
            Course(id="24UCS171_AIDS", degree_id="deg_ug_aids", name="Python Programming", credits=4, year=1, sem=1),
            Course(id="24UME166_AIDS", degree_id="deg_ug_aids", name="Engineering Graphics", credits=2, year=1, sem=1),

            # AIDS - Semester 2
            Course(id="24UTA261_AIDS", degree_id="deg_ug_aids", name="Tamils and Technology", credits=1, year=1, sem=2),
            Course(id="24UEN271_AIDS", degree_id="deg_ug_aids", name="Communicative English for Engineers and Professionals - II", credits=3, year=1, sem=2),
            Course(id="24UMA261_AIDS", degree_id="deg_ug_aids", name="Statistics and Numerical Methods", credits=4, year=1, sem=2),
            Course(id="24UPY261_AIDS", degree_id="deg_ug_aids", name="Physics for Information Science", credits=3, year=1, sem=2),
            Course(id="24UCH261_AIDS", degree_id="deg_ug_aids", name="Environmental Sciences and Sustainability", credits=2, year=1, sem=2),
            Course(id="24UCS271_AIDS", degree_id="deg_ug_aids", name="Programming in C", credits=4, year=1, sem=2),
            Course(id="24UEC272_AIDS", degree_id="deg_ug_aids", name="Basic Electrical and Electronics Engineering", credits=3, year=1, sem=2),
            Course(id="24UME266_AIDS", degree_id="deg_ug_aids", name="Engineering Practices Laboratory", credits=2, year=1, sem=2),
            Course(id="24USD296_AIDS", degree_id="deg_ug_aids", name="Skill Development Course", credits=3, year=1, sem=2),

            # AIML - Semester 1
            Course(id="24UTA161_AIML", degree_id="deg_ug_aiml", name="Heritage of Tamils", credits=1, year=1, sem=1),
            Course(id="24UEN171_AIML", degree_id="deg_ug_aiml", name="Communicative English for Engineers and Professionals - I", credits=3, year=1, sem=1),
            Course(id="24UMA161_AIML", degree_id="deg_ug_aiml", name="Calculus and Matrix Algebra", credits=4, year=1, sem=1),
            Course(id="24UPY171_AIML", degree_id="deg_ug_aiml", name="Physics for Engineering and Technology", credits=3, year=1, sem=1),
            Course(id="24UCH171_AIML", degree_id="deg_ug_aiml", name="Engineering Chemistry", credits=3, year=1, sem=1),
            Course(id="24UCS161_AIML", degree_id="deg_ug_aiml", name="Computational Thinking", credits=3, year=1, sem=1),
            Course(id="24UCS171_AIML", degree_id="deg_ug_aiml", name="Python Programming", credits=4, year=1, sem=1),
            Course(id="24UME266_AIML", degree_id="deg_ug_aiml", name="Engineering Practices Laboratory", credits=2, year=1, sem=1),

            # AIML - Semester 2
            Course(id="24UTA261_AIML", degree_id="deg_ug_aiml", name="Tamils and Technology", credits=1, year=1, sem=2),
            Course(id="24UEN271_AIML", degree_id="deg_ug_aiml", name="Communicative English for Engineers and Professionals - II", credits=3, year=1, sem=2),
            Course(id="24UMA261_AIML", degree_id="deg_ug_aiml", name="Statistics and Numerical Methods", credits=4, year=1, sem=2),
            Course(id="24UPY261_AIML", degree_id="deg_ug_aiml", name="Physics for Information Science", credits=3, year=1, sem=2),
            Course(id="24UCH261_AIML", degree_id="deg_ug_aiml", name="Environmental Sciences and Sustainability", credits=2, year=1, sem=2),
            Course(id="24UCS271_AIML", degree_id="deg_ug_aiml", name="Programming in C", credits=4, year=1, sem=2),
            Course(id="24UEC272_AIML", degree_id="deg_ug_aiml", name="Basic Electrical and Electronics Engineering", credits=3, year=1, sem=2),
            Course(id="24UME166_AIML", degree_id="deg_ug_aiml", name="Engineering Graphics", credits=2, year=1, sem=2),
            Course(id="24USD296_AIML", degree_id="deg_ug_aiml", name="Skill Development Course", credits=3, year=1, sem=2),

            # CSE - Semester 1
            Course(id="24UTA161_CSE", degree_id="deg_ug_cse", name="Heritage of Tamils", credits=1, year=1, sem=1),
            Course(id="24UEN171_CSE", degree_id="deg_ug_cse", name="Communicative English for Engineers and Professionals - I", credits=3, year=1, sem=1),
            Course(id="24UMA161_CSE", degree_id="deg_ug_cse", name="Calculus and Matrix Algebra", credits=4, year=1, sem=1),
            Course(id="24UPY171_CSE", degree_id="deg_ug_cse", name="Physics for Engineering and Technology", credits=3, year=1, sem=1),
            Course(id="24UCH171_CSE", degree_id="deg_ug_cse", name="Engineering Chemistry", credits=3, year=1, sem=1),
            Course(id="24UCS161_CSE", degree_id="deg_ug_cse", name="Computational Thinking", credits=3, year=1, sem=1),
            Course(id="24UCS171_CSE", degree_id="deg_ug_cse", name="Python Programming", credits=4, year=1, sem=1),
            Course(id="24UME166_CSE", degree_id="deg_ug_cse", name="Engineering Graphics", credits=2, year=1, sem=1),

            # CSE - Semester 2
            Course(id="24UTA261_CSE", degree_id="deg_ug_cse", name="Tamils and Technology", credits=1, year=1, sem=2),
            Course(id="24UEN271_CSE", degree_id="deg_ug_cse", name="Communicative English for Engineers and Professionals - II", credits=3, year=1, sem=2),
            Course(id="24UMA261_CSE", degree_id="deg_ug_cse", name="Statistics and Numerical Methods", credits=4, year=1, sem=2),
            Course(id="24UPY261_CSE", degree_id="deg_ug_cse", name="Physics for Information Science", credits=3, year=1, sem=2),
            Course(id="24UCH261_CSE", degree_id="deg_ug_cse", name="Environmental Sciences and Sustainability", credits=2, year=1, sem=2),
            Course(id="24UCS271_CSE", degree_id="deg_ug_cse", name="Programming in C", credits=4, year=1, sem=2),
            Course(id="24UEC272_CSE", degree_id="deg_ug_cse", name="Basic Electrical and Electronics Engineering", credits=3, year=1, sem=2),
            Course(id="24UME266_CSE", degree_id="deg_ug_cse", name="Engineering Practices Laboratory", credits=2, year=1, sem=2),
            Course(id="24USD296_CSE", degree_id="deg_ug_cse", name="Skill Development Course", credits=3, year=1, sem=2),

            # IT - Semester 1
            Course(id="24UTA161_IT", degree_id="deg_ug_it", name="Heritage of Tamils", credits=1, year=1, sem=1),
            Course(id="24UEN171_IT", degree_id="deg_ug_it", name="Communicative English for Engineers and Professionals - I", credits=3, year=1, sem=1),
            Course(id="24UMA161_IT", degree_id="deg_ug_it", name="Calculus and Matrix Algebra", credits=4, year=1, sem=1),
            Course(id="24UPY171_IT", degree_id="deg_ug_it", name="Physics for Engineering and Technology", credits=3, year=1, sem=1),
            Course(id="24UCH171_IT", degree_id="deg_ug_it", name="Engineering Chemistry", credits=3, year=1, sem=1),
            Course(id="24UCS161_IT", degree_id="deg_ug_it", name="Computational Thinking", credits=3, year=1, sem=1),
            Course(id="24UCS171_IT", degree_id="deg_ug_it", name="Python Programming", credits=4, year=1, sem=1),
            Course(id="24UME266_IT", degree_id="deg_ug_it", name="Engineering Practices Laboratory", credits=2, year=1, sem=1),

            # IT - Semester 2
            Course(id="24UTA261_IT", degree_id="deg_ug_it", name="Tamils and Technology", credits=1, year=1, sem=2),
            Course(id="24UEN271_IT", degree_id="deg_ug_it", name="Communicative English for Engineers and Professionals - II", credits=3, year=1, sem=2),
            Course(id="24UMA261_IT", degree_id="deg_ug_it", name="Statistics and Numerical Methods", credits=4, year=1, sem=2),
            Course(id="24UPY261_IT", degree_id="deg_ug_it", name="Physics for Information Science", credits=3, year=1, sem=2),
            Course(id="24UCH261_IT", degree_id="deg_ug_it", name="Environmental Sciences and Sustainability", credits=2, year=1, sem=2),
            Course(id="24UCS271_IT", degree_id="deg_ug_it", name="Programming in C", credits=4, year=1, sem=2),
            Course(id="24UEC272_IT", degree_id="deg_ug_it", name="Basic Electrical and Electronics Engineering", credits=3, year=1, sem=2),
            Course(id="24UME166_IT", degree_id="deg_ug_it", name="Engineering Graphics", credits=2, year=1, sem=2),
            Course(id="24USD296_IT", degree_id="deg_ug_it", name="Skill Development Course", credits=3, year=1, sem=2),

            # CYS - Semester 1
            Course(id="24UTA161_CYS", degree_id="deg_ug_cys", name="Heritage of Tamils", credits=1, year=1, sem=1),
            Course(id="24UEN171_CYS", degree_id="deg_ug_cys", name="Communicative English for Engineers and Professionals - I", credits=3, year=1, sem=1),
            Course(id="24UMA161_CYS", degree_id="deg_ug_cys", name="Calculus and Matrix Algebra", credits=4, year=1, sem=1),
            Course(id="24UPY171_CYS", degree_id="deg_ug_cys", name="Physics for Engineering and Technology", credits=3, year=1, sem=1),
            Course(id="24UCH171_CYS", degree_id="deg_ug_cys", name="Engineering Chemistry", credits=3, year=1, sem=1),
            Course(id="24UCS161_CYS", degree_id="deg_ug_cys", name="Computational Thinking", credits=3, year=1, sem=1),
            Course(id="24UCS171_CYS", degree_id="deg_ug_cys", name="Python Programming", credits=4, year=1, sem=1),
            Course(id="24UME266_CYS", degree_id="deg_ug_cys", name="Engineering Practices Laboratory", credits=2, year=1, sem=1),

            # CYS - Semester 2
            Course(id="24UTA261_CYS", degree_id="deg_ug_cys", name="Tamils and Technology", credits=1, year=1, sem=2),
            Course(id="24UEN271_CYS", degree_id="deg_ug_cys", name="Communicative English for Engineers and Professionals - II", credits=3, year=1, sem=2),
            Course(id="24UMA261_CYS", degree_id="deg_ug_cys", name="Statistics and Numerical Methods", credits=4, year=1, sem=2),
            Course(id="24UPY261_CYS", degree_id="deg_ug_cys", name="Physics for Information Science", credits=3, year=1, sem=2),
            Course(id="24UCH261_CYS", degree_id="deg_ug_cys", name="Environmental Sciences and Sustainability", credits=2, year=1, sem=2),
            Course(id="24UCS271_CYS", degree_id="deg_ug_cys", name="Programming in C", credits=4, year=1, sem=2),
            Course(id="24UEC272_CYS", degree_id="deg_ug_cys", name="Basic Electrical and Electronics Engineering", credits=3, year=1, sem=2),
            Course(id="24UME166_CYS", degree_id="deg_ug_cys", name="Engineering Graphics", credits=2, year=1, sem=2),
            Course(id="24USD296_CYS", degree_id="deg_ug_cys", name="Skill Development Course", credits=3, year=1, sem=2),

            # ECE - Semester 1
            Course(id="24UTA161_ECE", degree_id="deg_ug_ece", name="Heritage of Tamils", credits=1, year=1, sem=1),
            Course(id="24UEN171_ECE", degree_id="deg_ug_ece", name="Communicative English for Engineers and Professionals - I", credits=3, year=1, sem=1),
            Course(id="24UMA162_ECE", degree_id="deg_ug_ece", name="Calculus and Laplace Transforms", credits=4, year=1, sem=1),
            Course(id="24UPY171_ECE", degree_id="deg_ug_ece", name="Physics for Engineering and Technology", credits=3, year=1, sem=1),
            Course(id="24UCH172_ECE", degree_id="deg_ug_ece", name="Applied Chemistry", credits=3, year=1, sem=1),
            Course(id="24UCS161_ECE", degree_id="deg_ug_ece", name="Computational Thinking", credits=3, year=1, sem=1),
            Course(id="24UCS171_ECE", degree_id="deg_ug_ece", name="Python Programming", credits=4, year=1, sem=1),
            Course(id="24UME166_ECE", degree_id="deg_ug_ece", name="Engineering Graphics", credits=2, year=1, sem=1),

            # ECE - Semester 2
            Course(id="24UTA261_ECE", degree_id="deg_ug_ece", name="Tamils and Technology", credits=1, year=1, sem=2),
            Course(id="24UEN271_ECE", degree_id="deg_ug_ece", name="Communicative English for Engineers and Professionals - II", credits=3, year=1, sem=2),
            Course(id="24UMA262_ECE", degree_id="deg_ug_ece", name="Complex Variable and Ordinary Differential Equations", credits=4, year=1, sem=2),
            Course(id="24UPY262_ECE", degree_id="deg_ug_ece", name="Physics for Electronics Engineering", credits=3, year=1, sem=2),
            Course(id="24UCH261_ECE", degree_id="deg_ug_ece", name="Environmental Sciences and Sustainability", credits=2, year=1, sem=2),
            Course(id="24UCS271_ECE", degree_id="deg_ug_ece", name="Programming in C", credits=4, year=1, sem=2),
            Course(id="24UEC273_ECE", degree_id="deg_ug_ece", name="Circuit Analysis", credits=3, year=1, sem=2),
            Course(id="24UME266_ECE", degree_id="deg_ug_ece", name="Engineering Practices Laboratory", credits=2, year=1, sem=2),
            Course(id="24USD296_ECE", degree_id="deg_ug_ece", name="Skill Development Course", credits=3, year=1, sem=2),

            # MECH - Semester 1
            Course(id="24UTA161_MECH", degree_id="deg_ug_mech", name="Heritage of Tamils", credits=1, year=1, sem=1),
            Course(id="24UEN171_MECH", degree_id="deg_ug_mech", name="Communicative English for Engineers and Professionals - I", credits=3, year=1, sem=1),
            Course(id="24UMA161_MECH", degree_id="deg_ug_mech", name="Calculus and Matrix Algebra", credits=4, year=1, sem=1),
            Course(id="24UPY172_MECH", degree_id="deg_ug_mech", name="Engineering Physics", credits=3, year=1, sem=1),
            Course(id="24UCH173_MECH", degree_id="deg_ug_mech", name="Materials Chemistry", credits=3, year=1, sem=1),
            Course(id="24UCS161_MECH", degree_id="deg_ug_mech", name="Computational Thinking", credits=3, year=1, sem=1),
            Course(id="24UCS171_MECH", degree_id="deg_ug_mech", name="Python Programming", credits=4, year=1, sem=1),
            Course(id="24UME266_MECH", degree_id="deg_ug_mech", name="Engineering Practices Laboratory", credits=2, year=1, sem=1),

            # MECH - Semester 2
            Course(id="24UTA261_MECH", degree_id="deg_ug_mech", name="Tamils and Technology", credits=1, year=1, sem=2),
            Course(id="24UEN271_MECH", degree_id="deg_ug_mech", name="Communicative English for Engineers and Professionals - II", credits=3, year=1, sem=2),
            Course(id="24UMA261_MECH", degree_id="deg_ug_mech", name="Statistics and Numerical Methods", credits=4, year=1, sem=2),
            Course(id="24UPY263_MECH", degree_id="deg_ug_mech", name="Physics for Mechanical Engineering", credits=3, year=1, sem=2),
            Course(id="24UCH261_MECH", degree_id="deg_ug_mech", name="Environmental Sciences and Sustainability", credits=2, year=1, sem=2),
            Course(id="24UCS271_MECH", degree_id="deg_ug_mech", name="Programming in C", credits=4, year=1, sem=2),
            Course(id="24UEC271_MECH", degree_id="deg_ug_mech", name="Electrical and Instrumentation Engineering", credits=3, year=1, sem=2),
            Course(id="24UME166_MECH", degree_id="deg_ug_mech", name="Engineering Graphics", credits=2, year=1, sem=2),
            Course(id="24USD296_MECH", degree_id="deg_ug_mech", name="Skill Development Course", credits=3, year=1, sem=2),
        ]
        for c in courses: session.add(c)

        # Allocation
        allocations = []
        for a in allocations: session.add(a)

        # Enrollments
        enrollments = []
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

# student1@college.edu, student2@college.edu

# faculty allocated to courses via FacultyCourse
