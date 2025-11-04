import React, { useState } from "react";
import axios from "axios";

function App() {
  const [query, setQuery] = useState("");
  const [category, setCategory] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!query) return;
    setLoading(true);
    try {
      const res = await axios.post("http://127.0.0.1:5000/predict", { query });
      setCategory(res.data.category);
    } catch (err) {
      console.error(err);
      setCategory("Error connecting to backend");
    }
    setLoading(false);
  };

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        marginTop: "5rem",
        fontFamily: "sans-serif",
      }}
    >
      <h1 style={{ marginBottom: "1rem" }}>Bank Query Classifier</h1>
      <form onSubmit={handleSubmit} style={{ display: "flex", gap: "1rem" }}>
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Enter your query (e.g. Reset my PIN)"
          style={{
            padding: "0.5rem 1rem",
            width: "300px",
            borderRadius: "8px",
            border: "1px solid gray",
          }}
        />
        <button
          type="submit"
          style={{
            padding: "0.5rem 1rem",
            borderRadius: "8px",
            background: "#007bff",
            color: "white",
            border: "none",
          }}
        >
          {loading ? "Classifying..." : "Classify"}
        </button>
      </form>

      {category && (
        <div
          style={{
            marginTop: "2rem",
            padding: "1rem",
            background: "#f3f4f6",
            borderRadius: "10px",
            width: "350px",
            textAlign: "center",
          }}
        >
          <h3>Predicted Category:</h3>
          <p style={{ fontWeight: "bold", color: "#007bff" }}>{category}</p>
        </div>
      )}
    </div>
  );
}

export default App;
