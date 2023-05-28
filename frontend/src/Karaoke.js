import logo from "./logo.svg";
import "./Karaoke.css";
import { useState } from "react";


function Karaoke(){
    return(
        <div className="App">
            <div className="App-header">
                <div className="container">
                    <div className='pic' id='pic2' />
                    <div className='pic' id='pic1' />
                </div>
                <div>
                <div id="carouselExampleSlidesOnly" class="carousel slide" data-ride="carousel">
                    <div class="carousel-inner">
                        <div class="carousel-item active">
                        <div class="d-block w-100">
                            <h3>First slide</h3>
                            <p>first lyric</p>
                        </div>
                        </div>
                        <div class="carousel-item">
                        <div class="d-block w-100">
                            <h3>Second slide</h3>
                            <p>second lyric</p>
                        </div>
                        </div>
                        <div class="carousel-item">
                        <div class="d-block w-100">
                            <h3>Third slide</h3>
                            <p>third lyric</p>
                        </div>
                        </div>
                    </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Karaoke;