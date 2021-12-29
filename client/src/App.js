import './App.css';
import { useState, useEffect }  from 'react';

function App() {
  const [text, setText] = useState([]);
  useEffect(() => {
    fetch("https://fanfic-generator-i2xsl.ondigitalocean.app/api/fanfic")
      .then(res => res.json())
      .then(
        (data) => {
          setText(data.text);
        },
        (error) => {
        }
      )
  }, [])
  return (
    <div className="App">
      <p className="text">{text}</p>
    </div>
  );
}

export default App;
