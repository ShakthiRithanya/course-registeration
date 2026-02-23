from sqlmodel import Session, create_engine, select
from db.database import Degree, Course

engine = create_engine("sqlite:///database.db")

def verify():
    with Session(engine) as session:
        degrees = session.exec(select(Degree)).all()
        print(f"Total Degrees: {len(degrees)}")
        for d in degrees:
            courses = session.exec(select(Course).where(Course.degree_id == d.id)).all()
            print(f"- {d.name} ({d.id}): {len(courses)} courses")

if __name__ == "__main__":
    verify()
