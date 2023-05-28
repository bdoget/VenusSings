// Importing modules
import React, { useState, useEffect } from "react";
import "./App.css";

function App() {
  // usestate for setting a javascript
  // object for storing and using data
  const [data, setdata] = useState([]);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    fetch("/subtitles/biking-frankocean").then((res) =>
      res.json().then((data) => {
        // Setting a data from api
        setdata(data);
      }
    ));
  };


  return (
    <div className="App">
      <div>
        <h1>Data from Backend</h1>
        <ul>
          {data.map((item) => (
            <li key={item.id}>
              <div>
                <p>{item.words}</p>
                <p>{item.startTimeMs}</p>
                <img src={item.image}></img>
                {/* <p>{item.startTimeMs}</p>  */}

              </div>
              
            </li>
          ))}
        </ul>
      </div>
    </div>

  );
}

export default App;

