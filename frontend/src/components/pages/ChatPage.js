import ChatHeader from '../app/ChatHeader'
import personIcon from '../../images/person_icon.jpg'
import pinIcon from '../../images/pin_icon.png'


export default function ChatPage() {
    const icons = { person: personIcon, pin: pinIcon };
    return <div className="chat-container">
        <ChatHeader icons={icons} />
    </div>
}