import { useNavigate } from 'react-router-dom';
import { useQuery } from '@tanstack/react-query';
import axios from 'axios';
import { BookOpen, GraduationCap, Zap, Activity } from 'lucide-react';
import { motion } from 'framer-motion';

const AdminOverview = () => {
    const navigate = useNavigate();

    const { data: stats = {} } = useQuery({
        queryKey: ['admin-stats'],
        queryFn: () => axios.get('/api/admin/stats').then(res => res.data)
    });

    const programs = [
        { id: 'ug', name: 'Undergraduate', count: `${stats.total_students || 0} Students`, icon: BookOpen, color: 'text-blue-600', bg: 'bg-blue-50' },
        { id: 'pg', name: 'Postgraduate', count: 'Real-time Sync', icon: GraduationCap, color: 'text-purple-600', bg: 'bg-purple-50' },
    ];

    return (
        <div className="space-y-8">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {programs.map((program) => (
                    <motion.div
                        key={program.id}
                        whileHover={{ scale: 1.02 }}
                        whileTap={{ scale: 0.98 }}
                        className="glass-card p-8 rounded-3xl cursor-pointer relative overflow-hidden group"
                        onClick={() => navigate('/admin/degrees', { state: { type: program.id.toUpperCase() } })}
                    >
                        <div className={`absolute top-0 right-0 w-32 h-32 ${program.bg} opacity-50 rounded-bl-full translate-x-8 -translate-y-8 group-hover:scale-110 transition-transform`} />

                        <div className={`p-4 ${program.bg} ${program.color} w-fit rounded-2xl mb-6 shadow-sm`}>
                            <program.icon className="w-8 h-8" />
                        </div>

                        <h3 className="text-2xl font-bold text-gray-800 mb-2">{program.name} Programs</h3>
                        <p className="text-gray-500 mb-6">{program.count}</p>

                        <button className="flex items-center gap-2 text-sm font-bold text-primary-600 group-hover:gap-4 transition-all">
                            <span>Manage Degrees</span>
                            <Zap className="w-4 h-4 fill-current" />
                        </button>
                    </motion.div>
                ))}
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
                <div className="lg:col-span-2 glass-card p-6 rounded-2xl">
                    <div className="flex items-center justify-between mb-6">
                        <h4 className="font-bold text-gray-800 flex items-center gap-2">
                            <Activity className="w-5 h-5 text-green-500" />
                            System Activity
                        </h4>
                        <span className="text-xs text-blue-600 font-bold uppercase tracking-widest">Real-time</span>
                    </div>
                    <div className="space-y-4">
                        {/* Mock activity feed */}
                        {[
                            "Admin allocated Dr. Alan Turing to Math-101",
                            "Alice Smith enrolled in Data Structures",
                            "New course 'Edge Computing' added to PG",
                            "Bob Jones completed Semester 1"
                        ].map((text, idx) => (
                            <div key={idx} className="flex items-center gap-4 p-3 hover:bg-gray-50 rounded-xl transition-colors">
                                <div className="w-2 h-2 bg-primary-400 rounded-full" />
                                <p className="text-sm text-gray-600">{text}</p>
                                <span className="text-[10px] text-gray-400 ml-auto">{idx + 1}m ago</span>
                            </div>
                        ))}
                    </div>
                </div>

                <div className="bg-primary-600 rounded-2xl p-6 text-white shadow-xl shadow-primary-500/20">
                    <h4 className="font-bold mb-4 opacity-80 uppercase text-[10px] tracking-widest">Enrollment Stats</h4>
                    <div className="space-y-6">
                        <div>
                            <div className="flex justify-between text-sm mb-2">
                                <span>Total Capacity</span>
                                <span>{stats.capacity_percentage || 0}%</span>
                            </div>
                            <div className="h-2 bg-white/20 rounded-full overflow-hidden">
                                <motion.div
                                    initial={{ width: 0 }}
                                    animate={{ width: `${stats.capacity_percentage || 0}%` }}
                                    className="h-full bg-white"
                                />
                            </div>
                        </div>
                        <div className="grid grid-cols-2 gap-4">
                            <div>
                                <p className="text-2xl font-bold">{stats.total_courses || 0}</p>
                                <p className="text-[10px] opacity-70 uppercase">Courses</p>
                            </div>
                            <div>
                                <p className="text-2xl font-bold">{stats.total_faculty || 0}</p>
                                <p className="text-[10px] opacity-70 uppercase">Faculty</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default AdminOverview;
