# MCP Client-Server Demo

## 🚀 Overview

This project demonstrates a **complete Model Context Protocol (MCP) client-server architecture**, showcasing how AI agents interact with tools through a structured protocol.

It includes:

* MCP Server (tool provider)
* MCP Client (request handler)
* Logging and debugging setup

---

## 🧠 Problem Statement

Modern AI systems require a standardized way to interact with external tools and services.

This project demonstrates:

* How an MCP client communicates with an MCP server
* How tools are exposed and executed
* How responses are structured and returned

---

## 🏗️ Architecture

```text
User → MCP Client → MCP Server → Tool Execution → Response → Client → User
```

---

## ⚙️ Tech Stack

* Python
* Model Context Protocol (MCP)
* Loguru (for structured logging)
* MCP Inspector (for debugging)

---

## 📂 Project Structure

```bash
mcp-client-server-demo/
│── clients/        # MCP client implementation
│── servers/        # MCP server exposing tools
│── logs/           # Log files (Loguru)
│── README.md
│── requirements.txt
```

---

## 🔄 How It Works

1. User sends input
2. MCP Client formats request
3. Request is sent to MCP Server
4. Server identifies appropriate tool
5. Tool executes logic
6. Response is returned to client
7. Client displays result

---

## ▶️ How to Run

```bash
# Clone repository
git clone https://github.com/KrishnaPavan1729/mcp-client-server-demo.git

cd mcp-client-server-demo

# Install dependencies
pip install -r requirements.txt

# Run server
python servers/server.py

# Run client
python clients/client.py
```

---

## 🧪 Example Flow

### Input

User asks:

```
"Execute a tool or fetch data"
```

### Flow

* Client sends request → Server
* Server executes tool
* Result returned 


## 📊 Logging & Debugging

* Logging handled using **Loguru**

* Logs stored for:

  * Client requests
  * Server processing
  * Tool execution

* Debugging performed using **MCP Inspector**

---

## 📌 Future Improvements

* Add OpenAI / Claude integration
* Add real-world tools (file reader, API calls)
* Add RAG (ChromaDB / Pinecone)
* Add Docker support
* Add authentication & security

---

## 👨‍💻 Author

**Krishna Pavan**

---

## ⭐ Why This Project Matters

This project demonstrates foundational concepts required for:

* Agentic AI systems
* Tool-augmented LLMs
* Production MCP architectures
