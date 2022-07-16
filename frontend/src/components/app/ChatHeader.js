import Button from '../app/Button'

// Have access to general.scss stylesheet without importing from component file
// Temporarily have button disabled

const clickedButton = () => {
    console.log("Clicked!")
}

const ChatHeader = ({ icons }) => {
    return (
        <div className="chat-header">
            <h1>Group Chat</h1>
            <Button img={icons.person} onClick={clickedButton} />
            <Button img={icons.pin} onClick={clickedButton} />
        </div>
    )
}

export default ChatHeader