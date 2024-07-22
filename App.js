import React, { useState } from 'react';
import axios from 'axios';

const App = () => {
    const [start_date, setFirst] = useState("");
    const [end_date, setLast] = useState("");
    const [name,setName]=useState("")
    const [data, setData] = useState([]);

    const getData = () => {
        axios.get("http://localhost:8000/details", {
            params: {
                name:name,
                start_date: start_date,
                end_date: end_date,
      
            }
        })
        .then(response => setData(response.data.data))  // Assuming response.data is structured as { "data": [...] }
        .catch(error => console.error('Error fetching data:', error));
    };

    return (
        <div>
            <input type="text" name="start_date" value={start_date} onChange={(e) => setFirst(e.target.value)} /><br/>
            <input type="text" name="end_date" value={end_date} onChange={(e) => setLast(e.target.value)} /><br/>
            <input type="text" name="name" value={name} onChange={(e) => setName(e.target.value)} /><br/>
            <button onClick={getData}>GET</button>
            <pre>{JSON.stringify(data, null, 2)}</pre>
        </div>
    );
};

export default App;




