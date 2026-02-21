import { Routes, Route, Navigate } from 'react-router-dom';
import Sidebar from '../../components/Sidebar';
import StudentProfile from './StudentProfile';
import StudentEnroll from './StudentEnroll';
import StudentEnrolled from './StudentEnrolled';


const StudentDashboard = ({ user, logout }) => {
    return (
        <div className="flex min-h-screen bg-slate-50">
            <Sidebar role="student" user={user} logout={logout} />

            <main className="flex-1 ml-64 p-8">
                <header className="mb-8">
                    <h2 className="text-3xl font-bold text-slate-800">Welcome, {user.name}</h2>
                    <p className="text-slate-500">Manage your courses and enrollment status.</p>
                </header>

                <div
                    initial={{ opacity: 0, x: 20 }}
                    animate={{ opacity: 1, x: 0 }}
                    transition={{ duration: 0.3 }}
                >
                    <Routes>
                        <Route path="profile" element={<StudentProfile user={user} />} />
                        <Route path="enroll" element={<StudentEnroll user={user} />} />
                        <Route path="enrolled" element={<StudentEnrolled user={user} />} />
                        <Route path="/" element={<Navigate to="profile" />} />
                    </Routes>
                </div>
            </main>
        </div>
    );
};

export default StudentDashboard;

// student dashboard
