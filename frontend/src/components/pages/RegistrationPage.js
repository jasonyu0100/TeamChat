export default function RegistrationPage() {
    return <div className="content">
        <h1>Registration</h1>
        <input autocomplete="off" autofocus class="registration-field" name="username" placeholder="Username" type="text"/>
        <input class="registration-field" name="password" placeholder="Password" type="password"/>
        <input class="registration-field" name="confirmation" placeholder="Confirm Password" type="password"/>
        <button class="btn btn-primary" type="submit">Register</button>
    </div>
}