import { useQuery } from '@tanstack/react-query';
import axios from 'axios';
import { motion } from 'framer-motion';

import { AlertCircle, FileText } from 'lucide-react';

const FacultyBacklogs = ({ user }) => {
    const { data: backlogs = [], isLoading } = useQuery({
        queryKey: ['faculty-backlogs', user.user_id],
        queryFn: () => axios.get(`/api/faculty/backlogs/${user.user_id}`).then(res => res.data)
    });

    if (isLoading) return <div>Loading backlog reports...</div>;

    return (
        <div className="space-y-6">
            <div className="bg-white p-6 rounded-2xl shadow-sm border border-red-100 flex items-center gap-4">
                <div className="p-3 bg-red-50 text-red-600 rounded-xl">
                    <AlertCircle className="w-8 h-8" />
                </div>
                <div>
                    <h3 className="text-xl font-bold text-gray-800 tracking-tight">Backlog Monitoring</h3>
                    <p className="text-sm text-gray-500">Students with failing grades in your assigned courses.</p>
                </div>
            </div>

            <div className="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden">
                <table className="w-full text-left">
                    <thead className="bg-gray-50 text-gray-400 text-[10px] uppercase font-bold tracking-widest">
                        <tr>
                            <th className="px-6 py-4">Student Name</th>
                            <th className="px-6 py-4">Student ID</th>
                            <th className="px-6 py-4">Course</th>
                            <th className="px-6 py-4">Status</th>
                        </tr>
                    </thead>
                    <tbody className="divide-y divide-gray-50">
                        {backlogs.map((item, idx) => (
                            <motion.tr
                                key={idx}
                                initial={{ opacity: 0, y: 10 }}
                                animate={{ opacity: 1, y: 0 }}
                                transition={{ delay: idx * 0.05 }}
                                className="hover:bg-red-50/20 transition-colors"
                            >
                                <td className="px-6 py-4 font-semibold text-gray-700">{item.student_name}</td>
                                <td className="px-6 py-4 text-sm text-gray-500">{item.student_id}</td>
                                <td className="px-6 py-4 text-sm text-gray-500">{item.course_name}</td>
                                <td className="px-6 py-4">
                                    <span className="px-2 py-1 bg-red-100 text-red-700 rounded text-[10px] font-bold uppercase">
                                        Backlog (F)
                                    </span>
                                </td>
                            </motion.tr>
                        ))}
                        {backlogs.length === 0 && (
                            <tr>
                                <td colSpan="4" className="p-12 text-center text-gray-400 italic">
                                    No backlogs found in your courses. Great job!
                                </td>
                            </tr>
                        )}
                    </tbody>
                </table>
            </div>
        </div>
    );
};

export default FacultyBacklogs;
