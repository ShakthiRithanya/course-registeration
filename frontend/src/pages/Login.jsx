import { useState } from 'react';
import { LogIn, GraduationCap, ShieldCheck, User } from 'lucide-react';
import axios from 'axios';

const Login = ({ onLogin }) => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError('');
        try {
            const response = await axios.post('/api/auth/login', { email, password });
            localStorage.setItem('token', response.data.access_token);
            onLogin(response.data);
        } catch (err) {
            setError(err.response?.data?.detail || 'Login failed. Check your credentials.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-screen flex items-center justify-center bg-gray-50 p-4">
            <div className="bg-white w-full max-w-md p-8 rounded-2xl shadow-xl border border-gray-100">
                <div className="flex flex-col items-center mb-8">
                    <div className="w-16 h-16 bg-blue-600 rounded-2xl flex items-center justify-center shadow-lg mb-4">
                        <GraduationCap className="text-white w-10 h-10" />
                    </div>
                    <h1 className="text-2xl font-bold text-gray-800">Academic Portal</h1>
                    <p className="text-gray-500 text-sm">Sign in to manage your enrollment</p>
                </div>

                <form onSubmit={handleSubmit} className="space-y-6">
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">Email Address</label>
                        <input
                            type="email"
                            required
                            className="w-full px-4 py-2 bg-gray-50 border border-gray-200 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none"
                            placeholder="name@college.edu"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                        />
                    </div>

                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">Password</label>
                        <input
                            type="password"
                            required
                            className="w-full px-4 py-2 bg-gray-50 border border-gray-200 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none"
                            placeholder="••••••••"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                        />
                    </div>

                    {error && <p className="text-red-500 text-sm italic">{error}</p>}

                    <button
                        type="submit"
                        disabled={loading}
                        className="w-full py-3 bg-blue-600 text-white rounded-lg font-bold hover:bg-blue-700 transition-colors flex items-center justify-center gap-2"
                    >
                        {loading ? 'Signing In...' : (
                            <>
                                <LogIn className="w-5 h-5" />
                                <span>Sign In</span>
                            </>
                        )}
                    </button>
                </form>

                <div className="mt-8 pt-6 border-t border-gray-100 italic text-[10px] text-gray-400 text-center">
                    Use demo credentials below to explore roles.
                </div>

                <div className="mt-4 grid grid-cols-1 gap-2">
                    <button onClick={() => { setEmail('admin@college.edu'); setPassword('admin123'); }} className="text-xs text-left p-2 border rounded hover:bg-gray-50">Admin: admin@college.edu / admin123</button>
                    <button onClick={() => { setEmail('alice@college.edu'); setPassword('stud123'); }} className="text-xs text-left p-2 border rounded hover:bg-gray-50">Student: alice@college.edu / stud123</button>
                    <button onClick={() => { setEmail('turing@college.edu'); setPassword('fac123'); }} className="text-xs text-left p-2 border rounded hover:bg-gray-50">Faculty: turing@college.edu / fac123</button>
                </div>
            </div>
        </div>
    );
};

export default Login;
