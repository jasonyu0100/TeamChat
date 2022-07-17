import { useState } from 'react'

export default function RegistrationPage() {
    <>
    {/* An array of userInfo arrays, containing all the info/}*/}
    const [allUsers, setAllUsers] = useState([])
    {/* User info as initially an empty array that would contain the user's info:
    e.g. 'username: ..., password: ....' */}
    const [userInfo, setUserInfo] = useState([])
    
    
    return <div className="content">
        <h1 class="registration-field">Registration</h1>
        <input autocomplete="off" autofocus class="registration-field" name="username" placeholder="Username" type="text"/>
        <input class="registration-field" name="password" placeholder="Password" type="password"/>
        <input class="registration-field" name="confirmation" placeholder="Confirm Password" type="password"/>
        <button class="btn btn-primary" type="submit">Register</button>
    </div>
    </>
}