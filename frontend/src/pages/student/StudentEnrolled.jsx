import { useQuery } from '@tanstack/react-query';
import axios from 'axios';

import { AlertCircle, CheckCircle2, BookOpen } from 'lucide-react';

const StudentEnrolled = ({ user }) => {
    const { data: enrollments = [], isLoading } = useQuery({
        queryKey: ['enrolled', user.user_id],
        queryFn: () => axios.get(`/api/student/enrolled/${user.user_id}`).then(res => res.data)
    });

    const backlogs = enrollments.filter(e => e.status === 'backlog');
    const active = enrollments.filter(e => e.status === 'enrolled');
    const completed = enrollments.filter(e => e.status === 'completed');

    if (isLoading) return <div>Loading course history...</div>;

    return (
        <div className="space-y-8">
            {/* Backlogs Section */}
            {backlogs.length > 0 && (
                <section>
                    <div className="flex items-center gap-2 mb-4 text-red-600">
                        <AlertCircle className="w-5 h-5" />
                        <h3 className="text-xl font-bold">Backlogs (F Grades)</h3>
                    </div>
                    <div className="bg-white rounded-2xl shadow-sm border border-red-100 overflow-hidden">
                        <table className="w-full text-left">
                            <thead className="bg-red-50 text-red-700 text-sm">
                                <tr>
                                    <th className="px-6 py-4">Course</th>
                                    <th className="px-6 py-4">Faculty</th>
                                    <th className="px-6 py-4">Year/Sem</th>
                                    <th className="px-6 py-4">Grade</th>
                                </tr>
                            </thead>
                            <tbody className="divide-y divide-red-50">
                                {backlogs.map(e => (
                                    <tr key={e.enrollment_id} className="hover:bg-red-50/30 transition-colors">
                                        <td className="px-6 py-4 font-semibold text-gray-800">{e.course_name}</td>
                                        <td className="px-6 py-4 text-gray-600">{e.faculty_name}</td>
                                        <td className="px-6 py-4 text-gray-600">Sem {e.sem}</td>
                                        <td className="px-6 py-4 text-red-600 font-bold">F (0.0)</td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                </section>
            )}

            {/* Active Enrollments */}
            <section>
                <div className="flex items-center gap-2 mb-4 text-primary-600">
                    <BookOpen className="w-5 h-5" />
                    <h3 className="text-xl font-bold">Current Enrollments</h3>
                </div>
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                    {active.map(e => (
                        <div
                            key={e.enrollment_id}
                            whileHover={{ scale: 1.02 }}
                            className="glass-card p-5 rounded-2xl border-l-4 border-l-primary-500"
                        >
                            <h4 className="font-bold text-gray-800 mb-1">{e.course_name}</h4>
                            <p className="text-xs text-gray-500 mb-3">{e.course_id} • {e.credits} Credits</p>
                            <div className="flex items-center gap-2 text-sm text-gray-600">
                                <div className="w-6 h-6 bg-gray-100 rounded-full flex items-center justify-center text-[10px] font-bold">
                                    {e.faculty_name.charAt(0)}
                                </div>
                                <span>{e.faculty_name}</span>
                            </div>
                        </div>
                    ))}
                    {active.length === 0 && (
                        <div className="col-span-full py-12 flex flex-col items-center justify-center text-gray-400 bg-white rounded-2xl border-2 border-dashed border-gray-100">
                            <BookOpen className="w-12 h-12 mb-3 opacity-20" />
                            <p>No active enrollments for this semester.</p>
                        </div>
                    )}
                </div>
            </section>

            {/* Completed Courses */}
            {completed.length > 0 && (
                <section>
                    <div className="flex items-center gap-2 mb-4 text-green-600">
                        <CheckCircle2 className="w-5 h-5" />
                        <h3 className="text-xl font-bold">Completed Courses</h3>
                    </div>
                    <div className="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden text-sm">
                        {/* Simple list or accordion */}
                        {completed.map(e => (
                            <div key={e.enrollment_id} className="flex items-center justify-between p-4 hover:bg-gray-50 border-b border-gray-50 last:border-0 transition-colors">
                                <div>
                                    <p className="font-semibold text-gray-800">{e.course_name}</p>
                                    <p className="text-xs text-gray-500">{e.faculty_name} • Sem {e.sem}</p>
                                </div>
                                <div className="text-right">
                                    <p className="font-bold text-green-600">{e.grade.toFixed(1)} / 4.0</p>
                                    <p className="text-[10px] text-gray-400 uppercase tracking-widest font-bold">Passed</p>
                                </div>
                            </div>
                        ))}
                    </div>
                </section>
            )}
        </div>
    );
};

export default StudentEnrolled;

// GET /api/student/enrolled
