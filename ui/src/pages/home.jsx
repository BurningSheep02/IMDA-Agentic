import { 
  BrowserRouter as Router, Routes, 
  Route 
} from "react-router-dom";
import logo from '/star.svg'
import '../App.css'
import Chat from '../pages/chat' // import the Chat component from src/pages/
import MyButton from '../components/button'

const Home = () => { 
    const counter = 0;
    return (
      <>
        <div>
          <a href="https://react.dev" target="_blank">
            <img src={logo} className="logo react" alt="React logo" />
          </a>
        </div>
        <h1>IMDAi</h1>
        <div className="card">
            {/* <Router> 
                <MyButton to="chat" /> 
                <Routes> 
                    <Route path="/chat" element={<Chat />} /> 
                </Routes> 
            </Router> */}
            counter: {counter}
          <p>
            Edit <code>src/App.jsx</code> and save to test HMR
          </p>
        </div>
        <p className="read-the-docs">
          Click on the Vite and React logos to learn more
        </p>
      </>
    )
  }

//   import { useHistory } from 'react-router-dom';
// // Inside the handleLogin function
// const history = useHistory();
// history.push('/dashboard'); // Redirect to the dashboard after login

  export default Home