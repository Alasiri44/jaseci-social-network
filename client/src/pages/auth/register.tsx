import { Link } from "react-router-dom";
import logo from "/logo.png";


export default function Signup() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50 px-4">
      <div className="bg-white shadow-lg rounded-2xl p-8 w-full max-w-md text-center">
        <img
          src={logo}
          alt="ConnectSphere Logo"
          className="w-40 h-24 object-cover mx-auto rounded-xl mb-4"
        />

        <h1 className="text-2xl font-semibold text-gray-800 mb-1">
          Create an Account
        </h1>
        <p className="text-gray-500 mb-6">Join ConnectSphere today</p>

        <form className="space-y-5 text-left">
          <div>
            <label htmlFor="name" className="block text-gray-700 font-medium mb-1">
              Full Name
            </label>
            <input
              type="text"
              id="name"
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
            />
          </div>

          <div>
            <label htmlFor="email" className="block text-gray-700 font-medium mb-1">
              Email
            </label>
            <input
              type="email"
              id="email"
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
            />
          </div>

          <div>
            <label htmlFor="password" className="block text-gray-700 font-medium mb-1">
              Password
            </label>
            <input
              type="password"
              id="password"
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
            />
          </div>

          <div>
            <label
              htmlFor="confirmPassword"
              className="block text-gray-700 font-medium mb-1"
            >
              Confirm Password
            </label>
            <input
              type="password"
              id="confirmPassword"
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
            />
          </div>

          <button
            type="submit"
            className="w-full bg-green-600 text-white py-2 rounded-lg hover:bg-green-700 transition duration-200"
          >
            Sign Up
          </button>
        </form>

        <p className="text-gray-600 text-sm mt-6">
          Already have an account?{" "}
          <Link
            to='/login'
            className="text-indigo-600 font-medium hover:underline hover:text-indigo-700 transition"
          >
            Log in
          </Link>
        </p>
      </div>
    </div>
  );
}
