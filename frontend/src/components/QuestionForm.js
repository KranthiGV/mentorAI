import React, { useState } from "react";
import FlippedCard from "./FlippedCard";

function QuestionForm() {
  const [userQuestion, setUserQuestion] = useState("");
  const [responseText, setResponseText] = useState([]); // Initialize as an empty array
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = e => {
    e.preventDefault();
    setIsLoading(true);

    const data = { mentor_id: "h9ghxb2", msg: userQuestion };

    fetch("https://kranthigv--mentorai-fastapi-app.modal.run/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then(response => response.json())
      .then(data => {
        console.log(data);
        setResponseText(data[0].text); // Convert the full JSON response into a pretty-printed string
        setIsLoading(false);
      })
      .catch(error => {
        console.error("Error:", error);
        setResponseText(["An error occurred. Please try again later."]); // Set an array with an error message
        setIsLoading(false);
      });
  };

  return (
    <div className="main-container" style={{ display: "flex" }}>
      <div className="main-column">
        <form onSubmit={handleSubmit} className="form-container" style={{ width: "50%", textAlign: "left" }}>
          <label className="input-label" htmlFor="userQuestion">
            Question for <span style={{ fontFamily: "GT Pressura Trial", fontWeight: "700" }}>Elon Musk</span>:
          </label>
          <br />
          <textarea
            style={{
              fontFamily: "GT Sectra Display Trial",
              width: "464px",
              height: "213px",
              marginTop: "18px",
              font: "18px Inter, sans-serif",
              borderRadius: "20px",
              borderColor: "rgba(0, 0, 0, 1)",
              borderStyle: "solid",
              borderWidth: "1px",
              backgroundColor: "rgba(249, 247, 247, 0.8)",
            }}
            type="text"
            id="userQuestion"
            name="userQuestion"
            value={userQuestion}
            onChange={e => setUserQuestion(e.target.value)}
            disabled={isLoading}
          />
          <br />
          <input
            className="submit-btn"
            type="submit"
            value={isLoading ? "Waiting for response..." : "Submit"}
            disabled={isLoading}
          />
        </form>
      </div>

      <div className="card-container main-column">
        <FlippedCard responseText={responseText} />
      </div>
    </div>
  );
}

export default QuestionForm;
