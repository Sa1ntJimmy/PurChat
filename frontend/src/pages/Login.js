import Button from 'react-bootstrap/Button';
import './Login.css';
import Footer from '../components/Footer.js'

function Login() {
    return (
        <div>
            <div className='loginbox'>
                <h1 className='purchat'>PurChat</h1>

                <div className='username'>
                    <p className='usernamelabel'>Username: </p>
                    <input type="text" className='usernameinput' />

                </div>
                <Button variant="outline-success" size="lg" className='loginbutton' href='/chat'>Login</Button>
            </div>

            <Footer />
        </div>
    );
}

export default Login;