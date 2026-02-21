# Course Registration System

A full-stack Course Registration System built with **FastAPI** (backend) and **React + Vite** (frontend).

## Tech Stack
- **Backend**: Python, FastAPI, SQLModel, SQLite, Uvicorn, JWT Auth
- **Frontend**: React 18, Vite, React Router v6, Axios, TailwindCSS, Framer Motion, Lucide Icons

## Roles
| Role | Capabilities |
|------|-------------|
| **Student** | View profile, browse & enroll in courses, view enrolled courses |
| **Faculty** | View assigned courses, student lists, backlog management |
| **Admin** | Manage degrees, faculty allocation, system-wide statistics |

## Getting Started

### Backend
`ash
cd backend
pip install -r requirements.txt
python main.py
`
Server runs at http://localhost:8000

### Frontend
`ash
cd frontend
npm install
npm run dev
`
App runs at http://localhost:5173

## API Endpoints
- POST /api/auth/login – Authenticate user, get JWT
- GET /api/student/profile/{id} – Student profile
- GET /api/student/enrolled/{id} – Enrolled courses
- GET /api/student/enrollable/{id} – Courses available to enroll
- POST /api/student/enroll – Enroll in courses
- GET /api/faculty/courses/{id} – Faculty's assigned courses
- GET /api/course/{id}/students – Students in a course
- GET /api/faculty/backlogs/{id} – Backlog students
- GET /api/admin/degrees – All degree programmes
- GET /api/admin/degree/{id}/courses – Courses for a degree
- GET /api/admin/degree/{id}/history – Academic history
- GET /api/admin/faculty – All faculty
- GET /api/admin/courses – All courses
- GET /api/admin/stats – System statistics
- POST /api/admin/allocate – Allocate faculty to course
- DELETE /api/admin/allocate/{fid}/{cid} – Remove allocation
