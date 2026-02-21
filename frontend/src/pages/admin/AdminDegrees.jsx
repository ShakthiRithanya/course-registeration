import { useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { useQuery } from '@tanstack/react-query';
import axios from 'axios';
import { motion, AnimatePresence } from 'framer-motion';
import { GraduationCap, ArrowLeft, Plus, X, BookOpen } from 'lucide-react';

const AdminDegrees = () => {
    const location = useLocation();
    const navigate = useNavigate();
    const programType = location.state?.type || 'UG';
    const [selectedDegree, setSelectedDegree] = useState(null);
    const [showAddModal, setShowAddModal] = useState(false);
    const [showHistoryModal, setShowHistoryModal] = useState(null);

    const { data: degrees = [], isLoading } = useQuery({
        queryKey: ['admin-degrees', programType],
        queryFn: () => axios.get(`/api/admin/degrees?type=${programType}`).then(res => res.data)
    });

    const { data: degreeCourses = [], isLoading: loadingCourses } = useQuery({
        queryKey: ['admin-degree-courses', selectedDegree?.id],
        queryFn: () => axios.get(`/api/admin/degree/${selectedDegree.id}/courses`).then(res => res.data),
        enabled: !!selectedDegree
    });

    const { data: history = {}, isLoading: loadingHistory } = useQuery({
        queryKey: ['admin-degree-history', showHistoryModal?.id],
        queryFn: () => axios.get(`/api/admin/degree/${showHistoryModal.id}/history`).then(res => res.data),
        enabled: !!showHistoryModal
    });

    return (
        <div className="space-y-6">
            <div className="flex items-center justify-between">
                <button
                    onClick={() => navigate('/admin')}
                    className="flex items-center gap-2 text-sm text-gray-400 hover:text-gray-600 transition-colors"
                >
                    <ArrowLeft className="w-4 h-4" />
                    <span>Back to Overview</span>
                </button>
                <button
                    onClick={() => setShowAddModal(true)}
                    className="btn-primary flex items-center gap-2 text-sm py-2 px-4"
                >
                    <Plus className="w-4 h-4" />
                    <span>Add Degree</span>
                </button>
            </div>

            <div className="flex items-end gap-3 mb-8">
                <h3 className="text-2xl font-bold text-gray-800">{programType} Programs</h3>
                <p className="text-gray-400 mb-1 text-sm font-medium">Available Degrees</p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {isLoading ? (
                    <div className="animate-pulse glass-card p-12 col-span-full text-center text-gray-400">Loading degrees...</div>
                ) : degrees.length > 0 ? (
                    degrees.map((degree) => (
                        <motion.div
                            key={degree.id}
                            whileHover={{ y: -4 }}
                            whileTap={{ scale: 0.98 }}
                            className="glass-card p-6 rounded-2xl border-b-4 border-b-primary-500"
                        >
                            <div className="flex justify-between items-start mb-6">
                                <div className="w-12 h-12 bg-primary-50 text-primary-600 rounded-xl flex items-center justify-center">
                                    <GraduationCap className="w-6 h-6" />
                                </div>
                                <span className="text-[10px] uppercase font-bold text-gray-300 tracking-widest">{degree.id}</span>
                            </div>

                            <h4 className="text-lg font-bold text-gray-800 mb-2">{degree.name}</h4>
                            <p className="text-sm text-gray-500 mb-6 font-medium">Department: Professional Studies</p>

                            <div className="flex gap-2">
                                <button
                                    onClick={() => setShowHistoryModal(degree)}
                                    className="flex-1 px-3 py-2 bg-gray-50 text-gray-600 rounded-lg text-xs font-bold hover:bg-gray-100 transition-colors"
                                >
                                    History
                                </button>
                                <button
                                    onClick={() => setSelectedDegree(degree)}
                                    className="flex-1 px-3 py-2 bg-primary-50 text-primary-600 rounded-lg text-xs font-bold hover:bg-primary-100 transition-colors"
                                >
                                    Courses
                                </button>
                            </div>
                        </motion.div>
                    ))
                ) : (
                    <div className="col-span-full p-20 text-center glass-card">
                        <p className="text-gray-400 font-medium italic">No {programType} programs found in the system.</p>
                    </div>
                )}
            </div>

            <AnimatePresence>
                {selectedDegree && (
                    <motion.div
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        exit={{ opacity: 0 }}
                        className="fixed inset-0 bg-black/40 backdrop-blur-sm z-50 flex items-center justify-center p-4"
                        onClick={() => setSelectedDegree(null)}
                    >
                        {/* ... existing modal ... */}
                        <motion.div
                            initial={{ scale: 0.9, opacity: 0 }}
                            animate={{ scale: 1, opacity: 1 }}
                            exit={{ scale: 0.9, opacity: 0 }}
                            className="bg-white w-full max-w-2xl rounded-3xl shadow-2xl overflow-hidden"
                            onClick={e => e.stopPropagation()}
                        >
                            <div className="p-6 border-b border-gray-100 flex items-center justify-between bg-gray-50">
                                <div>
                                    <h4 className="text-xl font-bold text-gray-800">{selectedDegree.name}</h4>
                                    <p className="text-sm text-gray-500">Course List</p>
                                </div>
                                <button onClick={() => setSelectedDegree(null)} className="p-2 hover:bg-gray-200 rounded-xl transition-colors">
                                    <X className="w-6 h-6 text-gray-400" />
                                </button>
                            </div>

                            <div className="p-6 max-h-[60vh] overflow-y-auto">
                                <div className="space-y-3">
                                    {loadingCourses ? (
                                        <div className="text-center py-12 text-gray-400">Loading courses...</div>
                                    ) : degreeCourses.map(course => (
                                        <div key={course.id} className="flex items-center justify-between p-4 bg-gray-50 rounded-2xl hover:bg-gray-100 transition-colors">
                                            <div className="flex items-center gap-4">
                                                <div className="w-10 h-10 bg-white rounded-xl flex items-center justify-center shadow-sm">
                                                    <BookOpen className="w-5 h-5 text-primary-500" />
                                                </div>
                                                <div>
                                                    <p className="font-bold text-gray-800">{course.name}</p>
                                                    <p className="text-xs text-gray-500">Sem {course.sem} | {course.credits} Credits</p>
                                                </div>
                                            </div>
                                            <div className="text-right">
                                                <p className="text-xs font-bold text-gray-400 uppercase tracking-widest">{course.id}</p>
                                            </div>
                                        </div>
                                    ))}
                                    {!loadingCourses && degreeCourses.length === 0 && (
                                        <div className="text-center py-12 text-gray-400 italic text-sm">No courses found for this degree.</div>
                                    )}
                                </div>
                            </div>
                        </motion.div>
                    </motion.div>
                )}

                {/* History Modal */}
                {showHistoryModal && (
                    <motion.div
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        exit={{ opacity: 0 }}
                        className="fixed inset-0 bg-black/40 backdrop-blur-sm z-50 flex items-center justify-center p-4"
                        onClick={() => setShowHistoryModal(null)}
                    >
                        <motion.div
                            initial={{ scale: 0.9, opacity: 0 }}
                            animate={{ scale: 1, opacity: 1 }}
                            exit={{ scale: 0.9, opacity: 0 }}
                            className="bg-white w-full max-w-md rounded-3xl shadow-2xl overflow-hidden"
                            onClick={e => e.stopPropagation()}
                        >
                            <div className="p-6 border-b border-gray-100 flex items-center justify-between">
                                <h4 className="text-xl font-bold text-gray-800">Academic History</h4>
                                <button onClick={() => setShowHistoryModal(null)} className="p-2 hover:bg-gray-100 rounded-xl">
                                    <X className="w-6 h-6 text-gray-400" />
                                </button>
                            </div>
                            <div className="p-8 text-center bg-gray-50">
                                <div className="inline-flex p-4 bg-primary-100 text-primary-600 rounded-2xl mb-4">
                                    <GraduationCap className="w-10 h-10" />
                                </div>
                                <h3 className="text-2xl font-bold text-gray-800 mb-1">{showHistoryModal.name}</h3>
                                <p className="text-sm text-gray-500 mb-8">{showHistoryModal.id}</p>

                                <div className="grid grid-cols-2 gap-4">
                                    <div className="bg-white p-4 rounded-2xl shadow-sm border border-gray-100">
                                        <p className="text-3xl font-bold text-primary-600">{loadingHistory ? '...' : history.total_completions}</p>
                                        <p className="text-[10px] text-gray-400 font-bold uppercase tracking-widest mt-1">Total Grads</p>
                                    </div>
                                    <div className="bg-white p-4 rounded-2xl shadow-sm border border-gray-100">
                                        <p className="text-3xl font-bold text-orange-500">{loadingHistory ? '...' : history.avg_gpa}</p>
                                        <p className="text-[10px] text-gray-400 font-bold uppercase tracking-widest mt-1">Avg. GPA</p>
                                    </div>
                                </div>
                            </div>
                            <div className="p-6">
                                <button
                                    onClick={() => setShowHistoryModal(null)}
                                    className="w-full py-4 bg-gray-800 text-white rounded-2xl text-sm font-bold shadow-xl hover:bg-gray-700 transition-all"
                                >
                                    Close Performance Overview
                                </button>
                            </div>
                        </motion.div>
                    </motion.div>
                )}

                {showAddModal && (
                    <motion.div
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        exit={{ opacity: 0 }}
                        className="fixed inset-0 bg-black/40 backdrop-blur-sm z-50 flex items-center justify-center p-4"
                        onClick={() => setShowAddModal(false)}
                    >
                        <motion.div
                            initial={{ scale: 0.9, opacity: 0 }}
                            animate={{ scale: 1, opacity: 1 }}
                            exit={{ scale: 0.9, opacity: 0 }}
                            className="bg-white w-full max-w-md rounded-3xl shadow-2xl overflow-hidden"
                            onClick={e => e.stopPropagation()}
                        >
                            <div className="p-6 border-b border-gray-100 flex items-center justify-between">
                                <h4 className="text-xl font-bold text-gray-800">Add New Program</h4>
                                <button onClick={() => setShowAddModal(false)} className="p-2 hover:bg-gray-100 rounded-xl">
                                    <X className="w-6 h-6 text-gray-400" />
                                </button>
                            </div>
                            <form className="p-6 space-y-4" onSubmit={(e) => { e.preventDefault(); setShowAddModal(false); }}>
                                <div>
                                    <label className="block text-xs font-bold text-gray-400 uppercase mb-2">Program Name</label>
                                    <input type="text" className="w-full bg-gray-50 border-none rounded-xl p-3 text-sm focus:ring-2 focus:ring-primary-500" placeholder="e.g. B.Tech Artificial Intelligence" required />
                                </div>
                                <div>
                                    <label className="block text-xs font-bold text-gray-400 uppercase mb-2">Program ID</label>
                                    <input type="text" className="w-full bg-gray-50 border-none rounded-xl p-3 text-sm focus:ring-2 focus:ring-primary-500" placeholder="e.g. deg_ug_ai" required />
                                </div>
                                <button type="submit" className="w-full py-3 bg-primary-600 text-white rounded-2xl text-sm font-bold shadow-lg shadow-primary-500/20">
                                    Create Program
                                </button>
                            </form>
                        </motion.div>
                    </motion.div>
                )}
            </AnimatePresence>
        </div>
    );
};

export default AdminDegrees;

// degree list with filter

// view classes modal

// courses modal

// history GPA modal
