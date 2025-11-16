# 🛠️ Architect AI - Autonomous Code Generation Agent

<div align="center">

**Transform natural language into complete working projects with an interactive Streamlit interface**

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![LangGraph](https://img.shields.io/badge/LangGraph-0.6.3-green.svg)](https://github.com/langchain-ai/langgraph)
[![Groq](https://img.shields.io/badge/Groq-Powered-orange.svg)](https://groq.com/)

</div>

---

## 🚀 Overview

**Architect AI** transforms your ideas into complete, working software projects through natural language. Just describe what you want - "Create a modern to-do app" or "Build a colorful calculator" - and watch three AI agents collaborate to plan, design, and code your entire project!

### ✨ Why Architect AI?

- **🧠 Smart Multi-Agent Team**: Planner → Architect → Coder working together
- **⚡ Lightning Fast**: Groq-powered for near-instant results  
- **📦 Complete Projects**: Full applications, not just code snippets
- **🎨 Beautiful Interface**: Real-time progress with smooth animations
- **📥 Ready to Deploy**: Download as ZIP and run immediately

### 🎯 Perfect For

**Rapid Prototyping** • **Learning & Education** • **Client Demos** • **Side Projects** • **Code Inspiration**

### ⚡ Key Features

🎨 **Streamlit UI** • 🤖 **Multi-Agent System** • 📝 **Natural Language** • 🏗️ **Auto Scaffolding** • 💾 **Real-time Tracking** • 📥 **ZIP Downloads** • 🎯 **Smart Examples** • 🔧 **File Operations** • 🚀 **Groq Powered**

---

## 🏗️ Architecture

Architect AI implements a multi-agent workflow using LangGraph with a beautiful Streamlit interface, featuring three specialized agents:

### 🧠 Agent Roles

1. **Planner Agent**
   - Analyzes your natural language request
   - Generates a comprehensive project plan
   - Defines tech stack, features, and file structure

2. **Architect Agent**
   - Converts the plan into actionable implementation steps
   - Creates detailed task descriptions for each file
   - Establishes dependencies and execution order

3. **Coder Agent**
   - Implements each task using ReAct (Reasoning + Acting) pattern
   - Writes actual code to files using available tools
   - Iterates through all implementation steps sequentially

<div align="center">
    <!-- Architecture diagram would go here -->
</div>

### 🔄 Workflow

```
User Prompt → Planner → Architect → Coder (loop) → Complete Project
```

---

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.11 or higher** - [Download Python](https://www.python.org/downloads/)
- **uv** (Python package installer) - [Installation Guide](https://docs.astral.sh/uv/getting-started/installation/)
- **Groq API Key** - [Get your API key](https://console.groq.com/keys)

### 📦 Quick Setup

```bash
# Clone and setup
git clone <repository-url>
cd architect-ai
uv venv && .venv\Scripts\Activate.ps1  # Windows
# source .venv/bin/activate              # macOS/Linux

# Install dependencies
pip install streamlit groq langchain-groq langgraph python-dotenv

# Configure API key
cp .sample_env .env
# Edit .env and add: GROQ_API_KEY=your_api_key_here
```

### ▶️ Running Architect AI

Start the Streamlit application:
```bash
streamlit run app.py
```

Or using Python module:
```bash
python -m streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

### 🎛️ Adjusting Complexity

Use the **Recursion Limit** slider in the sidebar to control project complexity:
- **🐢 Conservative (50)** - Simple, small projects
- **⚡ Balanced (100)** - Medium complexity (recommended)
- **🚀 Aggressive (150)** - Large, complex projects

**Note:** Higher limits allow more complex projects but take longer to generate.

---

## 💡 Usage

1. **Launch:** `streamlit run app.py`
2. **Describe:** "Create a modern to-do app with dark theme"
3. **Generate:** Watch 🧠 Planner → 🏗️ Architect → 💻 Coder work their magic
4. **Download:** Get your complete project as ZIP

### 🎨 Try These Prompts

```
• "Build a colorful calculator with animations"
• "Create a dice rolling game with sound effects" 
• "Design a modern landing page for a startup"
• "Make a to-do app with local storage"
```

---

## 📂 Project Structure

```
architect-ai/
├── agent/
│   ├── __init__.py          # Package initialization
│   ├── graph.py             # LangGraph workflow definition
│   ├── prompts.py           # System and agent prompts
│   ├── states.py            # Pydantic models for state management
│   └── tools.py             # File system tools (read, write, list)
├── .streamlit/
│   └── config.toml          # Streamlit theme configuration
├── generated_projects/      # Your generated projects (with timestamps)
├── app.py                   # Streamlit UI application
├── main.py                  # CLI entry point (optional)
├── pyproject.toml           # Project dependencies and metadata
├── .env                     # Environment variables (create this)
├── .gitignore               # Git ignore rules
└── README.md                # This file
```

---

## 🛠️ Configuration

### Streamlit Configuration

The app uses a custom dark theme defined in `.streamlit/config.toml`. You can customize:
- Colors and styling
- Font family
- Theme preferences

### Recursion Limit

Adjust the recursion limit in the sidebar to control project complexity:
- **Conservative (50)**: Simple projects, faster generation
- **Balanced (100)**: Medium complexity, recommended for most projects
- **Aggressive (150)**: Complex projects, slower but more detailed

### Environment Variables

Create a `.env` file with:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## ⚙️ Tech Stack

**Streamlit** • **LangGraph** • **Groq** • **Pydantic**

**Agent Tools:** `write_file` • `read_file` • `list_files` • `get_current_directory`

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is open source and available for personal and educational use.

---

## 🔧 Quick Fixes

**API Key Issues:** Create `.env` with `GROQ_API_KEY=your_key` • Restart app

**Module Errors:** Activate venv • Reinstall dependencies

**Too Slow:** Lower recursion limit • Simplify prompts

**Port Busy:** Use `--server.port 8502`

---

## 📧 Support

For questions, issues, or suggestions:
- Open an issue on GitHub
- Check the troubleshooting section above

---

## 🙏 Acknowledgments

- Built with [LangGraph](https://github.com/langchain-ai/langgraph) by LangChain
- Powered by [Groq](https://groq.com/) for fast LLM inference
- UI built with [Streamlit](https://streamlit.io/)

---

<div align="center">

**Architect AI** - Autonomous Code Generation
</div>