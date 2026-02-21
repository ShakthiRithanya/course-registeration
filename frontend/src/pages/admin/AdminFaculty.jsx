import { useState } from 'react';
import { useQuery } from '@tanstack/react-query';
import axios from 'axios';
import { motion, AnimatePresence } from 'framer-motion';
import { Users, Mail, Book, X, Settings } from 'lucide-react';
import { useNavigate } from 'react-router-dom';

const AdminFaculty = () => {
    const navigate = useNavigate();
    const [selectedFaculty, setSelectedFaculty] = useState(null);
    const { data: faculty = [], isLoading } = useQuery({
        queryKey: ['admin-faculty'],
        queryFn: () => axios.get('/api/admin/faculty').then(res => res.data)
    });

    const { data: facultyCourses = [], isLoading: loadingCourses } = useQuery({
        queryKey: ['admin-faculty-courses', selectedFaculty?.id],
        queryFn: () => axios.get(`/api/faculty/courses/${selectedFaculty.id}`).then(res => res.data),
        enabled: !!selectedFaculty
    });

    return (
        <div className="space-y-6">
            <div className="flex items-center justify-between mb-8">
                <div>
                    <h3 className="text-2xl font-bold text-gray-800">Faculty Management</h3>
                    <p className="text-sm text-gray-500">View and manage college professors and heads.</p>
                </div>
                <div className="bg-white px-4 py-2 rounded-xl border border-gray-100 shadow-sm flex items-center gap-2">
                    <Users className="w-4 h-4 text-primary-500" />
                    <span className="text-sm font-bold text-gray-700">{faculty.length} Total</span>
                </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                {isLoading ? (
                    <div>Loading faculty members...</div>
                ) : faculty.map((f) => (
                    <motion.div
                        key={f.id}
                        whileHover={{ y: -2 }}
                        whileTap={{ scale: 0.98 }}
                        className="glass-card p-6 rounded-2xl"
                    >
                        <div className="flex items-center gap-4 mb-6">
                            <img src={f.photo_url} className="w-16 h-16 rounded-2xl shadow-md" />
                            <div>
                                <h4 className="font-bold text-gray-800 leading-tight">{f.name}</h4>
                                <p className="text-xs text-primary-600 font-semibold">{f.designation}</p>
                                <p className="text-[10px] text-gray-400 uppercase font-bold mt-1 tracking-widest">{f.id}</p>
                            </div>
                        </div>

                        <div className="space-y-3 pt-4 border-t border-gray-50">
                            <div className="flex items-center gap-3 text-sm text-gray-500">
                                <Mail className="w-4 h-4 text-gray-300" />
                                <span className="truncate">{f.email}</span>
                            </div>
                            <div className="flex items-center gap-3 text-sm text-gray-500">
                                <Book className="w-4 h-4 text-gray-300" />
                                <span>{f.dept} Department</span>
                            </div>
                        </div>

                        <button
                            onClick={() => setSelectedFaculty(f)}
                            className="w-full mt-6 py-2 bg-gray-50 hover:bg-gray-100 text-gray-600 rounded-xl text-xs font-bold transition-all"
                        >
                            Manage Courses
                        </button>
                    </motion.div>
                ))}
            </div>

            <AnimatePresence>
                {selectedFaculty && (
                    <motion.div
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        exit={{ opacity: 0 }}
                        className="fixed inset-0 bg-black/40 backdrop-blur-sm z-50 flex items-center justify-center p-4"
                        onClick={() => setSelectedFaculty(null)}
                    >
                        <motion.div
                            initial={{ scale: 0.9, opacity: 0 }}
                            animate={{ scale: 1, opacity: 1 }}
                            exit={{ scale: 0.9, opacity: 0 }}
                            className="bg-white w-full max-w-md rounded-3xl shadow-2xl overflow-hidden"
                            onClick={e => e.stopPropagation()}
                        >
                            <div className="p-6 border-b border-gray-100 flex items-center justify-between">
                                <div className="flex items-center gap-3">
                                    <img src={selectedFaculty.photo_url || `https://ui-avatars.com/api/?name=${selectedFaculty.name}`} className="w-10 h-10 rounded-full" />
                                    <div>
                                        <h4 className="font-bold text-gray-800">{selectedFaculty.name}</h4>
                                        <p className="text-xs text-gray-500">Assigned Courses</p>
                                    </div>
                                </div>
                                <button onClick={() => setSelectedFaculty(null)} className="p-2 hover:bg-gray-100 rounded-xl transition-colors">
                                    <X className="w-6 h-6 text-gray-400" />
                                </button>
                            </div>

                            <div className="p-6 space-y-3">
                                {loadingCourses ? (
                                    <div className="text-center py-6 text-gray-400">Loading courses...</div>
                                ) : facultyCourses.map(course => (
                                    <div key={course.id} className="flex items-center justify-between p-3 bg-gray-50 rounded-xl">
                                        <div>
                                            <p className="text-sm font-bold text-gray-700">{course.name}</p>
                                            <p className="text-[10px] text-gray-400 font-bold uppercase">{course.id}</p>
                                        </div>
                                        <button className="text-red-400 hover:text-red-600 p-2 transition-colors">
                                            <X className="w-4 h-4" />
                                        </button>
                                    </div>
                                ))}
                                {!loadingCourses && facultyCourses.length === 0 && (
                                    <div className="text-center py-6 text-gray-400 italic text-sm">No courses assigned.</div>
                                )}

                                <button
                                    onClick={() => navigate('/admin/allocation')}
                                    className="w-full mt-4 flex items-center justify-center gap-2 py-3 bg-primary-600 text-white rounded-2xl text-sm font-bold hover:bg-primary-700 transition-all shadow-lg shadow-primary-500/20"
                                >
                                    <Settings className="w-4 h-4" />
                                    <span>Allocate New Course</span>
                                </button>
                            </div>
                        </motion.div>
                    </motion.div>
                )}
            </AnimatePresence>
        </div>
    );
};

export default AdminFaculty;

// GET /api/admin/faculty

// manage courses modal
