const express = require("express");
const axios = require("axios");
const cors = require("cors");
const bodyParser = require("body-parser");

const app = express();
app.use(cors({ origin: "*" }));
app.use(bodyParser.json());

app.get("/", (req, res) => res.send("🌐 Node.js backend running successfully!"));

app.post("/getresult", async (req, res) => {
  try {
    console.log("Incoming data:", req.body);

    const flaskResponse = await axios.post("http://127.0.0.1:5000/predict", req.body);

    res.json({
      status: "success",
      result: flaskResponse.data,
    });
  } catch (err) {
    console.error("Error communicating with Flask:", err.message);
    res.status(500).json({ status: "error", message: "Flask connection failed" });
  }
});

app.listen(3000, () => console.log("🚀 Node.js backend on port 3000"));
