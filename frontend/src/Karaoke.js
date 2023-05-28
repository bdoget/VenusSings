import logo from "./logo.svg";
import "./Karaoke.css";
import { useState } from "react";
import Carousel from 'react-bootstrap/Carousel';


function Karaoke(){
    const FakeData = [{lyric: "First lyrics", image: "./images/umbrella.jpg"}, {lyric: "Second lyrics", image: ""}];
    const [index, setIndex] = useState(0);
    const handleSelect = (selectedIndex) => {setIndex(selectedIndex);
    };

    return(
        <div className="App">
            <div className="App-header">
                <div className="container">
                    {FakeData.map(data => (
                        div 
                    ))}
                    {/* <div className='pic' id='pic2' />
                    <div className='pic' id='pic1' />
                </div>
                <div>
                    <div className="text-overlay" id='text1'>first lyrics</div>
                    <div className="text-overlay" id='text2'>second lyrics</div> */}
                </div>
            </div>
        </div>
    )
}

export default Karaoke;