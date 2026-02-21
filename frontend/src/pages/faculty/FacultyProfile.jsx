
import { Mail, Phone, Book, Calendar, Award } from 'lucide-react';

const FacultyProfile = ({ user }) => {
    return (
        <div className="max-w-4xl">
            <div className="glass-card rounded-2xl overflow-hidden">
                <div className="h-32 bg-purple-600 relative">
                    <div className="absolute -bottom-16 left-8">
                        <img
                            src={user.photo_url || `https://ui-avatars.com/api/?name=${user.name}&size=128`}
                            className="w-32 h-32 rounded-2xl border-4 border-white shadow-xl"
                            alt="Profile"
                        />
                    </div>
                </div>

                <div className="pt-20 pb-8 px-8">
                    <div className="flex justify-between items-start">
                        <div>
                            <h3 className="text-2xl font-bold text-gray-800">{user.name}</h3>
                            <p className="text-purple-600 font-medium">{user.designation} • {user.user_id}</p>
                        </div>
                        <span className="px-3 py-1 bg-purple-100 text-purple-700 rounded-full text-sm font-semibold border border-purple-200">
                            Faculty
                        </span>
                    </div>

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mt-8">
                        <div className="space-y-4">
                            <div className="flex items-center gap-3 text-gray-600">
                                <div className="p-2 bg-gray-100 rounded-lg"><Mail className="w-4 h-4" /></div>
                                <span>{user.email || 'N/A'}</span>
                            </div>
                            <div className="flex items-center gap-3 text-gray-600">
                                <div className="p-2 bg-gray-100 rounded-lg"><Book className="w-4 h-4" /></div>
                                <span>{user.dept} Department</span>
                            </div>
                            <div className="flex items-center gap-3 text-gray-600">
                                <div className="p-2 bg-gray-100 rounded-lg"><Award className="w-4 h-4" /></div>
                                <span>Qualification: Ph.D.</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default FacultyProfile;
