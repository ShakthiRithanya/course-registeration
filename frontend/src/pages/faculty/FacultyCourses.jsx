import { useState } from 'react';
import { useQuery } from '@tanstack/react-query';
import axios from 'axios';
import { motion, AnimatePresence } from 'framer-motion';
import { Users, Info, ChevronRight, X } from 'lucide-react';

const FacultyCourses = ({ user }) => {
    const [selectedCourse, setSelectedCourse] = useState(null);

    const { data: courses = [], isLoading } = useQuery({
        queryKey: ['faculty-courses', user.user_id],
        queryFn: () => axios.get(`/api/faculty/courses/${user.user_id}`).then(res => res.data)
    });

    const { data: students = [], isLoading: loadingStudents } = useQuery({
        queryKey: ['course-students', selectedCourse?.id],
        queryFn: () => axios.get(`/api/course/${selectedCourse.id}/students`).then(res => res.data),
        enabled: !!selectedCourse
    });

    if (isLoading) return <div>Loading courses...</div>;

    return (
        <div className="space-y-6">
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                {courses.map(course => (
                    <motion.div
                        key={course.id}
                        whileHover={{ y: -4 }}
                        className="glass-card p-6 rounded-2xl cursor-pointer"
                        onClick={() => setSelectedCourse(course)}
                    >
                        <div className="flex justify-between items-start mb-4">
                            <div className="p-3 bg-primary-50 text-primary-600 rounded-xl">
                                <Users className="w-6 h-6" />
                            </div>
                            <span className="text-xs font-bold text-gray-400 bg-gray-50 px-2 py-1 rounded">Sem {course.sem}</span>
                        </div>
                        <h3 className="text-lg font-bold text-gray-800 mb-1">{course.name}</h3>
                        <p className="text-sm text-gray-500 mb-4">{course.id}</p>

                        <div className="flex items-center justify-between pt-4 border-t border-gray-50">
                            <div>
                                <p className="text-[10px] text-gray-400 uppercase font-bold tracking-wider">Students</p>
                                <p className="text-lg font-bold text-gray-700">{course.enrolled_count} / {course.max_enroll}</p>
                            </div>
                            <ChevronRight className="w-5 h-5 text-gray-300" />
                        </div>
                    </motion.div>
                ))}
            </div>

            {/* Student List Modal */}
            <AnimatePresence>
                {selectedCourse && (
                    <motion.div
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        exit={{ opacity: 0 }}
                        className="fixed inset-0 bg-black/20 backdrop-blur-sm z-50 flex items-center justify-center p-4"
                        onClick={() => setSelectedCourse(null)}
                    >
                        <motion.div
                            initial={{ scale: 0.95, opacity: 0 }}
                            animate={{ scale: 1, opacity: 1 }}
                            exit={{ scale: 0.95, opacity: 0 }}
                            className="bg-white w-full max-w-2xl rounded-2xl shadow-2xl overflow-hidden"
                            onClick={e => e.stopPropagation()}
                        >
                            <div className="p-6 border-b border-gray-100 flex items-center justify-between bg-primary-600 text-white">
                                <div>
                                    <h3 className="text-xl font-bold">{selectedCourse.name}</h3>
                                    <p className="text-sm text-white/70">Enrolled Students List</p>
                                </div>
                                <button
                                    onClick={() => setSelectedCourse(null)}
                                    className="p-2 hover:bg-white/10 rounded-lg transition-colors"
                                >
                                    <X className="w-6 h-6" />
                                </button>
                            </div>

                            <div className="max-h-[60vh] overflow-y-auto">
                                <table className="w-full text-left">
                                    <thead className="bg-gray-50 text-gray-400 text-[10px] uppercase font-bold tracking-widest">
                                        <tr>
                                            <th className="px-6 py-4">Student</th>
                                            <th className="px-6 py-4">ID</th>
                                            <th className="px-6 py-4">Dept/Year</th>
                                        </tr>
                                    </thead>
                                    <tbody className="divide-y divide-gray-50">
                                        {loadingStudents ? (
                                            <tr><td colSpan="3" className="p-8 text-center text-gray-400">Loading student list...</td></tr>
                                        ) : students.map(student => (
                                            <tr key={student.id} className="hover:bg-gray-50 transition-colors">
                                                <td className="px-6 py-4">
                                                    <div className="flex items-center gap-3">
                                                        <img src={student.photo_url} className="w-8 h-8 rounded-full" />
                                                        <span className="font-semibold text-gray-700">{student.name}</span>
                                                    </div>
                                                </td>
                                                <td className="px-6 py-4 text-sm text-gray-500">{student.id}</td>
                                                <td className="px-6 py-4 text-sm text-gray-500">{student.dept} • {student.year}</td>
                                            </tr>
                                        ))}
                                        {!loadingStudents && students.length === 0 && (
                                            <tr><td colSpan="3" className="p-8 text-center text-gray-400 italic">No students enrolled yet.</td></tr>
                                        )}
                                    </tbody>
                                </table>
                            </div>
                        </motion.div>
                    </motion.div>
                )}
            </AnimatePresence>
        </div>
    );
};

export default FacultyCourses;

// GET /api/faculty/courses
