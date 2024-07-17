import { 
  BrowserRouter as Router, Routes, 
  Route 
} from "react-router-dom";
import logo from '/star.svg'
import '../App.css'
import Chat from '../pages/chat' // import the Chat component from src/pages/
import MyButton from '../components/button'

const Home = () => { 
  return ( 
      <div className="home"> 
          <h1>This is the Home page</h1> 
      </div> 
  ) 
} 

//   import { useHistory } from 'react-router-dom';
// // Inside the handleLogin function
// const history = useHistory();
// history.push('/dashboard'); // Redirect to the dashboard after login

  export default Home