import { motion } from 'framer-motion';
import { useState } from 'react';
import { Routes, Route, Navigate, useNavigate } from 'react-router-dom';
import Sidebar from '../../components/Sidebar';
import AdminOverview from './AdminOverview';
import AdminDegrees from './AdminDegrees';
import AdminFaculty from './AdminFaculty';
import AdminAllocation from './AdminAllocation';


const AdminDashboard = ({ user, logout }) => {
    return (
        <div className="flex min-h-screen bg-slate-50">
            <Sidebar role="admin" user={user} logout={logout} />

            <main className="flex-1 ml-64 p-8">
                <header className="mb-8 flex justify-between items-end">
                    <div>
                        <h2 className="text-3xl font-bold text-slate-800">Admin Console</h2>
                        <p className="text-slate-500">System Management & Resource Allocation</p>
                    </div>
                    <div className="flex gap-2">
                        <span className="px-3 py-1 bg-blue-100 text-blue-700 rounded-full text-xs font-bold border border-blue-200">
                            System Live
                        </span>
                    </div>
                </header>

                <motion.div
                    initial={{ opacity: 0, y: 10 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.3 }}
                >
                    <Routes>
                        <Route path="/" element={<AdminOverview />} />
                        <Route path="degrees" element={<AdminDegrees />} />
                        <Route path="faculty" element={<AdminFaculty />} />
                        <Route path="allocation" element={<AdminAllocation />} />
                    </Routes>
                </motion.div>
            </main>
        </div>
    );
};

export default AdminDashboard;
