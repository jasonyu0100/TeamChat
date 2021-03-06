import { Switch, Route, useHistory, useLocation } from "react-router-dom"
import HomePage from "../pages/HomePage"
import RegistrationPage from "../pages/RegistrationPage"
import ChatPage from "../pages/ChatPage"
import "./css/_routes.scss"

/**
 * Stores and handles App Routes
 */
export default function AppRoutes() {
    let history = useHistory()
    const location = useLocation()

    return (
        <div className="route-content">
            <Switch>
                <Route exact path="/" component={HomePage} />
                <Route exact path="/register" component={RegistrationPage} />
                <Route exact path="/chat" component={ChatPage} />
            </Switch>

            {/* Cleaner way to do this? */}
            <ul>
                <li><a href="/">Home Page</a></li>
                <li><a href="/register">Registration</a></li>
                <li><a href="/chat">Chat</a></li>
            </ul>
        </div>
    )
}