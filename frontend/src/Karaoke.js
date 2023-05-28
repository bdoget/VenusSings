import logo from "./logo.svg";
import "./Karaoke.css";
import { useState } from "react";
import Carousel from 'react-bootstrap/Carousel';


function Karaoke(){
    const [index, setIndex] = useState(0);
    const handleSelect = (selectedIndex) => {setIndex(selectedIndex);
    };

    return(
        <div className="App">
            <div className="App-header">
                <div className="container">
                        <div> </div>
                </div>
                <div>
                </div>
            </div>
        </div>
    )
}

export default Karaoke;