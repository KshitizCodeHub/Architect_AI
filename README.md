# 🛠️ Architect AI - Autonomous Code Generation Agent

<div align="center">

**Transform natural language into complete working projects with an interactive Streamlit interface**

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![LangGraph](https://img.shields.io/badge/LangGraph-0.6.3-green.svg)](https://github.com/langchain-ai/langgraph)
[![Groq](https://img.shields.io/badge/Groq-Powered-orange.svg)](https://groq.com/)

</div>

---

## 📖 Overview

**Architect AI** is a revolutionary autonomous code generation system that transforms natural language descriptions into complete, functional software projects. Built with a stunning Streamlit interface and powered by cutting-edge AI technology, it simulates an entire development team working in harmony.

### 🎯 What Makes Architect AI Special?

- **🧠 Intelligent Multi-Agent System**: Three specialized AI agents (Planner, Architect, Coder) collaborate like a real dev team
- **🎨 Beautiful Real-Time Interface**: Watch your project come to life with smooth animations and live progress tracking
- **📦 Complete Project Generation**: From HTML/CSS/JS apps to Python backends - full projects, not just code snippets
- **⚡ Lightning Fast**: Powered by Groq's ultra-fast inference for near-instant results
- **📥 Instant Downloads**: Get your complete project as a ready-to-deploy ZIP file
- **🎯 Smart Complexity Control**: Adjust project complexity with intelligent recursion limits

Simply describe your vision in plain English - "Create a modern to-do app with dark theme" or "Build a calculator with colorful animations" - and watch Architect AI plan, design, and implement your entire project from scratch!

### 🚀 Perfect For

- **Rapid Prototyping**: Turn ideas into working prototypes in minutes
- **Learning & Education**: See how complete projects are structured and built
- **Client Demos**: Quickly create proof-of-concepts for presentations
- **Side Projects**: Generate fully functional apps without starting from scratch
- **Code Inspiration**: Get fresh perspectives on solving common problems

### ✨ Key Features

- 🎨 **Beautiful Streamlit UI** - Interactive web interface with smooth animations
- 🤖 **Multi-Agent Architecture** - Three specialized AI agents working in harmony
- 📝 **Natural Language Input** - Describe your project in plain English
- 🏗️ **Automated Project Scaffolding** - Creates complete project structures
- 💾 **Real-time Progress Tracking** - Watch agents work with dynamic status indicators
- 📥 **Download Projects as ZIP** - Get your complete project instantly
- 📁 **Unique Project Folders** - Each project saved with timestamp for organization
- 🎯 **Dynamic Examples** - Smart examples that adapt to your complexity settings
- 🔧 **Tool-Augmented Coding** - Uses real file system operations like a human developer
- 🚀 **Powered by Groq** - Lightning-fast inference using state-of-the-art LLMs

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

### 📦 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd architect-ai
   ```

2. **Create and activate a virtual environment**
   
   **Windows (PowerShell):**
   ```powershell
   uv venv
   .venv\Scripts\Activate.ps1
   ```
   
   **macOS/Linux:**
   ```bash
   uv venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install streamlit groq langchain-groq langgraph python-dotenv
   ```

4. **Configure environment variables**
   
   Create a `.env` file in the project root:
   ```bash
   cp .sample_env .env
   ```
   
   Edit `.env` and add your Groq API key:
   ```env
   GROQ_API_KEY=your_api_key_here
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

### Quick Start

1. **Launch the application**
   ```bash
   streamlit run app.py
   ```

2. **Enter your project idea** in the text area
   - Example: "Create a simple calculator web application"

3. **Adjust the recursion limit** using the sidebar slider (if needed)

4. **Click "Generate Project"** and watch the magic happen!

5. **Monitor progress** as agents work:
   - 🧠 **Planner** creates the project plan
   - 🏗️ **Architect** designs the implementation
   - 💻 **Coder** builds your project file by file

6. **Download your project** as a ZIP file when complete

### Example Prompts

Here are some example prompts to get you started:

1. **Web Applications**
   ```
   Create a to-do list application using HTML, CSS, and JavaScript with local storage
   ```

2. **Interactive Tools**
   ```
   Build a simple calculator with a modern UI using vanilla JavaScript
   ```

3. **Games**
   ```
   Create a dice rolling game with colorful animations
   ```

4. **Landing Pages**
   ```
   Design a modern landing page for a tech startup with smooth animations
   ```

### 📥 Downloading Your Project

After generation completes:
1. Click the **"📥 Download Project as ZIP"** button
2. The ZIP file will be downloaded to your browser's download folder
3. Extract and open in your favorite code editor
4. Projects are also saved in `generated_projects/` folder with timestamps

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

## 🔧 Technical Details

### Dependencies

- **Streamlit** - Beautiful web UI framework
- **LangChain & LangGraph** - Agent orchestration and workflow management
- **Groq** - Lightning-fast LLM inference (using `openai/gpt-oss-120b` model)
- **Pydantic** - Data validation and settings management
- **python-dotenv** - Environment variable management

### Agent Tools

The Coder Agent has access to these tools:

- `write_file(path, content)` - Create or overwrite files
- `read_file(path)` - Read file contents
- `list_files(directory)` - List files in a directory
- `get_current_directory()` - Get the current working directory

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

## 🐛 Troubleshooting

### Common Issues

**Issue: "Groq API key not found"**
- Ensure you've created a `.env` file with your `GROQ_API_KEY`
- Verify the API key is valid at [Groq Console](https://console.groq.com/keys)
- Restart the Streamlit app after adding the key

**Issue: "Module not found" errors**
- Make sure your virtual environment is activated
- Reinstall dependencies: `pip install streamlit groq langchain-groq langgraph python-dotenv`

**Issue: "Recursion limit exceeded"**
- Increase the recursion limit using the sidebar slider
- Try simplifying your prompt or breaking it into smaller projects
- Start with Conservative mode (50) for simple projects

**Issue: "Port already in use"**
- Stop any running Streamlit instances
- Or specify a different port: `streamlit run app.py --server.port 8502`

**Issue: "Project generation takes too long"**
- Lower the recursion limit for faster generation
- Use simpler, more specific prompts
- Check your internet connection for Groq API calls

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