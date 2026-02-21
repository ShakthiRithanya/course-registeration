import { Routes, Route, Navigate } from 'react-router-dom';
import { useState, useEffect } from 'react';
import Login from './pages/Login';
import StudentDashboard from './pages/student/StudentDashboard';
import FacultyDashboard from './pages/faculty/FacultyDashboard';
import AdminDashboard from './pages/admin/AdminDashboard';

function App() {
    const [user, setUser] = useState(null);

    useEffect(() => {
        try {
            const savedUser = localStorage.getItem('user');
            if (savedUser) {
                setUser(JSON.parse(savedUser));
            }
        } catch (e) {
            console.error("Auth init error", e);
        }
    }, []);

    const handleLogin = (userData) => {
        setUser(userData);
        localStorage.setItem('user', JSON.stringify(userData));
    };

    const logout = () => {
        setUser(null);
        localStorage.removeItem('user');
        localStorage.removeItem('token');
    };

    return (
        <Routes>
            <Route
                path="/login"
                element={user ? <Navigate to={`/${user.role}`} /> : <Login onLogin={handleLogin} />}
            />

            <Route
                path="/student/*"
                element={user?.role === 'student' ? <StudentDashboard user={user} logout={logout} /> : <Navigate to="/login" />}
            />

            <Route
                path="/faculty/*"
                element={user?.role === 'faculty' ? <FacultyDashboard user={user} logout={logout} /> : <Navigate to="/login" />}
            />

            <Route
                path="/admin/*"
                element={user?.role === 'admin' ? <AdminDashboard user={user} logout={logout} /> : <Navigate to="/login" />}
            />

            <Route path="/" element={<Navigate to="/login" />} />
        </Routes>
    );
}

export default App;
