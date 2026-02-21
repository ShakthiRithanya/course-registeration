import { NavLink } from 'react-router-dom';

import {
    LayoutDashboard,
    BookOpen,
    User,
    LogOut,
    GraduationCap,
    Users,
    Layers,
    Settings
} from 'lucide-react';

const Sidebar = ({ role, user, logout }) => {
    const menuItems = {
        student: [
            { name: 'Profile', path: '/student/profile', icon: User },
            { name: 'Enroll', path: '/student/enroll', icon: BookOpen },
            { name: 'Enrolled', path: '/student/enrolled', icon: Layers },
        ],
        faculty: [
            { name: 'Profile', path: '/faculty/profile', icon: User },
            { name: 'Courses', path: '/faculty/courses', icon: BookOpen },
            { name: 'Backlogs', path: '/faculty/backlogs', icon: Layers },
        ],
        admin: [
            { name: 'Dashboard', path: '/admin', icon: LayoutDashboard },
            { name: 'Degrees', path: '/admin/degrees', icon: GraduationCap },
            { name: 'Faculty', path: '/admin/faculty', icon: Users },
            { name: 'Allocation', path: '/admin/allocation', icon: Settings },
        ],
    };

    return (
        <div className="w-64 h-screen bg-white border-r border-gray-100 flex flex-col fixed left-0 top-0">
            <div className="p-6 border-b border-gray-50 flex items-center gap-3">
                <div className="w-10 h-10 bg-primary-600 rounded-xl flex items-center justify-center shadow-lg shadow-primary-500/30">
                    <GraduationCap className="text-white w-6 h-6" />
                </div>
                <span className="font-bold text-lg text-gray-800 tracking-tight">Academic</span>
            </div>

            <div className="p-4 flex-1">
                <div className="space-y-1">
                    {menuItems[role]?.map((item) => (
                        <NavLink
                            key={item.path}
                            to={item.path}
                            className={({ isActive }) => `
                flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-200
                ${isActive
                                    ? 'bg-primary-50 text-primary-600 font-semibold'
                                    : 'text-gray-500 hover:bg-gray-50 hover:text-gray-700'}
              `}
                        >
                            <item.icon className="w-5 h-5" />
                            <span>{item.name}</span>
                        </NavLink>
                    ))}
                </div>
            </div>

            <div className="p-4 border-t border-gray-50 bg-gray-50/30">
                <div className="flex items-center gap-3 px-2 mb-4">
                    <img
                        src={user.photo_url || `https://ui-avatars.com/api/?name=${user.name}`}
                        className="w-10 h-10 rounded-full border-2 border-white shadow-sm"
                        alt="Profile"
                    />
                    <div className="overflow-hidden">
                        <p className="text-sm font-semibold text-gray-800 truncate">{user.name}</p>
                        <p className="text-xs text-gray-500 capitalize">{role}</p>
                    </div>
                </div>
                <button
                    onClick={logout}
                    className="flex items-center gap-3 w-full px-4 py-2 text-sm text-red-500 hover:bg-red-50 rounded-lg transition-colors"
                >
                    <LogOut className="w-4 h-4" />
                    <span>Sign Out</span>
                </button>
            </div>
        </div>
    );
};

export default Sidebar;
