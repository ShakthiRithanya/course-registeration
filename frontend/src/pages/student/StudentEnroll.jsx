import { useState, useMemo } from 'react';
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import axios from 'axios';
import { motion } from 'framer-motion';

import { Check, Info, AlertTriangle, Send } from 'lucide-react';

const StudentEnroll = ({ user }) => {
    const queryClient = useQueryClient();
    const [selected, setSelected] = useState({}); // { courseId: facultyId }
    const [error, setError] = useState('');
    const [success, setSuccess] = useState('');

    const { data: courses = [], isLoading } = useQuery({
        queryKey: ['enrollable', user.user_id],
        queryFn: () => axios.get(`/api/student/enrollable/${user.user_id}`).then(res => res.data)
    });

    const totalCredits = useMemo(() => {
        return Object.keys(selected).reduce((acc, courseId) => {
            const course = courses.find(c => c.id === courseId);
            return acc + (course?.credits || 0);
        }, 0);
    }, [selected, courses]);

    const enrollMutation = useMutation({
        mutationFn: (payload) => axios.post('/api/student/enroll', payload),
        onSuccess: (res) => {
            setSuccess('Enrollment successful!');
            setSelected({});
            queryClient.invalidateQueries(['enrolled', user.user_id]);
        },
        onError: (err) => {
            setError(err.response?.data?.detail || 'Enrollment failed.');
        }
    });

    const toggleCourse = (courseId, facultyId) => {
        setError('');
        setSuccess('');
        setSelected(prev => {
            const next = { ...prev };
            if (next[courseId] === facultyId) {
                delete next[courseId];
            } else {
                next[courseId] = facultyId;
            }
            return next;
        });
    };

    const handleEnroll = () => {
        if (totalCredits < 20) {
            setError('Minimum 20 credits required to submit.');
            return;
        }
        const payload = {
            student_id: user.user_id,
            selected_courses: Object.entries(selected).map(([cId, fId]) => ({
                course_id: cId,
                faculty_id: fId
            }))
        };
        enrollMutation.mutate(payload);
    };

    if (isLoading) return <div className="animate-pulse">Loading courses...</div>;

    return (
        <div className="space-y-6">
            <div className="bg-white p-6 rounded-2xl shadow-sm border border-gray-100 flex items-center justify-between">
                <div>
                    <h3 className="text-lg font-bold text-gray-800">Enrollment Portal</h3>
                    <p className="text-sm text-gray-500">Degree: B.Tech CSE | Year 2 | Semester 3</p>
                </div>
                <div className="text-right">
                    <p className="text-sm font-medium text-gray-400 mb-1">Total Credits</p>
                    <div className="flex items-center gap-3">
                        <span className={`text-2xl font-bold ${totalCredits >= 20 ? 'text-green-600' : 'text-orange-500'}`}>
                            {totalCredits}
                        </span>
                        <div className="w-32 h-2 bg-gray-100 rounded-full overflow-hidden">
                            <motion.div
                                className={`h-full ${totalCredits >= 20 ? 'bg-green-500' : 'bg-orange-500'}`}
                                animate={{ width: `${Math.min((totalCredits / 20) * 100, 100)}%` }}
                                transition={{ type: 'spring', stiffness: 300, damping: 30 }}
                            />
                        </div>
                        <span className="text-xs text-gray-400">/ 20 min</span>
                    </div>
                </div>
            </div>

            {error && (
                <motion.div
                    initial={{ opacity: 0, x: -10 }}
                    animate={{ opacity: 1, x: 0 }}
                    className="bg-red-50 border border-red-100 p-4 rounded-xl flex items-center gap-3 text-red-600"
                >
                    <AlertTriangle className="w-5 h-5" />
                    <p className="text-sm font-medium">{error}</p>
                </motion.div>
            )}

            {success && (
                <motion.div
                    initial={{ opacity: 0, x: -10 }}
                    animate={{ opacity: 1, x: 0 }}
                    className="bg-green-50 border border-green-100 p-4 rounded-xl flex items-center gap-3 text-green-600"
                >
                    <Check className="w-5 h-5" />
                    <p className="text-sm font-medium">{success}</p>
                </motion.div>
            )}

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
                {courses.map(course => (
                    <motion.div
                        key={course.id}
                        whileHover={{ y: -2 }}
                        whileTap={{ scale: 0.99 }}
                        className={`p-5 rounded-2xl border-2 transition-all cursor-pointer bg-white
              ${selected[course.id] ? 'border-primary-500 shadow-lg shadow-primary-500/10' : 'border-gray-50 hover:border-gray-200'}
            `}
                    >
                        <div className="flex justify-between items-start mb-4">
                            <div>
                                <h4 className="font-bold text-gray-800">{course.name}</h4>
                                <p className="text-xs text-gray-500">{course.id} | {course.credits} Credits</p>
                            </div>
                            <div className="text-right">
                                <span className="text-xs font-semibold text-gray-400 block mb-1">Seats</span>
                                <span className={`text-sm font-bold ${course.enrolled_count >= course.max_enroll ? 'text-red-500' : 'text-green-600'}`}>
                                    {course.enrolled_count}/{course.max_enroll}
                                </span>
                            </div>
                        </div>

                        <div className="space-y-2">
                            <p className="text-xs font-semibold text-gray-400 uppercase tracking-wider">Select Faculty</p>
                            <div className="flex flex-wrap gap-2">
                                {course.faculties.map(fac => (
                                    <button
                                        key={fac.id}
                                        disabled={course.enrolled_count >= course.max_enroll}
                                        onClick={(e) => { e.stopPropagation(); toggleCourse(course.id, fac.id); }}
                                        className={`px-3 py-2 rounded-lg text-xs font-medium border transition-all
                      ${selected[course.id] === fac.id
                                                ? 'bg-primary-600 text-white border-primary-600 shadow-md shadow-primary-500/20'
                                                : 'bg-gray-50 text-gray-600 border-gray-100 hover:bg-gray-100'}
                      ${course.enrolled_count >= course.max_enroll ? 'opacity-50 cursor-not-allowed' : ''}
                    `}
                                    >
                                        {fac.name}
                                    </button>
                                ))}
                            </div>
                        </div>
                    </motion.div>
                ))}
            </div>

            <div className="fixed bottom-8 right-8">
                <button
                    onClick={handleEnroll}
                    disabled={totalCredits < 20 || enrollMutation.isLoading}
                    className={`
            btn-primary flex items-center gap-2 px-8 py-4 text-lg
            ${totalCredits < 20 ? 'opacity-50 cursor-not-allowed' : ''}
          `}
                >
                    {enrollMutation.isLoading ? (
                        <div className="w-6 h-6 border-2 border-white/30 border-t-white rounded-full animate-spin" />
                    ) : (
                        <>
                            <Send className="w-5 h-5" />
                            <span>Submit Enrollment</span>
                        </>
                    )}
                </button>
            </div>
        </div>
    );
};

export default StudentEnroll;

// GET /api/student/enrollable
