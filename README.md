# LLM Agentic RAG with Magentic

![Image](https://github.com/user-attachments/assets/b5144ca5-442e-454a-9f49-7c70424506ce)

**Just started building. Here's the general plan:**

This project builds an **LLM-powered investment research agent** using the **Magentic** framework.  
It connects large language models with real financial data sources to produce dynamic, explainable insights.

## 🧩 Core Idea
An **agentic Retrieval-Augmented Generation (RAG)** pipeline where the model:
1. Understands user queries (e.g., “Analyze AAPL’s recent performance”)
2. Decides which APIs to call (news, prices, fundamentals, etc.)
3. Retrieves and processes real data
4. Generates a structured investment insight in natural language

## ⚙️ Components
- **Magentic** – handles LLM prompting, chaining, and function calling  
- **FastAPI** – serves the agent as a live endpoint
- **Alpha Vantage API** – provides financial data (prices, earnings, sentiment, etc.)  
- **Pydantic** - structures and validates LLM outputs
- **Async + Streaming** – enables real-time, step-by-step responses

## 🔁 Flow
1. User asks a question  
2. LLM selects relevant data functions  
3. Data is fetched and analyzed iteratively  
4. Final insight is generated and streamed back  

## 🧠 Purpose
To explore **agentic reasoning** in finance, blending **LLM decision-making** with **real-time market data** to create a smart, interactive research assistant.

## 🚀 Outcome
A working prototype of an **autonomous financial research agent** capable of:
- Iterative retrieval and reasoning  
- Context-aware analysis  
- Structured streaming responses  
- Ready deployment via FastAPI  
