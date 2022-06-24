import { Switch, Route, useHistory, useLocation } from "react-router-dom"
import HomePage from "../pages/HomePage"
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
            </Switch>
        </div>
    )
}