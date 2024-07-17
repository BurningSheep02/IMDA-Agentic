import React, { useState } from 'react';
import axios from 'axios';
import './Chat.css';


const Chat = () => {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState('');

    const handleSendMessage = async () => {
        if (input.trim()) {
            const userMessage = { text: input, sender: 'user' };
            setMessages([...messages, userMessage]);
            setInput('');

            try {
                const response = await axios.post('http://api.openai.com/v1/chat/completions', { "messages": [{"role": "user", "content": input}] });
                const botMessage = { text: response.data.response, sender: 'bot' };
                setMessages(prevMessages => [...prevMessages, botMessage]);
            } catch (error) {
                console.error('Error:', error);
                const errorMessage = { text: 'An error occurred', sender: 'bot' };
                setMessages(prevMessages => [...prevMessages, errorMessage]);
            }
        }
    };

    return (
        <div className="chatContainer">
            <div className="chatBox">
                {messages.map((message, index) => (
                    <div key={index} className={message.sender === 'user' ? 'userMessage' : 'botMessage'}>
                        {message.text}
                    </div>
                ))}
            </div>
            <div className="inputContainer">
                <input 
                    type="text" 
                    value={input} 
                    onChange={(e) => setInput(e.target.value)} 
                    className="input" 
                    placeholder="Type your message..."
                    onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
                />
                <button onClick={handleSendMessage} className="button">Send</button>
            </div>
        </div>
    );
};

export default Chat;
