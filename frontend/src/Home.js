import logo from "./logo.svg";
import "./Home.css";
import { useState, } from "react";
import { useNavigate} from "react-router-dom";


function Home() {
    const subject = "VenusSings";
    const navigate = useNavigate();


    const [password, setPassword] = useState('');

    function submit(){
        console.log(password);
        fetch('server.com/getSong/' + password )
        .then(res => {
            navigate('/karaoke');
        })    
    }

    return (
        <div className="App">
            <header className="App-header">
                <h1>
                    Welcome to {subject}!
                </h1>
                <div>
                    <p>Search here!</p>
                </div>
                <div>
                    <input placeholder='"song" - "artist"' type="text" onChange={event => setPassword(event.target.value)}/>
                    <button onClick={submit}>click me</button>
                </div>
            </header>
        </div>
    );
}
export default Home;