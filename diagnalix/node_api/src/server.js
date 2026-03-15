const express = require("express");
const app = express();
app.get("/", (req, res) => res.send("Diagnalix Node API Ativa"));
app.listen(3000, () => console.log("Node rodando na porta 3000"));
