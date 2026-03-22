const express = require("express");
const axios = require("axios");
const path = require("path");

const app = express();
const PORT = 3000;
const BACKEND_URL = process.env.BACKEND_URL || "http://backend:8000";

// Configura o EJS como view engine
app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));

// Serve arquivos estáticos da pasta 'public'
app.use(express.static(path.join(__dirname, "..", "public")));

// Rota principal para buscar e renderizar os cards
app.get("/", async (req, res) => {
  let cards = [];
  let backendOnline = false;

  try {
    const response = await axios.get(`${BACKEND_URL}/api/cards/`, {
      headers: {
        'Host': 'backend'
      }
    });
    cards = response.data;
    backendOnline = true;
  } catch (error) {
    console.error("Erro ao buscar dados do backend:", error.message);
  }

  res.render("index", { cards, backendOnline });
});

app.listen(PORT, () => console.log(`Node rodando na porta ${PORT}`));
