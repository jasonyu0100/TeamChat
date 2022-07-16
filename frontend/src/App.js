import { BrowserRouter } from "react-router-dom"
import AppRoutes from "./components/app/AppRoutes"
import './css/general.scss'
import './app.scss'


export default function App(props) {
    return (
        <BrowserRouter>
            <AppRoutes />
        </BrowserRouter>
    )
}
