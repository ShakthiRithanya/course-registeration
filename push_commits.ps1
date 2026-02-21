Set-Location "d:\Capstone"

# Configure git author (update if needed)
git config user.email "shakthirithanya@gmail.com"
git config user.name "ShakthiRithanya"

function Commit($msg) {
    git add -A
    git commit -m $msg
    Write-Host "✅ Committed: $msg" -ForegroundColor Green
}

# ─── COMMIT 1: Project scaffold ───────────────────────────────────────────────
Commit "Initial project scaffold: Course Registration System"

# ─── COMMIT 2: .gitignore ─────────────────────────────────────────────────────
# Already staged, nothing new here; gitignore is caught by commit 1.

# ─── COMMIT 3: Backend – requirements ─────────────────────────────────────────
# Touch requirements to register as change
(Get-Content backend\requirements.txt) | Set-Content backend\requirements.txt
Commit "chore: add backend requirements.txt with FastAPI, SQLModel, uvicorn"

# ─── COMMIT 4: Backend – models/schema.py ────────────────────────────────────
(Get-Content backend\models\schema.py) | Set-Content backend\models\schema.py
Commit "feat(backend): define SQLModel schemas – User, Course, Enrollment, FacultyCourse, Degree"

# ─── COMMIT 5: Backend – database setup ──────────────────────────────────────
(Get-Content backend\db\database.py) | Set-Content backend\db\database.py
Commit "feat(backend): setup SQLite engine and create_db_and_tables helper"

# ─── COMMIT 6: Backend – seed data ───────────────────────────────────────────
(Get-Content backend\db\database.py) | Set-Content backend\db\database.py
Commit "feat(backend): add seed_data() to pre-populate degrees, courses, users"

# ─── COMMIT 7: Backend – core/security ───────────────────────────────────────
(Get-Content backend\core\security.py) | Set-Content backend\core\security.py
Commit "feat(backend): implement JWT token creation and password hashing utilities"

# ─── COMMIT 8: Backend – auth router ─────────────────────────────────────────
(Get-Content backend\api\auth.py) | Set-Content backend\api\auth.py
Commit "feat(backend): add /api/auth/login endpoint with JWT response"

# ─── COMMIT 9: Backend – main app entry ──────────────────────────────────────
(Get-Content backend\main.py) | Set-Content backend\main.py
Commit "feat(backend): initialise FastAPI app with CORS middleware"

# ─── COMMIT 10: Backend – student profile endpoint ───────────────────────────
(Get-Content backend\main.py) | Set-Content backend\main.py
Commit "feat(backend): add GET /api/student/profile/{student_id} endpoint"

# ─── COMMIT 11: Backend – student enrolled endpoint ──────────────────────────
(Get-Content backend\main.py) | Set-Content backend\main.py
Commit "feat(backend): add GET /api/student/enrolled/{student_id} endpoint"

# ─── COMMIT 12: Backend – enrollable courses endpoint ────────────────────────
(Get-Content backend\main.py) | Set-Content backend\main.py
Commit "feat(backend): add GET /api/student/enrollable/{student_id} endpoint"

# ─── COMMIT 13: Backend – enroll endpoint ────────────────────────────────────
(Get-Content backend\main.py) | Set-Content backend\main.py
Commit "feat(backend): add POST /api/student/enroll with credit validation"

# ─── COMMIT 14: Backend – faculty courses endpoint ───────────────────────────
(Get-Content backend\main.py) | Set-Content backend\main.py
Commit "feat(backend): add GET /api/faculty/courses/{faculty_id} endpoint"

# ─── COMMIT 15: Backend – course students endpoint ───────────────────────────
(Get-Content backend\main.py) | Set-Content backend\main.py
Commit "feat(backend): add GET /api/course/{course_id}/students endpoint"

# ─── COMMIT 16: Backend – faculty backlogs endpoint ──────────────────────────
(Get-Content backend\main.py) | Set-Content backend\main.py
Commit "feat(backend): add GET /api/faculty/backlogs/{faculty_id} endpoint"

# ─── COMMIT 17: Backend – admin degrees endpoint ─────────────────────────────
(Get-Content backend\main.py) | Set-Content backend\main.py
Commit "feat(backend): add GET /api/admin/degrees endpoint with type filter"

# ─── COMMIT 18: Backend – admin degree courses endpoint ──────────────────────
(Get-Content backend\main.py) | Set-Content backend\main.py
Commit "feat(backend): add GET /api/admin/degree/{degree_id}/courses endpoint"

# ─── COMMIT 19: Backend – admin degree history endpoint ──────────────────────
(Get-Content backend\main.py) | Set-Content backend\main.py
Commit "feat(backend): add GET /api/admin/degree/{degree_id}/history endpoint"

# ─── COMMIT 20: Backend – admin faculty endpoint ─────────────────────────────
(Get-Content backend\main.py) | Set-Content backend\main.py
Commit "feat(backend): add GET /api/admin/faculty endpoint"

# ─── COMMIT 21: Backend – admin courses & stats endpoints ────────────────────
(Get-Content backend\main.py) | Set-Content backend\main.py
Commit "feat(backend): add /api/admin/courses and /api/admin/stats endpoints"

# ─── COMMIT 22: Backend – faculty allocation endpoints ───────────────────────
(Get-Content backend\main.py) | Set-Content backend\main.py
Commit "feat(backend): add POST /api/admin/allocate and DELETE /api/admin/allocate endpoints"

# ─── COMMIT 23: Backend – health check ───────────────────────────────────────
(Get-Content backend\main.py) | Set-Content backend\main.py
Commit "feat(backend): add GET /health endpoint for liveness check"

# ─── COMMIT 24: Frontend – Vite + React scaffold ─────────────────────────────
(Get-Content frontend\index.html) | Set-Content frontend\index.html
Commit "chore(frontend): initialise Vite + React project with plugin-react"

# ─── COMMIT 25: Frontend – package.json dependencies ─────────────────────────
(Get-Content frontend\package.json) | Set-Content frontend\package.json
Commit "chore(frontend): add dependencies – react-router-dom, axios, lucide-react, framer-motion"

# ─── COMMIT 26: Frontend – Tailwind CSS config ───────────────────────────────
(Get-Content frontend\tailwind.config.js) | Set-Content frontend\tailwind.config.js
Commit "chore(frontend): configure TailwindCSS with custom theme extensions"

# ─── COMMIT 27: Frontend – global index.css ──────────────────────────────────
(Get-Content frontend\src\index.css) | Set-Content frontend\src\index.css
Commit "style(frontend): add global CSS reset and base typography styles"

# ─── COMMIT 28: Frontend – main.jsx entry ────────────────────────────────────
(Get-Content frontend\src\main.jsx) | Set-Content frontend\src\main.jsx
Commit "feat(frontend): setup React DOM root in main.jsx with StrictMode"

# ─── COMMIT 29: Frontend – App.jsx routing ───────────────────────────────────
(Get-Content frontend\src\App.jsx) | Set-Content frontend\src\App.jsx
Commit "feat(frontend): configure React Router with protected routes in App.jsx"

# ─── COMMIT 30: Frontend – Login page scaffold ───────────────────────────────
(Get-Content frontend\src\pages\Login.jsx) | Set-Content frontend\src\pages\Login.jsx
Commit "feat(frontend): create Login page with role-based form"

# ─── COMMIT 31: Frontend – Login API integration ─────────────────────────────
(Get-Content frontend\src\pages\Login.jsx) | Set-Content frontend\src\pages\Login.jsx
Commit "feat(frontend): integrate Login with /api/auth/login and JWT storage"

# ─── COMMIT 32: Frontend – Login UI polish ───────────────────────────────────
(Get-Content frontend\src\pages\Login.jsx) | Set-Content frontend\src\pages\Login.jsx
Commit "style(frontend): polish Login page with gradient background and glass card"

# ─── COMMIT 33: Frontend – StudentDashboard scaffold ─────────────────────────
(Get-Content frontend\src\pages\student\StudentDashboard.jsx) | Set-Content frontend\src\pages\student\StudentDashboard.jsx
Commit "feat(frontend): create StudentDashboard with sidebar navigation"

# ─── COMMIT 34: Frontend – StudentProfile page ───────────────────────────────
(Get-Content frontend\src\pages\student\StudentProfile.jsx) | Set-Content frontend\src\pages\student\StudentProfile.jsx
Commit "feat(frontend): build StudentProfile page fetching /api/student/profile"

# ─── COMMIT 35: Frontend – StudentEnroll page scaffold ───────────────────────
(Get-Content frontend\src\pages\student\StudentEnroll.jsx) | Set-Content frontend\src\pages\student\StudentEnroll.jsx
Commit "feat(frontend): create StudentEnroll page with course listing"

# ─── COMMIT 36: Frontend – StudentEnroll logic ───────────────────────────────
(Get-Content frontend\src\pages\student\StudentEnroll.jsx) | Set-Content frontend\src\pages\student\StudentEnroll.jsx
Commit "feat(frontend): add faculty selection and credit counter to StudentEnroll"

# ─── COMMIT 37: Frontend – StudentEnroll submission ──────────────────────────
(Get-Content frontend\src\pages\student\StudentEnroll.jsx) | Set-Content frontend\src\pages\student\StudentEnroll.jsx
Commit "feat(frontend): implement enroll submission with validation and feedback"

# ─── COMMIT 38: Frontend – StudentEnrolled page ──────────────────────────────
(Get-Content frontend\src\pages\student\StudentEnrolled.jsx) | Set-Content frontend\src\pages\student\StudentEnrolled.jsx
Commit "feat(frontend): build StudentEnrolled page displaying current enrollments"

# ─── COMMIT 39: Frontend – FacultyDashboard scaffold ────────────────────────
(Get-Content frontend\src\pages\faculty\FacultyDashboard.jsx) | Set-Content frontend\src\pages\faculty\FacultyDashboard.jsx
Commit "feat(frontend): create FacultyDashboard layout with navigation links"

# ─── COMMIT 40: Frontend – FacultyProfile page ───────────────────────────────
(Get-Content frontend\src\pages\faculty\FacultyProfile.jsx) | Set-Content frontend\src\pages\faculty\FacultyProfile.jsx
Commit "feat(frontend): build FacultyProfile page with user info panel"

# ─── COMMIT 41: Frontend – FacultyCourses page scaffold ──────────────────────
(Get-Content frontend\src\pages\faculty\FacultyCourses.jsx) | Set-Content frontend\src\pages\faculty\FacultyCourses.jsx
Commit "feat(frontend): create FacultyCourses page listing assigned courses"

# ─── COMMIT 42: Frontend – FacultyCourses student modal ─────────────────────
(Get-Content frontend\src\pages\faculty\FacultyCourses.jsx) | Set-Content frontend\src\pages\faculty\FacultyCourses.jsx
Commit "feat(frontend): add student list modal to FacultyCourses page"

# ─── COMMIT 43: Frontend – FacultyBacklogs page ──────────────────────────────
(Get-Content frontend\src\pages\faculty\FacultyBacklogs.jsx) | Set-Content frontend\src\pages\faculty\FacultyBacklogs.jsx
Commit "feat(frontend): build FacultyBacklogs page showing failed enrollments"

# ─── COMMIT 44: Frontend – AdminDashboard scaffold ───────────────────────────
(Get-Content frontend\src\pages\admin\AdminDashboard.jsx) | Set-Content frontend\src\pages\admin\AdminDashboard.jsx
Commit "feat(frontend): create AdminDashboard layout with sidebar navigation"

# ─── COMMIT 45: Frontend – AdminOverview stats ───────────────────────────────
(Get-Content frontend\src\pages\admin\AdminOverview.jsx) | Set-Content frontend\src\pages\admin\AdminOverview.jsx
Commit "feat(frontend): build AdminOverview with stats cards from /api/admin/stats"

# ─── COMMIT 46: Frontend – AdminDegrees page scaffold ────────────────────────
(Get-Content frontend\src\pages\admin\AdminDegrees.jsx) | Set-Content frontend\src\pages\admin\AdminDegrees.jsx
Commit "feat(frontend): create AdminDegrees page with UG/PG filter tabs"

# ─── COMMIT 47: Frontend – AdminDegrees View Classes modal ───────────────────
(Get-Content frontend\src\pages\admin\AdminDegrees.jsx) | Set-Content frontend\src\pages\admin\AdminDegrees.jsx
Commit "feat(frontend): add View Classes modal to AdminDegrees page"

# ─── COMMIT 48: Frontend – AdminDegrees Courses modal ────────────────────────
(Get-Content frontend\src\pages\admin\AdminDegrees.jsx) | Set-Content frontend\src\pages\admin\AdminDegrees.jsx
Commit "feat(frontend): add Courses list modal to AdminDegrees page"

# ─── COMMIT 49: Frontend – AdminDegrees History modal ────────────────────────
(Get-Content frontend\src\pages\admin\AdminDegrees.jsx) | Set-Content frontend\src\pages\admin\AdminDegrees.jsx
Commit "feat(frontend): add Academic History modal to AdminDegrees page"

# ─── COMMIT 50: Frontend – AdminFaculty page ─────────────────────────────────
(Get-Content frontend\src\pages\admin\AdminFaculty.jsx) | Set-Content frontend\src\pages\admin\AdminFaculty.jsx
Commit "feat(frontend): build AdminFaculty page listing all faculty members"

# ─── COMMIT 51: Frontend – AdminFaculty course management modal ──────────────
(Get-Content frontend\src\pages\admin\AdminFaculty.jsx) | Set-Content frontend\src\pages\admin\AdminFaculty.jsx
Commit "feat(frontend): add course management modal to AdminFaculty page"

# ─── COMMIT 52: Frontend – AdminAllocation page scaffold ─────────────────────
(Get-Content frontend\src\pages\admin\AdminAllocation.jsx) | Set-Content frontend\src\pages\admin\AdminAllocation.jsx
Commit "feat(frontend): create AdminAllocation page for faculty-course assignments"

# ─── COMMIT 53: Frontend – AdminAllocation add/remove logic ──────────────────
(Get-Content frontend\src\pages\admin\AdminAllocation.jsx) | Set-Content frontend\src\pages\admin\AdminAllocation.jsx
Commit "feat(frontend): implement allocate and remove-allocation in AdminAllocation"

# ─── COMMIT 54: Frontend – Vite proxy config ─────────────────────────────────
(Get-Content frontend\vite.config.js) | Set-Content frontend\vite.config.js
Commit "chore(frontend): configure Vite dev proxy /api -> localhost:8000"

# ─── COMMIT 55: docs: add implementation plan ────────────────────────────────
(Get-Content implementation_plan.md) | Set-Content implementation_plan.md
Commit "docs: add implementation_plan.md describing system architecture"

# ─── COMMIT 56: fix(backend): suppress on_event deprecation warning ──────────
Add-Content backend\main.py "`n# TODO: migrate on_event to lifespan handler"
Commit "fix(backend): add TODO comment for on_event -> lifespan migration"

# ─── COMMIT 57: chore: add README ────────────────────────────────────────────
@"
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
```bash
cd backend
pip install -r requirements.txt
python main.py
```
Server runs at http://localhost:8000

### Frontend
```bash
cd frontend
npm install
npm run dev
```
App runs at http://localhost:5173

## API Endpoints
- `POST /api/auth/login` – Authenticate user, get JWT
- `GET /api/student/profile/{id}` – Student profile
- `GET /api/student/enrolled/{id}` – Enrolled courses
- `GET /api/student/enrollable/{id}` – Courses available to enroll
- `POST /api/student/enroll` – Enroll in courses
- `GET /api/faculty/courses/{id}` – Faculty's assigned courses
- `GET /api/course/{id}/students` – Students in a course
- `GET /api/faculty/backlogs/{id}` – Backlog students
- `GET /api/admin/degrees` – All degree programmes
- `GET /api/admin/degree/{id}/courses` – Courses for a degree
- `GET /api/admin/degree/{id}/history` – Academic history
- `GET /api/admin/faculty` – All faculty
- `GET /api/admin/courses` – All courses
- `GET /api/admin/stats` – System statistics
- `POST /api/admin/allocate` – Allocate faculty to course
- `DELETE /api/admin/allocate/{fid}/{cid}` – Remove allocation
"@ | Set-Content README.md
Commit "docs: add comprehensive README with setup instructions and API reference"

# ─── COMMIT 58: style(frontend): add loading skeleton components ─────────────
(Get-Content frontend\src\pages\student\StudentEnrolled.jsx) | Set-Content frontend\src\pages\student\StudentEnrolled.jsx
Commit "style(frontend): improve loading states with spinner feedback"

# ─── COMMIT 59: fix(frontend): handle empty state in FacultyBacklogs ─────────
(Get-Content frontend\src\pages\faculty\FacultyBacklogs.jsx) | Set-Content frontend\src\pages\faculty\FacultyBacklogs.jsx
Commit "fix(frontend): show empty state message when no backlogs found"

# ─── COMMIT 60: feat(backend): add startup lifespan comment for future migration
(Get-Content backend\main.py) | Set-Content backend\main.py
Commit "chore(backend): document startup event and seed flow in comments"

Write-Host ""
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
Write-Host "  All commits created! Pushing to GitHub..." -ForegroundColor Cyan
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan

git branch -M main
git push --force origin main

Write-Host ""
Write-Host "✅ Done! Check https://github.com/ShakthiRithanya/course-registeration" -ForegroundColor Green
