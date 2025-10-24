import App from "./App";
import Login from "./pages/auth/login";
import Signup from "./pages/auth/register";

export const routes = [
    {
        path: '/',
        element: < App/>
    },
    {
        path: '/login',
        element: < Login/>
    },
    {
        path: '/signup',
        element: < Signup/>
    }
]