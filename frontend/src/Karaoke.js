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
                    <div className="pic" id="pic4"></div>
                    <div className="pic" id="pic3"></div>
                    <div className="pic" id="pic2"></div>
                    <div className="pic" id="pic1"></div>
                </div>
                <div>
                    <div className="text-overlay" id='text1'>First Lyrics</div>
                    <div className="text-overlay" id='text2'>Second Lyrics</div>
                    <div className="text-overlay" id='text3'>Third Lyrics</div>
                    <div className="text-overlay" id='text4'>Fourth Lyrics</div>
                </div>
            </div>
        </div>
    )
}

export default Karaoke;