const MyButton = ({ to }) => { 
  
    return ( 
        <a href={`/${to}`}> 
            <button className="my-button"> 
                Send request to {to === '' ? "home" : to} 
            </button> 
        </a> 
    ) 
} 
  
export default MyButton;
