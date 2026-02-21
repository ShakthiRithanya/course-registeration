import { motion } from 'framer-motion';
import { Routes, Route, Navigate } from 'react-router-dom';
import Sidebar from '../../components/Sidebar';
import FacultyProfile from './FacultyProfile';
import FacultyCourses from './FacultyCourses';
import FacultyBacklogs from './FacultyBacklogs';


const FacultyDashboard = ({ user, logout }) => {
    return (
        <div className="flex min-h-screen bg-slate-50">
            <Sidebar role="faculty" user={user} logout={logout} />

            <main className="flex-1 ml-64 p-8">
                <header className="mb-8">
                    <h2 className="text-3xl font-bold text-slate-800">Welcome, {user.name}</h2>
                    <p className="text-slate-500">{user.designation} • {user.dept} Department</p>
                </header>

                <motion.div
                    initial={{ opacity: 0, x: 20 }}
                    animate={{ opacity: 1, x: 0 }}
                    transition={{ duration: 0.3 }}
                >
                    <Routes>
                        <Route path="profile" element={<FacultyProfile user={user} />} />
                        <Route path="courses" element={<FacultyCourses user={user} />} />
                        <Route path="backlogs" element={<FacultyBacklogs user={user} />} />
                        <Route path="/" element={<Navigate to="courses" />} />
                    </Routes>
                </motion.div>
            </main>
        </div>
    );
};

export default FacultyDashboard;
