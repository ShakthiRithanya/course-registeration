import sqlite3
import os

db_path = 'database.db'
if not os.path.exists(db_path):
    print("Database file not found!")
    exit(1)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Check student count
cursor.execute('SELECT COUNT(*) FROM user WHERE role = "student"')
student_count = cursor.fetchone()[0]

# Check enrollment count (total historic + faculty allocs)
cursor.execute('SELECT COUNT(*) FROM enrollment')
enrollment_count = cursor.fetchone()[0]

# Check history for a Year 3 student (AIDS009)
cursor.execute('SELECT DISTINCT sem FROM enrollment WHERE student_id = "AIDS009"')
aids009_sems = [row[0] for row in cursor.fetchall()]

# Check backlog status
cursor.execute('SELECT status, COUNT(*) FROM enrollment GROUP BY status')
status_counts = cursor.fetchall()

print(f"Total Students: {student_count}")
print(f"Total Enrollments (History): {enrollment_count}")
print(f"History Semesters for AIDS009 (Year 3): {sorted(aids009_sems)}")
print("Enrollment Status Breakdown:")
for status, count in status_counts:
    print(f"  - {status}: {count}")

conn.close()
