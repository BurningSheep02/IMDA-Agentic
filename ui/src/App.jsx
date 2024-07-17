import './App.css';
import { Link, Route, Routes } from 'react-router-dom';
import Home from './Components/Home';
import About from './Components/About';
import Chat from './Components/Chat';
import logo from './assets/IMDA.svg';

function App() {
    return (
        <div className="App">
            <div className="navbar">
                <div className="IMDAlogo">
                    <a href="https://react.dev" target="_blank">
                        <img src={logo} className="logo imda" alt="IMDA logo" />
                    </a>
                </div>
                <div className='nav-title'>
                    <Link to="/" className='nav-link'>
                        Home
                    </Link>
                    <Link to="/about" className='nav-link'>
                        About
                    </Link>
                    <Link to="/chat" className='nav-link'>
                        Chat
                    </Link>
                </div>
            </div>
            <div className="content">
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/about" element={<About />} />
                    <Route path="/chat" element={<Chat />} />
                </Routes>
            </div>
        </div>
    );
}

export default App;