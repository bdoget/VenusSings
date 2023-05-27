import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import Home from './Home'


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Apps/>
  </React.StrictMode>
);

export default function Apps() {
  return(
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='karaoke' element={<Karaoke />} />
        <Route path='app' element={<App />} />
      </Routes>
    </BrowserRouter>
  )
}
