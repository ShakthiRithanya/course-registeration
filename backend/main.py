from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from api import auth
from sqlmodel import Session, select, func
from db.database import engine, create_db_and_tables, seed_data
from models.schema import User, Course, Enrollment, FacultyCourse, Degree
from typing import List

app = FastAPI(title="Course Registration System")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize DB
@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    seed_data()

# Include Routers
app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])

# Basic Student Info
@app.get("/api/student/profile/{student_id}")
def get_student_profile(student_id: str):
    with Session(engine) as session:
        user = session.get(User, student_id)
        if not user or user.role != "student":
            raise HTTPException(status_code=404, detail="Student not found")
        return user

@app.get("/api/student/enrolled/{student_id}")
def get_enrolled_courses(student_id: str):
    with Session(engine) as session:
        statement = select(Enrollment).where(Enrollment.student_id == student_id)
        enrollments = session.exec(statement).all()
        
        result = []
        for e in enrollments:
            course = session.get(Course, e.course_id)
            faculty = session.get(User, e.faculty_id)
            result.append({
                "enrollment_id": e.id,
                "course_name": course.name if course else "Unknown",
                "course_id": e.course_id,
                "credits": course.credits if course else 0,
                "faculty_name": faculty.name if faculty else "Unknown",
                "status": e.status,
                "grade": e.grade,
                "sem": e.sem
            })
        return result

@app.get("/api/student/enrollable/{student_id}")
def get_enrollable_courses(student_id: str):
    with Session(engine) as session:
        student = session.get(User, student_id)
        if not student: return []
        
        # Simple logic: courses for their degree and year/sem
        # In a real app, logic would be more complex.
        # For mock: Return all courses for B.Tech CSE Year 2 Sem 1
        statement = select(Course) # In real app filter by degree/sem
        courses = session.exec(statement).all()
        
        result = []
        for c in courses:
            # Get faculties for this course
            fac_stmt = select(User).join(FacultyCourse).where(FacultyCourse.course_id == c.id)
            faculties = session.exec(fac_stmt).all()
            
            result.append({
                "id": c.id,
                "name": c.name,
                "credits": c.credits,
                "max_enroll": c.max_enroll,
                "enrolled_count": session.exec(select(func.count(Enrollment.id)).where(Enrollment.course_id == c.id)).one(),
                "faculties": [{"id": f.id, "name": f.name} for f in faculties]
            })
        return result

@app.post("/api/student/enroll")
def enroll_student(data: dict):
    # data: { student_id, selected_courses: [{ course_id, faculty_id }] }
    student_id = data.get("student_id")
    selected = data.get("selected_courses", [])
    
    with Session(engine) as session:
        # Credit check
        total_credits = 0
        for item in selected:
            course = session.get(Course, item['course_id'])
            if course: total_credits += course.credits
        
        if total_credits < 20:
             raise HTTPException(status_code=400, detail=f"Minimum 20 credits required. Current: {total_credits}")
        
        # Capacity check & enrollment
        for item in selected:
             new_enroll = Enrollment(
                 student_id=student_id,
                 course_id=item['course_id'],
                 faculty_id=item['faculty_id'],
                 sem=3, # Mock Sem
                 status="enrolled"
             )
             session.add(new_enroll)
        
        session.commit()
        return {"message": "Enrolled successfully", "total_credits": total_credits}

@app.get("/api/faculty/courses/{faculty_id}")
def get_faculty_courses(faculty_id: str):
    with Session(engine) as session:
        statement = select(Course).join(FacultyCourse).where(FacultyCourse.faculty_id == faculty_id)
        courses = session.exec(statement).all()
        
        result = []
        for c in courses:
            enrolled_count = session.exec(select(func.count(Enrollment.id)).where(Enrollment.course_id == c.id)).one()
            result.append({
                "id": c.id,
                "name": c.name,
                "sem": c.sem,
                "enrolled_count": enrolled_count,
                "max_enroll": c.max_enroll
            })
        return result

@app.get("/api/course/{course_id}/students")
def get_course_students(course_id: str):
    with Session(engine) as session:
        statement = select(User).join(Enrollment, User.id == Enrollment.student_id).where(Enrollment.course_id == course_id, Enrollment.status == 'enrolled')
        students = session.exec(statement).all()
        return students

@app.get("/api/faculty/backlogs/{faculty_id}")
def get_faculty_backlogs(faculty_id: str):
    with Session(engine) as session:
        # Get courses handled by faculty
        # Join User(Student) with Enrollment on course_id where grade == 0 (F)
        statement = select(User, Course).join(Enrollment, User.id == Enrollment.student_id).join(Course, Enrollment.course_id == Course.id).where(Enrollment.faculty_id == faculty_id, Enrollment.status == 'backlog')
        results = session.exec(statement).all()
        
        # results is a list of tuples (User, Course)
        return [{"student_name": r[0].name, "student_id": r[0].id, "course_name": r[1].name, "grade": "F"} for r in results]

@app.get("/api/admin/degrees")
def get_admin_degrees(type: str = None):
    with Session(engine) as session:
        statement = select(Degree)
        if type:
            statement = statement.where(Degree.type == type)
        return session.exec(statement).all()

@app.get("/api/admin/degree/{degree_id}/courses")
def get_degree_courses(degree_id: str):
    with Session(engine) as session:
        statement = select(Course).where(Course.degree_id == degree_id)
        return session.exec(statement).all()

@app.get("/api/admin/degree/{degree_id}/history")
def get_degree_history(degree_id: str):
    with Session(engine) as session:
        # Get all courses for this degree
        courses = session.exec(select(Course).where(Course.degree_id == degree_id)).all()
        course_ids = [c.id for c in courses]
        
        # Get all enrollments for these courses
        completions = session.exec(select(Enrollment).where(Enrollment.course_id.in_(course_ids), Enrollment.status == 'completed')).all()
        
        avg_gpa = sum([e.grade for e in completions]) / len(completions) if completions else 0
        
        return {
            "total_completions": len(completions),
            "avg_gpa": round(avg_gpa, 2),
            "course_breakdown": [{"id": c.id, "name": c.name} for c in courses]
        }

@app.get("/api/admin/faculty")
def get_admin_faculty():
    with Session(engine) as session:
        statement = select(User).where(User.role == 'faculty')
        return session.exec(statement).all()

@app.get("/api/admin/courses")
def get_admin_courses():
    with Session(engine) as session:
        return session.exec(select(Course)).all()

@app.get("/api/admin/stats")
def get_admin_stats():
    with Session(engine) as session:
        total_students = session.exec(select(func.count(User.id)).where(User.role == 'student')).one()
        total_faculty = session.exec(select(func.count(User.id)).where(User.role == 'faculty')).one()
        total_courses = session.exec(select(func.count(Course.id))).one()
        
        # Calculate some capacity metric (mock/real)
        total_capacity = total_courses * 30
        total_enrolled = session.exec(select(func.count(Enrollment.id)).where(Enrollment.status == 'enrolled')).one()
        capacity_perc = (total_enrolled / total_capacity * 100) if total_capacity > 0 else 0
        
        return {
            "total_students": total_students,
            "total_faculty": total_faculty,
            "total_courses": total_courses,
            "capacity_percentage": round(capacity_perc, 1)
        }

@app.post("/api/admin/allocate")
def allocate_faculty(data: dict):
    # data: { faculty_id, course_id }
    f_id = data.get("faculty_id")
    c_id = data.get("course_id")
    with Session(engine) as session:
        # Check if already exists
        exists = session.exec(select(FacultyCourse).where(FacultyCourse.faculty_id == f_id, FacultyCourse.course_id == c_id)).first()
        if not exists:
            alloc = FacultyCourse(faculty_id=f_id, course_id=c_id)
            session.add(alloc)
            session.commit()
        return {"message": "Allocation successful"}

@app.delete("/api/admin/allocate/{faculty_id}/{course_id}")
def remove_allocation(faculty_id: str, course_id: str):
    with Session(engine) as session:
        statement = select(FacultyCourse).where(FacultyCourse.faculty_id == faculty_id, FacultyCourse.course_id == course_id)
        alloc = session.exec(statement).first()
        if alloc:
            session.delete(alloc)
            session.commit()
            return {"message": "Allocation removed"}
        raise HTTPException(status_code=404, detail="Allocation not found")

# Simple Health Check
@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# TODO: migrate on_event to lifespan handler
