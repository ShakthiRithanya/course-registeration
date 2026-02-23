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

        # Students
        dept_prefixes = {
            "deg_ug_csbs": "CSBS",
            "deg_ug_aids": "AIDS",
            "deg_ug_aiml": "AIML",
            "deg_ug_cse": "CSE",
            "deg_ug_it": "IT",
            "deg_ug_cys": "CYS",
            "deg_ug_ece": "ECE",
            "deg_ug_mech": "MECH"
        }

        for deg_id, prefix in dept_prefixes.items():
            for i in range(1, 17):
                roll_no = f"{prefix}{i:03d}"
                year = (i - 1) // 4 + 1
                student = User(
                    id=roll_no,
                    role="student",
                    name=f"Student {roll_no}",
                    email=f"{roll_no.lower()}@college.edu",
                    password_hash=pwd_context.hash("stud123"),
                    dept=prefix,
                    year=year,
                    photo_url=f"https://api.dicebear.com/7.x/avataaars/svg?seed={roll_no}"
                )
                session.add(student)


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
        # We define courses for all 8 semesters for each degree
        all_courses = []

        
        # Helper to add courses
        seen_ids = set()
        def add_bulk_courses(degree_id, data):
            import random
            for sem, semester_courses in data.items():
                year = (sem + 1) // 2
                for code, name, credits in semester_courses:
                    course_id = f"{code}_{degree_id.split('_')[-1]}"
                    if course_id in seen_ids:
                        continue
                    seen_ids.add(course_id)
                    course = Course(
                        id=course_id,
                        degree_id=degree_id,
                        name=name,
                        credits=credits,
                        year=year,
                        sem=sem
                    )
                    all_courses.append(course)
                    # Assign a random faculty
                    faculty = random.choice(faculties)
                    session.add(FacultyCourse(faculty_id=faculty.id, course_id=course_id))

        # CSBS
        add_bulk_courses("deg_ug_csbs", {
            1: [("24UTA161", "Heritage of Tamils", 1), ("24UEN171", "Communicative English I", 3), ("24UMA161", "Calculus and Matrix Algebra", 4), ("24UPY171", "Physics for Engineering", 3), ("24UCH171", "Engineering Chemistry", 3), ("24UCS161", "Computational Thinking", 3), ("24UCS171", "Python Programming", 4), ("24UME266", "Engineering Practices Lab", 2)],
            2: [("24UTA261", "Tamils and Technology", 1), ("24UMA261", "Statistics and Linear Algebra", 4), ("24UPY271", "Physics for Data Science", 3), ("24UCS271", "Data Structures and Algorithms", 4), ("24UCB261", "Fundamentals of Business Systems", 3), ("24UCB271", "Business Systems Lab", 2)],
            3: [("24UMA361", "Algebra and Combinatorics", 4), ("24UCS271", "Design and Analysis of Algorithms", 4), ("24UCB311", "Financial Management", 3), ("24UCB312", "Marketing Management", 3), ("24UCS312", "Object Oriented Programming", 4)],
            4: [("24UMA461", "Probability and Statistics", 4), ("24UCB411", "Business Strategy", 3), ("24UCS412", "Database Management Systems", 4), ("24UCS414", "Operating Systems", 4)],
            5: [("24UHV501", "Universal Human Values", 2), ("24UCB511", "Enterprise resource planning", 3), ("24UCB512", "E-Commerce", 3), ("24UCS511", "Computer Networks", 4)],
            6: [("24UCB611", "Cloud Computing for Business", 3), ("24UCB612", "Business Intelligence", 3)],
            7: [("24UCB711", "Ethics in Business and Tech", 3), ("24UCB712", "Human Resource Management", 3)],
            8: [("24UCB895", "Project Work", 10)]
        })

        # AIDS
        add_bulk_courses("deg_ug_aids", {
            1: [("24UTA161", "Heritage of Tamils", 1), ("24UEN171", "Communicative English I", 3), ("24UMA161", "Calculus and Matrix Algebra", 4), ("24UPY171", "Physics for Engineering", 3), ("24UCH171", "Engineering Chemistry", 3), ("24UCS161", "Computational Thinking", 3), ("24UCS171", "Python Programming", 4), ("24UME166", "Engineering Graphics", 2)],
            2: [("24UTA261", "Tamils and Technology", 1), ("24UEN271", "Communicative English II", 3), ("24UMA261", "Statistics and Numerical Methods", 4), ("24UPY261", "Physics for Information Science", 3), ("24UCH261", "Environmental Sciences", 2), ("24UCS271", "Programming in C", 4), ("24UEC272", "Basic Electrical and Electronics", 3), ("24UME266", "Engineering Practices Lab", 2)],
            3: [("24UMA361", "Algebra and Combinatorics", 4), ("24UEC341", "Digital Principals", 4), ("24UAD302", "Artificial Intelligence", 3), ("24UCS414", "Operating Systems", 4), ("24UAD311", "Foundations of Data Science", 4), ("24UAD312", "OOPS for Data Structures", 3)],
            4: [("24UMA461", "Probability and Number Theory", 4), ("24UCS511", "Computer Networks", 4), ("24UAD411", "Database Design", 3), ("24UCS301", "Design and Analysis of Algorithms", 4), ("24UAM512", "Machine Learning", 4)],
            5: [("24UHV501", "Universal Human Values", 2), ("24UAD511", "Deep Learning", 4), ("24UAD512", "Data Exploration", 3), ("24UAD513", "Generative AI", 3)],
            6: [("24UAD611", "Big Data Analytics", 4), ("24UAD612", "AR and VR", 3)],
            7: [("24UAD701", "Ethics and AI", 3), ("24UAD711", "Devops", 4)],
            8: [("24UAD895", "Project Work", 10)]
        })

        # AIML
        add_bulk_courses("deg_ug_aiml", {
            1: [("24UTA161", "Heritage of Tamils", 1), ("24UEN171", "Communicative English I", 3), ("24UMA161", "Calculus and Matrix Algebra", 4), ("24UPY171", "Physics for Engineering", 3), ("24UCH171", "Engineering Chemistry", 3), ("24UCS161", "Computational Thinking", 3), ("24UCS171", "Python Programming", 4), ("24UME266", "Engineering Practices Lab", 2)],
            2: [("24UTA261", "Tamils and Technology", 1), ("24UEN271", "Communicative English II", 3), ("24UMA261", "Statistics and Numerical Methods", 4), ("24UPY261", "Physics for Information Science", 3), ("24UCH261", "Environmental Sciences", 2), ("24UCS271", "Programming in C", 4), ("24UEC272", "Basic Electrical and Electronics", 3), ("24UME166", "Engineering Graphics", 2)],
            3: [("24UMA361", "Algebra and Combinatorics", 4), ("24UEC341", "Digital Principles", 4), ("24UAD311", "Foundations of Data Science", 4), ("24UTI311", "Data Structures and Algorithms", 4), ("24UCS312", "Object Oriented Programming", 4), ("24UCS412", "Database Management Systems", 4)],
            4: [("24UMA463", "Optimization Techniques", 4), ("24UAM411", "Artificial Intelligence", 4), ("24UCB513", "Object Oriented Software Engineering", 3), ("24UCS511", "Computer Networks", 4), ("24UCS414", "Operating Systems", 4)],
            5: [("24UHV501", "Universal Human Values", 2), ("24UAM511", "Natural Language Processing", 3), ("24UAM512", "Machine Learning", 4), ("24UIT411", "Web Technologies", 3)],
            6: [("24UAM611", "Deep Learning for Vision", 3), ("24UAD513", "Generative AI", 3)],
            7: [("24UIT701", "Engineering Economics", 3), ("24UCY512", "Cryptography and Cyber Security", 4)],
            8: [("24UAM895", "Project Work", 10)]
        })

        # CSE
        add_bulk_courses("deg_ug_cse", {
            1: [("24UTA161", "Heritage of Tamils", 1), ("24UEN171", "Communicative English I", 3), ("24UMA161", "Calculus and Matrix Algebra", 4), ("24UPY171", "Physics for Engineering", 3), ("24UCH171", "Engineering Chemistry", 3), ("24UCS161", "Computational Thinking", 3), ("24UCS171", "Python Programming", 4), ("24UME166", "Engineering Graphics", 2)],
            2: [("24UTA261", "Tamils and Technology", 1), ("24UEN271", "Communicative English II", 3), ("24UMA261", "Statistics and Numerical Methods", 4), ("24UPY261", "Physics for Information Science", 3), ("24UCH261", "Environmental Sciences", 2), ("24UCS271", "Programming in C", 4), ("24UEC272", "Basic Electrical and Electronics", 3), ("24UME266", "Engineering Practices Lab", 2)],
            3: [("24UMA361", "Algebra and Combinatorics", 4), ("24UCS301", "Design and Analysis of Algorithms", 4), ("24UCS311", "Data Structures", 4), ("24UCS312", "Object Oriented Programming", 4), ("24UAD311", "Foundations of Data Science", 4), ("24UEC341", "Digital Principles", 4)],
            4: [("24UMA461", "Probability and Number Theory", 4), ("24UCS401", "Theory of Computation", 4), ("24UCS411", "AI and ML", 4), ("24UCS412", "Database Management Systems", 4), ("24UCS414", "Operating Systems", 4)],
            5: [("24UHV501", "Universal Human Values", 2), ("24UCS511", "Computer Networks", 4), ("24UCS512", "Internet Programming", 4), ("24UCY512", "Cryptography and Cyber Security", 4)],
            6: [("24UCS611", "Compiler Design", 3), ("24UCB513", "Object Oriented Software Engineering", 3)],
            7: [("24UCS701", "Software Project Management", 2), ("24UIT611", "Cloud Computing", 3)],
            8: [("24UCS895", "Project Work", 10)]
        })

        # IT
        add_bulk_courses("deg_ug_it", {
            1: [("24UTA161", "Heritage of Tamils", 1), ("24UEN171", "Communicative English I", 3), ("24UMA161", "Calculus and Matrix Algebra", 4), ("24UPY171", "Physics for Engineering", 3), ("24UCH171", "Engineering Chemistry", 3), ("24UCS161", "Computational Thinking", 3), ("24UCS171", "Python Programming", 4), ("24UME266", "Engineering Practices Lab", 2)],
            2: [("24UTA261", "Tamils and Technology", 1), ("24UEN271", "Communicative English II", 3), ("24UMA261", "Statistics and Numerical Methods", 4), ("24UPY261", "Physics for Information Science", 3), ("24UCH261", "Environmental Sciences", 2), ("24UCS271", "Programming in C", 4), ("24UEC272", "Basic Electrical and Electronics", 3), ("24UME166", "Engineering Graphics", 2)],
            3: [("24UMA361", "Algebra and Combinatorics", 4), ("24UEC341", "Digital Principles", 4), ("24UIT311", "Data Structures and Algorithms", 4), ("24UCS312", "Object Oriented Programming", 4), ("24UCS412", "Database Management Systems", 4), ("24UAD311", "Foundations of Data Science", 4)],
            4: [("24UMA461", "Probability and Number Theory", 4), ("24UCS401", "Theory of Computation", 4), ("24UIT411", "Web Technologies", 3), ("24UCS414", "Operating Systems", 4), ("24UCS511", "Computer Networks", 4)],
            5: [("24UHV501", "Universal Human Values", 2), ("24UIT511", "Full Stack Web Development", 4), ("24UIT512", "Embedded Systems and IoT", 3), ("24UCB513", "Object Oriented Software Engineering", 3)],
            6: [("24UCS411", "AI and Machine Learning", 4), ("24UIT611", "Cloud Computing", 3)],
            7: [("24UIT701", "Engineering Economics", 3), ("24UCY512", "Cryptography and Cyber Security", 4)],
            8: [("24UIT895", "Project Work", 10)]
        })

        # CYS
        add_bulk_courses("deg_ug_cys", {
            1: [("24UTA161", "Heritage of Tamils", 1), ("24UEN171", "Communicative English I", 3), ("24UMA161", "Calculus and Matrix Algebra", 4), ("24UPY171", "Physics for Engineering", 3), ("24UCH171", "Engineering Chemistry", 3), ("24UCS161", "Computational Thinking", 3), ("24UCS171", "Python Programming", 4), ("24UME266", "Engineering Practices Lab", 2)],
            2: [("24UTA261", "Tamils and Technology", 1), ("24UEN271", "Communicative English II", 3), ("24UMA261", "Statistics and Numerical Methods", 4), ("24UPY261", "Physics for Information Science", 3), ("24UCH261", "Environmental Sciences", 2), ("24UCS271", "Programming in C", 4), ("24UEC272", "Basic Electrical and Electronics", 3), ("24UME166", "Engineering Graphics", 2)],
            3: [("24UMA361", "Algebra and Combinatorics", 4), ("24UEC341", "Digital Principles", 4), ("24UIT311", "Data structures and Algorithms", 4), ("24UCS312", "Object Oriented Programming", 4), ("24UCY311", "Data Science for Cyber Security", 4)],
            4: [("24UMA463", "Optimization Techniques", 4), ("24UCS511", "Computer Networks", 4), ("24UCY411", "Database Management Systems", 4), ("24UCY412", "Operating Systems", 4), ("24UCS411", "AI and ML", 4)],
            5: [("24UHV501", "Universal Human Values", 2), ("24UIT411", "Web Technologies", 3), ("24UCY511", "Secure Software Systems", 4), ("24UCY512", "Cryptography and Cyber Security", 4), ("24UCY513", "Secure Coding", 3)],
            6: [("24UCY611", "Network Security", 4)],
            7: [("24UIT701", "Engineering Economics", 3), ("24UCY711", "Ethical Hacking", 4)],
            8: [("24UCY895", "Project Work", 10)]
        })

        # ECE
        add_bulk_courses("deg_ug_ece", {
            1: [("24UTA161", "Heritage of Tamils", 1), ("24UEN171", "Communicative English I", 3), ("24UMA162", "Calculus and Laplace Transforms", 4), ("24UPY171", "Physics for Engineering", 3), ("24UCH172", "Applied Chemistry", 3), ("24UCS161", "Computational Thinking", 3), ("24UCS171", "Python Programming", 4), ("24UME166", "Engineering Graphics", 2)],
            2: [("24UTA261", "Tamils and Technology", 1), ("24UEN271", "Communicative English II", 3), ("24UMA262", "Complex Variable and ODE", 4), ("24UPY262", "Physics for Electronics Engineering", 3), ("24UCH261", "Environmental Sciences", 2), ("24UCS271", "Programming in C", 4), ("24UEC273", "Circuit Analysis", 3), ("24UME266", "Engineering Practices Lab", 2)],
            3: [("24UMA362", "Linear Algebra and Numerical Methods", 4), ("24UEC301", "Signals and Systems", 3), ("24UEC302", "Electrical Engineering", 3), ("24UEC311", "Electronic Devices and Circuits", 3), ("24UEC312", "Digital Electronics", 3), ("24UIT311", "Data Structures and Algorithms", 4)],
            4: [("24UMA462", "Probability and Random Process", 4), ("24UEC401", "Electromagnetic Fields", 3), ("24UEC402", "Control Systems", 3), ("24UEC411", "Analog and Baseband Communication", 3), ("24UEC412", "Transmission Lines and Antennas", 3), ("24UEC413", "Linear and Digital Integrated Circuits", 3)],
            5: [("24UHV501", "Universal Human Values", 2), ("24UEC511", "Digital Signal Processing", 4), ("24UEC512", "Digital Communication", 3), ("24UEC513", "Microprocessors and Microcontrollers", 4)],
            6: [("24UEC611", "Digital VLSI Design", 4), ("24UEC612", "RF and Microwave Engineering", 3)],
            7: [("24UEC701", "Artificial Neural Networks", 3), ("24UEC711", "Wireless Communication", 4)],
            8: [("24UEC895", "Project Work", 10)]
        })

        # MECH
        add_bulk_courses("deg_ug_mech", {
            1: [("24UTA161", "Heritage of Tamils", 1), ("24UEN171", "Communicative English I", 3), ("24UMA161", "Calculus and Matrix Algebra", 4), ("24UPY172", "Engineering Physics", 3), ("24UCH173", "Materials Chemistry", 3), ("24UCS161", "Computational Thinking", 3), ("24UCS171", "Python Programming", 4), ("24UME266", "Engineering Practices Lab", 2)],
            2: [("24UTA261", "Tamils and Technology", 1), ("24UEN271", "Communicative English II", 3), ("24UMA261", "Statistics and Numerical Methods", 4), ("24UPY263", "Physics for Mechanical Engineering", 3), ("24UCH261", "Environmental Sciences", 2), ("24UCS271", "Programming in C", 4), ("24UEC271", "Electrical and Instrumentation Engineering", 3), ("24UME166", "Engineering Graphics", 2)],
            3: [("24UMA363", "Transforms and PDE", 4), ("24UME301", "Engineering Mechanics", 4), ("24UME302", "Engineering Thermodynamics", 4), ("24UME311", "Engineering Materials", 3), ("24UME312", "Fluid Mechanics", 4), ("24UME313", "Manufacturing Processes", 3), ("24UME321", "Machine Drawing", 2)],
            4: [("24UMA463", "Optimization Techniques", 4), ("24UME411", "Hydraulics and Pneumatics", 3), ("24UME412", "Thermal Engineering", 3), ("24UME413", "Theory of Machines", 3), ("24UME414", "Manufacturing Technology", 3), ("24UME415", "Strength of Materials", 3)],
            5: [("24UHV501", "Universal Human Values", 2), ("24UME501", "Design of Machine Elements", 3), ("24UME511", "Heat and Mass Transfer", 4), ("24UME512", "Metrology and Measurements", 3), ("24UME521", "CAD/CAM Lab", 2)],
            6: [("24UME601", "Design of Transmission Systems", 3), ("24UME611", "Finite Element Analysis", 4)],
            7: [("24UME701", "Economics and Project Management", 3), ("24UME711", "Mechatronics and IoT", 3)],
            8: [("24UME895", "Project Work", 10)]
        })

        for c in all_courses: session.add(c)
        session.flush() # Ensure courses have IDs available if needed

        # Enrollments (History)
        import random
        users = session.exec(select(User).where(User.role == "student")).all()
        for student in users:
            student_year = int(student.year)
            # Historic semesters: all semesters before current even semester
            # Current semester = student_year * 2
            # Historic semesters = [1, 2, ..., student_year * 2 - 1]
            historic_sems = list(range(1, student_year * 2))
            
            # Use a deterministic seed per student for reproducible history
            random.seed(student.id)
            
            # Map degree prefixes back to degree IDs
            prefix_to_deg = {v: k for k, v in dept_prefixes.items()}
            degree_id = prefix_to_deg.get(student.dept)
            
            for s in historic_sems:
                statement = select(Course).where(Course.degree_id == degree_id, Course.sem == s)
                sem_courses = session.exec(statement).all()
                for c in sem_courses:
                    # Get faculty handling this course
                    fac_stmt = select(FacultyCourse).where(FacultyCourse.course_id == c.id)
                    alloc = session.exec(fac_stmt).first()
                    faculty_id = alloc.faculty_id if alloc else faculties[0].id
                    
                    is_backlog = random.random() < 0.1 # 10% backlog rate
                    enrollment = Enrollment(
                        student_id=student.id,
                        course_id=c.id,
                        faculty_id=faculty_id,
                        sem=s,
                        status="backlog" if is_backlog else "completed",
                        grade=0.0 if is_backlog else round(random.uniform(2.5, 4.0), 1)
                    )
                    session.add(enrollment)
        
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
