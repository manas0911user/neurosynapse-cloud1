# NeuroSynapse Cloud – Serverless Function Scheduler

🚀 **NeuroSynapse Cloud** is an experimental serverless function scheduling system.  
It implements a **Rank-Based Scheduler** that optimizes function execution by monitoring latency, CPU, memory usage, and success rate.  
The system runs functions in a sandboxed environment and logs results into a structured database for further analysis.

---

## 📂 Project Structure

neurosynapse-cloud/
├── backend/
│ ├── core/ # Scheduler logic 
│ ├── utils/ # Logging utilities
│ ├── db/ # Database models
│ └── test_logger.py # Test for logger + DB
├── sandbox/ # Function runner sandbox
├── logs/ # Auto-generated logs & DB
└── README.md

---

## ⚡ Features
- Rank-based function scheduling
- Sandbox runner for safe execution
- Logging to console + file
- SQLite database for execution history
- Modular design (easily extendable)

---

## 🛠️ Installation

Clone the repo:
```bash
git clone https://github.com/manas0911user/neurosynapse-cloud.git
cd neurosynapse-cloud

