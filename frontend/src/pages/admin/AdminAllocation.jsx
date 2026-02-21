import { useState } from 'react';
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import axios from 'axios';
import { motion } from 'framer-motion';

import { Settings, Users, BookOpen, Check, AlertCircle } from 'lucide-react';

const AdminAllocation = () => {
    const queryClient = useQueryClient();
    const [selectedFaculty, setSelectedFaculty] = useState('');
    const [selectedCourse, setSelectedCourse] = useState('');
    const [success, setSuccess] = useState('');

    const { data: faculty = [] } = useQuery({
        queryKey: ['admin-faculty'],
        queryFn: () => axios.get('/api/admin/faculty').then(res => res.data)
    });

    const { data: courses = [] } = useQuery({
        queryKey: ['admin-courses'],
        queryFn: () => axios.get('/api/admin/courses').then(res => res.data)
    });

    const allocateMutation = useMutation({
        mutationFn: (payload) => axios.post('/api/admin/allocate', payload),
        onSuccess: () => {
            setSuccess('Allocation successful!');
            setSelectedFaculty('');
            setSelectedCourse('');
            setTimeout(() => setSuccess(''), 3000);
        }
    });

    const handleAllocate = () => {
        if (!selectedFaculty || !selectedCourse) return;
        allocateMutation.mutate({
            faculty_id: selectedFaculty,
            course_id: selectedCourse
        });
    };

    return (
        <div className="max-w-4xl space-y-8">
            <div className="bg-white p-8 rounded-3xl shadow-sm border border-gray-100">
                <div className="flex items-center gap-4 mb-8">
                    <div className="p-3 bg-primary-100 text-primary-600 rounded-2xl">
                        <Settings className="w-8 h-8" />
                    </div>
                    <div>
                        <h3 className="text-2xl font-bold text-gray-800 tracking-tight">Resource Allocation</h3>
                        <p className="text-sm text-gray-500">Assign faculty members to specific academic courses.</p>
                    </div>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
                    <div>
                        <label className="block text-sm font-bold text-gray-700 mb-2 uppercase tracking-wider text-[10px]">Select Faculty</label>
                        <select
                            className="input-field appearance-none cursor-pointer"
                            value={selectedFaculty}
                            onChange={(e) => setSelectedFaculty(e.target.value)}
                        >
                            <option value="">-- Choose Professor --</option>
                            {faculty.map(f => (
                                <option key={f.id} value={f.id}>{f.name} ({f.dept})</option>
                            ))}
                        </select>
                    </div>

                    <div>
                        <label className="block text-sm font-bold text-gray-700 mb-2 uppercase tracking-wider text-[10px]">Select Course</label>
                        <select
                            className="input-field appearance-none cursor-pointer"
                            value={selectedCourse}
                            onChange={(e) => setSelectedCourse(e.target.value)}
                        >
                            <option value="">-- Choose Course --</option>
                            {courses.map(c => (
                                <option key={c.id} value={c.id}>{c.name} ({c.id})</option>
                            ))}
                        </select>
                    </div>
                </div>

                {success && (
                    <motion.div
                        initial={{ opacity: 0, scale: 0.9 }}
                        animate={{ opacity: 1, scale: 1 }}
                        className="mb-8 p-4 bg-green-50 text-green-700 rounded-2xl flex items-center justify-center gap-2 border border-green-100 font-bold"
                    >
                        <Check className="w-5 h-5" />
                        <span>{success}</span>
                    </motion.div>
                )}

                <button
                    onClick={handleAllocate}
                    disabled={!selectedFaculty || !selectedCourse || allocateMutation.isLoading}
                    className="btn-primary w-full py-4 text-lg font-bold flex items-center justify-center gap-2 rounded-2xl shadow-xl shadow-primary-500/20 disabled:opacity-50 disabled:shadow-none"
                >
                    {allocateMutation.isLoading ? 'Processing...' : 'Assign Allocation'}
                </button>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="glass-card p-6 rounded-2xl flex items-center gap-4">
                    <div className="p-3 bg-blue-50 text-blue-600 rounded-xl"><Users className="w-6 h-6" /></div>
                    <div>
                        <p className="text-xs text-gray-400 font-bold uppercase tracking-widest">Active Faculty</p>
                        <p className="text-xl font-bold text-gray-800">{faculty.length}</p>
                    </div>
                </div>
                <div className="glass-card p-6 rounded-2xl flex items-center gap-4">
                    <div className="p-3 bg-purple-50 text-purple-600 rounded-xl"><BookOpen className="w-6 h-6" /></div>
                    <div>
                        <p className="text-xs text-gray-400 font-bold uppercase tracking-widest">Total Courses</p>
                        <p className="text-xl font-bold text-gray-800">{courses.length}</p>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default AdminAllocation;

// faculty course allocation

// POST and DELETE allocate
