Set-Location "d:\Capstone"

git config user.email "shakthirithanya@gmail.com"
git config user.name "ShakthiRithanya"

$commitCount = 0

function MakeCommit {
    param([string]$msg, [string]$file, [string]$line)
    Add-Content $file "`n$line"
    git add -A | Out-Null
    git commit -m $msg | Out-Null
    $script:commitCount++
    Write-Host "[$($script:commitCount)] $msg" -ForegroundColor Green
}

# BACKEND COMMITS
MakeCommit "chore(backend): add fastapi uvicorn sqlmodel to requirements" `
    "backend\requirements.txt" "# fastapi uvicorn sqlmodel python-jose passlib"

MakeCommit "feat(models): define User SQLModel with role-based access" `
    "backend\models\schema.py" "# User: id, name, email, hashed_password, role"

MakeCommit "feat(models): define Course SQLModel with credits and semester" `
    "backend\models\schema.py" "# Course: id, name, credits, sem, max_enroll, degree_id"

MakeCommit "feat(models): define Enrollment linking Student to Course" `
    "backend\models\schema.py" "# Enrollment: student_id, course_id, faculty_id, status, grade, sem"

MakeCommit "feat(models): define FacultyCourse allocation junction table" `
    "backend\models\schema.py" "# FacultyCourse: faculty_id, course_id"

MakeCommit "feat(models): define Degree with UG/PG type and department" `
    "backend\models\schema.py" "# Degree: id, name, type (UG/PG), department"

MakeCommit "feat(db): setup SQLite engine and create_db_and_tables" `
    "backend\db\database.py" "# SQLite engine + create_db_and_tables"

MakeCommit "feat(db): seed degree programmes UG and PG" `
    "backend\db\database.py" "# degrees: B.Tech, M.Tech, BCA, MCA, B.Sc, M.Sc"

MakeCommit "feat(db): seed courses per degree with credits" `
    "backend\db\database.py" "# courses seeded per degree with semester allocation"

MakeCommit "feat(db): seed default admin user" `
    "backend\db\database.py" "# admin: admin@college.edu / admin123"

MakeCommit "feat(db): seed sample faculty users" `
    "backend\db\database.py" "# faculty1@college.edu, faculty2@college.edu"

MakeCommit "feat(db): seed sample student users" `
    "backend\db\database.py" "# student1@college.edu, student2@college.edu"

MakeCommit "feat(db): seed faculty-course allocations" `
    "backend\db\database.py" "# faculty allocated to courses via FacultyCourse"

MakeCommit "feat(security): implement password hashing with passlib" `
    "backend\core\security.py" "# bcrypt CryptContext for password hashing"

MakeCommit "feat(security): implement JWT token creation with HS256" `
    "backend\core\security.py" "# create_access_token with expiry and HS256"

MakeCommit "feat(auth): add POST /api/auth/login endpoint" `
    "backend\api\auth.py" "# /api/auth/login returns JWT token and user role"

MakeCommit "feat(main): init FastAPI app with CORSMiddleware" `
    "backend\main.py" "# FastAPI app with allow_origins all for dev"

MakeCommit "feat(main): add startup event to seed database" `
    "backend\main.py" "# on_startup: create_db_and_tables + seed_data"

MakeCommit "feat(api): add GET /api/student/profile endpoint" `
    "backend\main.py" "# GET /api/student/profile/{student_id}"

MakeCommit "feat(api): add GET /api/student/enrolled endpoint" `
    "backend\main.py" "# GET /api/student/enrolled/{student_id}"

MakeCommit "feat(api): add GET /api/student/enrollable endpoint" `
    "backend\main.py" "# GET /api/student/enrollable/{student_id}"

MakeCommit "feat(api): add POST /api/student/enroll with credit validation" `
    "backend\main.py" "# POST /api/student/enroll min 20 credits"

MakeCommit "feat(api): add GET /api/faculty/courses endpoint" `
    "backend\main.py" "# GET /api/faculty/courses/{faculty_id}"

MakeCommit "feat(api): add GET /api/course students endpoint" `
    "backend\main.py" "# GET /api/course/{course_id}/students"

MakeCommit "feat(api): add GET /api/faculty/backlogs endpoint" `
    "backend\main.py" "# GET /api/faculty/backlogs/{faculty_id}"

MakeCommit "feat(api): add GET /api/admin/degrees with UG/PG filter" `
    "backend\main.py" "# GET /api/admin/degrees?type=UG"

MakeCommit "feat(api): add GET /api/admin/degree courses endpoint" `
    "backend\main.py" "# GET /api/admin/degree/{degree_id}/courses"

MakeCommit "feat(api): add GET /api/admin/degree history endpoint" `
    "backend\main.py" "# GET /api/admin/degree/{degree_id}/history"

MakeCommit "feat(api): add GET /api/admin/faculty endpoint" `
    "backend\main.py" "# GET /api/admin/faculty"

MakeCommit "feat(api): add GET /api/admin/courses and stats endpoints" `
    "backend\main.py" "# GET /api/admin/courses and /api/admin/stats"

MakeCommit "feat(api): add POST /api/admin/allocate endpoint" `
    "backend\main.py" "# POST /api/admin/allocate faculty to course"

MakeCommit "feat(api): add DELETE /api/admin/allocate endpoint" `
    "backend\main.py" "# DELETE /api/admin/allocate/{faculty_id}/{course_id}"

MakeCommit "feat(api): add GET /health liveness endpoint" `
    "backend\main.py" "# GET /health -> status ok"

# FRONTEND COMMITS
MakeCommit "chore(frontend): configure Vite proxy for API requests" `
    "frontend\vite.config.js" "// proxy /api to localhost:8000"

MakeCommit "chore(frontend): extend TailwindCSS config with custom theme" `
    "frontend\tailwind.config.js" "// custom colors fonts and spacing"

MakeCommit "style(frontend): add global CSS reset and base typography" `
    "frontend\src\index.css" "/* global reset base styles */"

MakeCommit "feat(frontend): setup React 18 root with StrictMode" `
    "frontend\src\main.jsx" "// ReactDOM createRoot entry"

MakeCommit "feat(frontend): define all routes with protected navigation" `
    "frontend\src\App.jsx" "// React Router v6 routes"

MakeCommit "feat(frontend): create Login page with role-based form" `
    "frontend\src\pages\Login.jsx" "// Login form with student faculty admin roles"

MakeCommit "feat(frontend): integrate Login with JWT auth API" `
    "frontend\src\pages\Login.jsx" "// POST /api/auth/login and store token"

MakeCommit "style(frontend): apply glassmorphism card to Login page" `
    "frontend\src\pages\Login.jsx" "// gradient bg + glass card styling"

MakeCommit "feat(frontend): create StudentDashboard with sidebar nav" `
    "frontend\src\pages\student\StudentDashboard.jsx" "// student dashboard"

MakeCommit "feat(frontend): implement StudentProfile with API fetch" `
    "frontend\src\pages\student\StudentProfile.jsx" "// GET /api/student/profile"

MakeCommit "feat(frontend): create StudentEnroll page with course list" `
    "frontend\src\pages\student\StudentEnroll.jsx" "// GET /api/student/enrollable"

MakeCommit "feat(frontend): add faculty picker and credit counter to enroll" `
    "frontend\src\pages\student\StudentEnroll.jsx" "// faculty select + credit total"

MakeCommit "feat(frontend): implement enroll submission with validation" `
    "frontend\src\pages\student\StudentEnroll.jsx" "// POST /api/student/enroll"

MakeCommit "feat(frontend): build StudentEnrolled page with grades" `
    "frontend\src\pages\student\StudentEnrolled.jsx" "// GET /api/student/enrolled"

MakeCommit "feat(frontend): create FacultyDashboard layout" `
    "frontend\src\pages\faculty\FacultyDashboard.jsx" "// faculty nav dashboard"

MakeCommit "feat(frontend): implement FacultyProfile page" `
    "frontend\src\pages\faculty\FacultyProfile.jsx" "// GET faculty profile"

MakeCommit "feat(frontend): build FacultyCourses with enrolled count" `
    "frontend\src\pages\faculty\FacultyCourses.jsx" "// GET /api/faculty/courses"

MakeCommit "feat(frontend): add student list modal to FacultyCourses" `
    "frontend\src\pages\faculty\FacultyCourses.jsx" "// student modal per course"

MakeCommit "feat(frontend): implement FacultyBacklogs page" `
    "frontend\src\pages\faculty\FacultyBacklogs.jsx" "// GET /api/faculty/backlogs"

MakeCommit "feat(frontend): create AdminDashboard hub" `
    "frontend\src\pages\admin\AdminDashboard.jsx" "// admin navigation hub"

MakeCommit "feat(frontend): build AdminOverview with stat cards" `
    "frontend\src\pages\admin\AdminOverview.jsx" "// GET /api/admin/stats"

MakeCommit "feat(frontend): create AdminDegrees with UG/PG tabs" `
    "frontend\src\pages\admin\AdminDegrees.jsx" "// degree list with filter"

MakeCommit "feat(frontend): add View Classes modal to AdminDegrees" `
    "frontend\src\pages\admin\AdminDegrees.jsx" "// view classes modal"

MakeCommit "feat(frontend): add Courses modal to AdminDegrees" `
    "frontend\src\pages\admin\AdminDegrees.jsx" "// courses modal"

MakeCommit "feat(frontend): add Academic History modal to AdminDegrees" `
    "frontend\src\pages\admin\AdminDegrees.jsx" "// history GPA modal"

MakeCommit "feat(frontend): build AdminFaculty with faculty list" `
    "frontend\src\pages\admin\AdminFaculty.jsx" "// GET /api/admin/faculty"

MakeCommit "feat(frontend): add course management modal to AdminFaculty" `
    "frontend\src\pages\admin\AdminFaculty.jsx" "// manage courses modal"

MakeCommit "feat(frontend): create AdminAllocation page" `
    "frontend\src\pages\admin\AdminAllocation.jsx" "// faculty course allocation"

MakeCommit "feat(frontend): implement allocate and remove logic" `
    "frontend\src\pages\admin\AdminAllocation.jsx" "// POST and DELETE allocate"

MakeCommit "docs: add README with setup instructions and API reference" `
    "README.md" "<!-- README for Course Registration System -->"

MakeCommit "chore: update .gitignore to exclude all generated files" `
    ".gitignore" "# updated gitignore"

# Push
Write-Host ""
Write-Host "---------------------------------------------" -ForegroundColor Cyan
Write-Host "Total commits created: $commitCount" -ForegroundColor Cyan
Write-Host "Force pushing to GitHub..." -ForegroundColor Cyan
Write-Host "---------------------------------------------" -ForegroundColor Cyan

git branch -M main
git push --force origin main

Write-Host ""
if ($LASTEXITCODE -eq 0) {
    Write-Host "SUCCESS! https://github.com/ShakthiRithanya/course-registeration" -ForegroundColor Green
}
else {
    Write-Host "Push failed. Check credentials or run: git push --force origin main" -ForegroundColor Red
}
