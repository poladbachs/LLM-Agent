# 💼 AI Investment Agent Suite

![Image](https://github.com/user-attachments/assets/4e880b46-c2d9-48d8-8126-2163a0b375fe)

A system of **LLM-powered financial agents** that perform live data retrieval, reasoning, and analysis.  
Built with the **Magentic framework**, it shows how language models can act as analytical engines capable of calling real functions, fetching data, and forming structured investment insights.

---

## 🧩 Project Overview

The suite connects **reasoning-based AI** with **financial data pipelines**.  
Each agent interprets a question, selects relevant financial endpoints, retrieves data, and produces a coherent analytical response.

The process follows four clear stages:

1. **Function Selection** – the LLM dynamically determines which API endpoint to use (e.g., prices, fundamentals, news, earnings) based on the input query.  
2. **Retrieval** – it calls the chosen functions to fetch relevant financial data.  
3. **Processing** – the retrieved data is formatted and organized for model reasoning.  
4. **Generation** – the LLM analyzes the data and produces an investment insight.

This structure allows the model to **autonomously plan, execute, and decide when it has gathered enough information**, exactly like a research assistant performing iterative analysis.

---

## ⚙️ Core Stack

**Frameworks:** Magentic · FastAPI · Gradio · Chainlit · Pydantic  
**Data:** Alpha Vantage API (prices, fundamentals, news, earnings)  
**Features:** Async logic · Function calling · Streaming responses · Structured outputs

```bash
pip install magentic fastapi uvicorn gradio chainlit pydantic python-dotenv requests

python3 async_agent.py         # Entity Explorer  
python3 portfolio_frontend.py  # Portfolio Generator  
python3 rag_finance.py         # Research Agent backend
python3 rag_frontend.py        # Research Agent interface (run simultanously with backend (rag_finance.py))

# Access:
Gradio   → http://localhost:7860
FastAPI  → http://localhost:8000
Chainlit → http://localhost:8000
```

---

## 🧠 Modules

### 1. Async Entity Explorer
![Image](https://github.com/user-attachments/assets/3f526fd4-51a5-4ccb-84b6-069c7db345da)

Runs asynchronous queries to identify and summarize related companies, sectors, or trends.  
Used to demonstrate **parallel reasoning** and **entity association**.

### 2. Portfolio Design Assistant
![Image](https://github.com/user-attachments/assets/b62dc07d-cbfd-4711-b065-234877370627)

Generates diversified portfolios by risk level.  
Each portfolio includes allocation percentages across equities, bonds, crypto, and commodities, with concise reasoning.

### 3. Investment Research Agent
![Image](https://github.com/user-attachments/assets/5785e101-d736-41b6-aa7a-c286f733e39b)

Retrieves live financial data - prices, sentiment, and fundamentals - and builds a structured investment briefing.

The LLM autonomously decides which data functions to call and when to stop.

This is done by exposing it to a list of available functions inside the prompt.  

For each query, the model selects the most relevant function (e.g., prices, sentiment, or fundamentals), receives the results, and re-evaluates if additional data is needed.  

When it determines that enough information is gathered, it signals to stop and proceeds with analysis — forming a self-contained reasoning loop.

---

## 🧩 Concept

The project applies this agentic reasoning pipeline to **investment research**.  
The model acts as an investment analyst that can decide *what data to gather* and *how to interpret it*, without being hard-coded for specific tasks.  
It uses Magentic’s prompt chaining and function-calling to loop through data retrieval until the answer is complete — forming a working example of **Retrieval-Augmented Generation (RAG)** for finance.

This demonstrates how LLMs can be integrated into research and quantitative workflows — combining reasoning, data access, and interpretability.

---

## 📘 Key Outcomes

- Implemented dynamic **function selection and reasoning loops** with Magentic  
- Integrated **live market APIs** (e.g., Alpha Vantage) for real data retrieval  
- Produced **structured, explainable outputs** for investment workflows  
- Showcased **how LLMs can act as autonomous research assistants** in finance

