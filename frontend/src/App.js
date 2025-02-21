import React, { useState } from "react";
import axios from "axios";

function App() {
    const [inputData, setInputData] = useState("");
    const [response, setResponse] = useState(null);
    const [selectedOptions, setSelectedOptions] = useState([]);

    const handleSubmit = async () => {
        try {
            const jsonData = JSON.parse(inputData);
            const res = await axios.post("https://your-backend-url.onrender.com/bfhl", jsonData);
            setResponse(res.data);
        } catch (error) {
            alert("Invalid JSON input");
        }
    };

    return (
        <div>
            <h1>Your Roll Number</h1>
            <textarea value={inputData} onChange={(e) => setInputData(e.target.value)} placeholder='Enter JSON here...' />
            <button onClick={handleSubmit}>Submit</button>

            {response && (
                <div>
                    <label>Select data to display:</label>
                    <select multiple onChange={(e) => setSelectedOptions(Array.from(e.target.selectedOptions, opt => opt.value))}>
                        <option value="alphabets">Alphabets</option>
                        <option value="numbers">Numbers</option>
                        <option value="highest_alphabet">Highest Alphabet</option>
                    </select>

                    <div>
                        {selectedOptions.includes("alphabets") && <p>Alphabets: {response.alphabets.join(", ")}</p>}
                        {selectedOptions.includes("numbers") && <p>Numbers: {response.numbers.join(", ")}</p>}
                        {selectedOptions.includes("highest_alphabet") && <p>Highest Alphabet: {response.highest_alphabet.join(", ")}</p>}
                    </div>
                </div>
            )}
        </div>
    );
}

export default App;
