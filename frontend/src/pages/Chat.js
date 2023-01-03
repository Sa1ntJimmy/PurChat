import Button from 'react-bootstrap/Button';
import './Chat.css';
import Footer from '../components/Footer.js'

function Chat() {
    return (
        <div>
            <div className='NavBar'>
                <h1 className='Logo'>PurChat</h1>
                <Button variant="outline-success" size="lg" className='logoutbutton' href='/login'>Logout</Button>
            </div>

            <Footer />
        </div>
    );
}

export default Chat;