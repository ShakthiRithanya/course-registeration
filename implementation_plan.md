# Course Registration Module - Implementation Plan

## Phase 1: UI/UX & Mock Backend

### 1. Technology Stack
- **Backend**: FastAPI, SQLModel, SQLite (In-Memory), JWT Auth.
- **Frontend**: React (Vite), Tailwind CSS, Framer Motion, TanStack Query.
- **Styling**: Premium academic theme (Whites, Blues, Glassmorphism).

### 2. File Structure
```text
/
├── backend/
│   ├── main.py
│   ├── models/
│   │   └── schema.py
│   ├── api/
│   │   ├── auth.py
│   │   ├── student.py
│   │   ├── faculty.py
│   │   └── admin.py
│   ├── core/
│   │   ├── security.py
│   │   └── config.py
│   ├── db/
│   │   └── database.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── auth/
│   │   │   ├── dashboard/
│   │   │   ├── shared/
│   │   │   └── UI/
│   │   ├── pages/
│   │   │   ├── student/
│   │   │   ├── faculty/
│   │   │   └── admin/
│   │   ├── layouts/
│   │   ├── hooks/
│   │   └── App.jsx
│   ├── tailwind.config.js
│   └── package.json
└── .env
```

### 3. Database Schema
- **User**: id, role, name, email, photo_url, dept, year, designation.
- **Degree**: id, type (UG/PG), name.
- **Class**: id, degree_id, year, sem.
- **Course**: id, degree_id, year, sem, name, credits, max_enroll, status.
- **FacultyCourse**: faculty_id, course_id (m2m).
- **Enrollment**: student_id, course_id, faculty_id, sem, status, grade.

### 4. Key Workflows
1. **Login**: Role-based redirect to `/student`, `/faculty`, or `/admin`.
2. **Student Enrollment**: Credit count validation (min 20) and seat capacity check.
3. **Faculty View**: Real-time list of enrolled students per course.
4. **Admin Allocation**: Linking faculty to courses, instantly visible to students.

### 5. Seed Data (50+ Records)
- 1 Admin
- 5 Students (Mixed years/depts)
- 5 Faculty (Mixed depts)
- 20+ Courses (UG/PG)
- 20+ Mock Enrollments (Backlogs/Completed)
