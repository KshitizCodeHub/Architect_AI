import streamlit as st
import time
import os
import zipfile
import io
from agent.graph import agent
from agent.tools import init_project_root

def create_project_zip(project_path):
    """Create a ZIP file containing all project files"""
    zip_buffer = io.BytesIO()
    
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        # Walk through all files in the project directory
        for root, dirs, files in os.walk(project_path):
            for file in files:
                file_path = os.path.join(root, file)
                # Create archive name (relative path from project root)
                arcname = os.path.relpath(file_path, project_path)
                zip_file.write(file_path, arcname)
    
    zip_buffer.seek(0)
    return zip_buffer.getvalue()

# Page config
st.set_page_config(
    page_title="Architect AI - Autonomous Code Generator",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for dark sleek theme - Enhanced version
st.markdown("""
<style>
    /* Only hide the menu and footer - leave header completely alone */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Make header transparent but keep minimal space */
    header[data-testid="stHeader"] {
        background: transparent !important;
        height: 60px !important;
        min-height: 60px !important;
        padding: 0px !important;
    }
    
    /* Add top padding to main content so it's not cut off */
    .main .block-container {
        padding-top: 2rem !important;
        transition: all 0.3s ease !important;
    }
    
    /* Smooth page transitions */
    .stApp {
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    
    /* Enhanced main content area */
    .main {
        transition: margin-left 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    
    /* Ensure main content takes full width when sidebar is collapsed */
    .stApp:not(:has([data-testid="stSidebar"][aria-expanded="true"])) .main {
        margin-left: 0px !important;
    }
    
    /* Smooth form animations */
    .stTextArea textarea {
        transition: all 0.2s ease !important;
    }
    
    .stTextArea textarea:focus {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(0, 212, 255, 0.2) !important;
    }
    
    /* Clean sidebar styling */
    [data-testid="stSidebar"] {
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        min-width: 280px !important;
        max-width: 320px !important;
    }
    
    [data-testid="stSidebar"] > div {
        padding: 1rem 1.5rem !important;
    }
    
    /* Hide the sidebar collapse area text */
    [data-testid="stSidebar"] .css-1d391kg, 
    [data-testid="stSidebar"] .css-17eq0hr {
        display: none !important;
    }
    
    /* Clean sidebar background */
    [data-testid="stSidebar"] .css-1lcbmhc {
        background: rgba(26, 26, 46, 0.95) !important;
        backdrop-filter: blur(20px) !important;
    }
    
    /* Hide sidebar vertical text when collapsed */
    [data-testid="stSidebar"][aria-expanded="false"] {
        width: 0px !important;
        min-width: 0px !important;
        padding: 0px !important;
        overflow: hidden !important;
    }
    
    [data-testid="stSidebar"][aria-expanded="false"] > div {
        display: none !important;
    }
    
    /* Hide any remaining sidebar artifacts */
    .css-1rs6os, .css-17eq0hr, .css-1d391kg {
        display: none !important;
    }
    
    /* Keep sidebar toggle visible and styled with smooth animations */
    button[data-testid="collapsedControl"] {
        position: fixed !important;
        top: 15px !important;
        left: 15px !important;
        z-index: 1000 !important;
        background: linear-gradient(135deg, #00d4ff, #7b2cbf) !important;
        border: none !important;
        border-radius: 50% !important;
        color: white !important;
        font-size: 16px !important;
        width: 45px !important;
        height: 45px !important;
        box-shadow: 0 4px 20px rgba(0, 212, 255, 0.3) !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        backdrop-filter: blur(10px) !important;
    }
    
    button[data-testid="collapsedControl"]:hover {
        transform: scale(1.15) rotate(5deg) !important;
        box-shadow: 0 8px 25px rgba(123, 44, 191, 0.5) !important;
        background: linear-gradient(135deg, #7b2cbf, #00d4ff) !important;
    }
    
    button[data-testid="collapsedControl"]:active {
        transform: scale(0.95) !important;
        transition: all 0.1s ease !important;
    }
    
    /* Enhanced progress bar styling */
    .stProgress .st-bo {
        background: linear-gradient(90deg, #00d4ff, #7b2cbf) !important;
        border-radius: 10px !important;
        height: 8px !important;
        transition: all 0.3s ease !important;
    }
    
    .stProgress {
        background: rgba(255, 255, 255, 0.1) !important;
        border-radius: 10px !important;
        overflow: hidden !important;
    }
    
    /* Smooth metric animations */
    [data-testid="metric-container"] {
        transition: all 0.2s ease !important;
    }
    
    [data-testid="metric-container"]:hover {
        transform: translateY(-2px) !important;
        background: rgba(0, 212, 255, 0.05) !important;
        border-radius: 8px !important;
    }
    
    /* Remove anchor links */
    .stMarkdown h1 a, .stMarkdown h2 a, .stMarkdown h3 a {display: none !important;}
    
    /* Main background with animated gradient */
    .stApp {
        background: #0a0a0a;
        background-image: 
            radial-gradient(at 40% 20%, rgba(0, 212, 255, 0.08) 0px, transparent 50%),
            radial-gradient(at 80% 0%, rgba(123, 44, 191, 0.08) 0px, transparent 50%),
            radial-gradient(at 20% 80%, rgba(0, 212, 255, 0.04) 0px, transparent 50%);
        animation: gradientShift 15s ease infinite;
    }
    
    @keyframes gradientShift {
        0%, 100% {
            background-position: 0% 0%;
        }
        50% {
            background-position: 100% 100%;
        }
    }
    
    /* Container - centered */
    .block-container {
        max-width: 900px !important;
        padding: 3rem 2rem !important;
        animation: fadeIn 0.6s ease-out;
    }
    
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a1a 0%, #0f0f0f 100%);
        border-right: 1px solid #2a2a2a;
    }
    
    /* Title with glow effect */
    .main-title {
        font-size: 3.5rem !important;
        font-weight: 900 !important;
        background: linear-gradient(90deg, #00d4ff 0%, #7b2cbf 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        line-height: 1.1 !important;
        animation: titleGlow 3s ease-in-out infinite;
        filter: drop-shadow(0 0 30px rgba(0, 212, 255, 0.3));
    }
    
    @keyframes titleGlow {
        0%, 100% {
            filter: drop-shadow(0 0 30px rgba(0, 212, 255, 0.3));
        }
        50% {
            filter: drop-shadow(0 0 40px rgba(123, 44, 191, 0.4));
        }
    }
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        line-height: 1.1 !important;
    }
    
    .subtitle {
        font-size: 0.85rem !important;
        color: #666 !important;
        letter-spacing: 3px !important;
        text-transform: uppercase;
        text-align: center;
        margin-bottom: 3rem !important;
        animation: fadeIn 0.8s ease-out 0.3s backwards;
    }
    
    /* Text area with better focus state */
    .stTextArea {
        margin-bottom: 1.5rem;
    }
    
    .stTextArea textarea {
        background: #141414 !important;
        color: #fff !important;
        border: 1px solid #2a2a2a !important;
        border-radius: 14px !important;
        padding: 20px !important;
        font-size: 15px !important;
        min-height: 140px !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
        line-height: 1.6 !important;
    }
    
    .stTextArea textarea:focus {
        border-color: #00d4ff !important;
        box-shadow: 0 0 0 1px #00d4ff, 0 0 25px rgba(0, 212, 255, 0.2) !important;
        background: #1a1a1a !important;
        transform: translateY(-2px);
    }
    
    .stTextArea textarea::placeholder {
        color: #555 !important;
        font-style: italic;
    }
    
    /* Enhanced buttons with ripple effect */
    .stButton > button {
        width: 100% !important;
        background: linear-gradient(135deg, #00d4ff 0%, #7b2cbf 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 18px 32px !important;
        font-weight: 600 !important;
        font-size: 15px !important;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        box-shadow: 0 4px 20px rgba(0, 212, 255, 0.3) !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.3);
        transform: translate(-50%, -50%);
        transition: width 0.6s, height 0.6s;
    }
    
    .stButton > button:hover::before {
        width: 300px;
        height: 300px;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.02) !important;
        box-shadow: 0 8px 35px rgba(0, 212, 255, 0.5) !important;
    }
    
    .stButton > button:active {
        transform: translateY(0) scale(0.98) !important;
    }
    
    /* Enhanced metrics with hover effect */
    [data-testid="stMetric"] {
        background: linear-gradient(135deg, #141414 0%, #1a1a1a 100%);
        border: 1px solid #2a2a2a;
        border-radius: 14px;
        padding: 1.5rem;
        text-align: center;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        cursor: default;
    }
    
    [data-testid="stMetric"]:hover {
        transform: translateY(-5px) scale(1.05);
        border-color: #00d4ff;
        box-shadow: 0 10px 30px rgba(0, 212, 255, 0.2);
        background: linear-gradient(135deg, #1a1a1a 0%, #141414 100%);
    }
    
    [data-testid="stMetricValue"] {
        color: #00d4ff !important;
        font-size: 2.2rem !important;
        font-weight: 800 !important;
        text-shadow: 0 0 20px rgba(0, 212, 255, 0.3);
    }
    
    [data-testid="stMetricLabel"] {
        color: #888 !important;
        font-size: 0.75rem !important;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        font-weight: 600;
    }
    
    /* Enhanced alerts with icons and animations */
    .stAlert {
        border-radius: 14px !important;
        border: 1px solid #2a2a2a !important;
        padding: 1.3rem 1.7rem !important;
        animation: slideIn 0.4s ease-out;
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateX(-20px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    .stInfo {
        background: linear-gradient(135deg, #0a1929 0%, #0d1b2a 100%) !important;
        border-left: 4px solid #00d4ff !important;
    }
    
    .stSuccess {
        background: linear-gradient(135deg, #0a2917 0%, #0d2118 100%) !important;
        border-left: 4px solid #00ff88 !important;
        animation: successPulse 0.6s ease-out;
    }
    
    @keyframes successPulse {
        0% {
            transform: scale(0.95);
        }
        50% {
            transform: scale(1.02);
        }
        100% {
            transform: scale(1);
        }
    }
    
    .stWarning {
        background: linear-gradient(135deg, #2a2310 0%, #221c0d 100%) !important;
        border-left: 4px solid #ffaa00 !important;
    }
    
    .stError {
        background: linear-gradient(135deg, #2a1010 0%, #220d0d 100%) !important;
        border-left: 4px solid #ff3366 !important;
        animation: shake 0.5s ease-out;
    }
    
    @keyframes shake {
        0%, 100% {transform: translateX(0);}
        25% {transform: translateX(-10px);}
        75% {transform: translateX(10px);}
    }
    
    /* Enhanced progress bar with pulse */
    .stProgress > div > div {
        background: linear-gradient(90deg, #00d4ff 0%, #7b2cbf 50%, #00d4ff 100%) !important;
        background-size: 200% 100%;
        animation: progressShine 2s ease-in-out infinite;
        height: 8px !important;
        border-radius: 10px !important;
    }
    
    @keyframes progressShine {
        0% {
            background-position: 200% 0;
        }
        100% {
            background-position: -200% 0;
        }
    }
    
    .stProgress > div {
        background: #1a1a1a !important;
        border-radius: 10px !important;
        overflow: hidden;
    }
    
    /* Enhanced code blocks */
    code {
        background: linear-gradient(135deg, #141414 0%, #1a1a1a 100%) !important;
        color: #00d4ff !important;
        padding: 4px 10px !important;
        border-radius: 8px !important;
        border: 1px solid #2a2a2a;
        font-family: 'Fira Code', 'Consolas', 'Monaco', monospace !important;
        font-size: 13px !important;
        transition: all 0.2s ease;
    }
    
    code:hover {
        border-color: #00d4ff;
        box-shadow: 0 0 15px rgba(0, 212, 255, 0.2);
    }
    
    pre {
        background: linear-gradient(135deg, #141414 0%, #1a1a1a 100%) !important;
        border: 1px solid #2a2a2a !important;
        border-radius: 14px !important;
        padding: 1.5rem !important;
        transition: all 0.3s ease;
    }
    
    pre:hover {
        border-color: #00d4ff;
        box-shadow: 0 5px 20px rgba(0, 212, 255, 0.15);
    }
    
    /* Sidebar buttons with better hover */
    [data-testid="stSidebar"] .stButton > button {
        background: #1a1a1a !important;
        color: #00d4ff !important;
        border: 1px solid #2a2a2a !important;
        font-size: 13px !important;
        text-transform: none;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    [data-testid="stSidebar"] .stButton > button:hover {
        background: linear-gradient(135deg, #2a2a2a 0%, #1f1f1f 100%) !important;
        border-color: #00d4ff !important;
        transform: translateX(5px) !important;
        box-shadow: -3px 0 10px rgba(0, 212, 255, 0.3) !important;
    }
    
    /* Enhanced scrollbar */
    ::-webkit-scrollbar {width: 10px; height: 10px;}
    ::-webkit-scrollbar-track {
        background: #0a0a0a;
        border-radius: 5px;
    }
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #2a2a2a 0%, #1a1a1a 100%);
        border-radius: 5px;
        border: 2px solid #0a0a0a;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, #00d4ff 0%, #7b2cbf 100%);
    }
    
    /* Enhanced expander */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #141414 0%, #1a1a1a 100%) !important;
        border: 1px solid #2a2a2a !important;
        border-radius: 12px !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        padding: 1rem !important;
    }
    
    .streamlit-expanderHeader:hover {
        border-color: #00d4ff !important;
        transform: translateX(5px);
        box-shadow: -3px 0 15px rgba(0, 212, 255, 0.2);
    }
    
    /* Loading spinner enhancement */
    .stSpinner > div {
        border-top-color: #00d4ff !important;
        border-right-color: #7b2cbf !important;
        animation: spin 0.8s linear infinite;
    }
    
    /* Tooltip-like effect for headers */
    .section-header {
        position: relative;
        display: inline-block;
    }
    
    .section-header::after {
        content: '';
        position: absolute;
        bottom: -4px;
        left: 0;
        width: 0;
        height: 2px;
        background: linear-gradient(90deg, #00d4ff 0%, #7b2cbf 100%);
        transition: width 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .section-header:hover::after {
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)



# Initialize session state
if 'project_generated' not in st.session_state:
    st.session_state.project_generated = False
if 'generation_time' not in st.session_state:
    st.session_state.generation_time = 0
if 'result' not in st.session_state:
    st.session_state.result = None
if 'prompt_input' not in st.session_state:
    st.session_state.prompt_input = ""

# Header
st.markdown("""
<div style="text-align: center; margin-bottom: 3rem;">
    <div class="main-title">🛠️ ARCHITECT AI</div>
    <div class="subtitle">Autonomous Code Generation Agent</div>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown('<p style="font-size: 1.3rem; color: #e0e0e0; font-weight: 700;">⚙️ Settings</p>', unsafe_allow_html=True)
    
    recursion_limit = st.slider("Recursion Limit", 50, 200, 100, 10, 
                               help="Controls AI decision steps: Lower = Faster/Simpler, Higher = More Complex/Detailed")
    
    # Store in session state for dynamic examples
    st.session_state.recursion_limit = recursion_limit
    
    # Add helpful explanation
    if recursion_limit <= 75:
        st.caption("🚀 **Fast Mode** - Quick, simple projects")
    elif recursion_limit <= 125:
        st.caption("⚖️ **Balanced** - Good for most projects")
    else:
        st.caption("🔥 **Complex Mode** - Detailed, feature-rich projects")
    
    st.markdown("---")
    st.markdown('<p style="font-size: 1.3rem; color: #e0e0e0; font-weight: 700;">📊 Info</p>', unsafe_allow_html=True)
    st.info("""
    **Architect AI** uses a 3-agent workflow:
    - 🧠 **Planner**: Analyzes your request
    - 🏗️ **Architect**: Creates tasks
    - 💻 **Coder**: Writes code
    """)
    
    st.markdown("---")
    st.markdown('<p style="font-size: 1.2rem; color: #e0e0e0; font-weight: 700; margin-bottom: 0.5rem;">💡 Examples</p>', unsafe_allow_html=True)
    
    # Dynamic examples based on recursion limit
    if recursion_limit <= 75:
        # Fast Mode - Simple projects
        examples = [
            ("🧮 Calculator", "Create a simple calculator with HTML, CSS, and JavaScript"),
            ("📝 Todo List", "Build a basic todo list with local storage"),
            ("🎲 Dice Game", "Create a simple dice rolling game")
        ]
    elif recursion_limit <= 125:
        # Balanced Mode - Moderate complexity
        examples = [
            ("🧮 Calculator", "Create a calculator web app with HTML, CSS, and JavaScript with memory functions"),
            ("📝 Todo List", "Build a todo list app with local storage, filters, and edit functionality"),
            ("🔌 REST API", "Create a FastAPI REST API with SQLite database and basic CRUD operations")
        ]
    else:
        # Complex Mode - Advanced projects
        examples = [
            ("🧮 Calculator", "Create an advanced calculator with HTML, CSS, and JavaScript featuring scientific functions, history, and keyboard support"),
            ("📝 Todo List", "Build a comprehensive todo list app with local storage, categories, due dates, search, and import/export features"),
            ("🔌 REST API", "Create a complete FastAPI REST API with SQLite database, authentication, data validation, and API documentation")
        ]
    
    # Custom CSS for compact example buttons
    st.markdown("""
    <style>
    .compact-example {
        margin: 0.3rem 0 !important;
        padding: 0.4rem 0.8rem !important;
        font-size: 0.85rem !important;
        background: linear-gradient(45deg, rgba(0, 212, 255, 0.1), rgba(123, 44, 191, 0.1)) !important;
        border: 1px solid rgba(0, 212, 255, 0.3) !important;
        border-radius: 8px !important;
        transition: all 0.2s ease !important;
        width: 100% !important;
    }
    .compact-example:hover {
        background: linear-gradient(45deg, rgba(0, 212, 255, 0.2), rgba(123, 44, 191, 0.2)) !important;
        border-color: rgba(0, 212, 255, 0.5) !important;
        transform: translateY(-1px) !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    for i, (short, full) in enumerate(examples):
        if st.button(short, key=f"ex_{i}", help=full):
            st.session_state.prompt_input = full

# Show sidebar button if not visible
if not st.session_state.get('sidebar_visible', True):
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <p style="color: #00d4ff; font-size: 1rem; margin-bottom: 1rem;">
            📝 Need examples? Click below to show sidebar with quick project templates
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("📝 Show Examples Sidebar", key="show_sidebar", type="secondary"):
            st.rerun()

# Quick examples when sidebar is not visible
if not st.session_state.get('sidebar_visible', True):
    # Get current recursion limit for dynamic examples
    current_recursion = st.session_state.get('recursion_limit', 100)
    
    # Dynamic examples based on recursion limit
    if current_recursion <= 75:
        # Fast Mode - Simple projects
        main_examples = [
            ("🧮", "Create a simple calculator with HTML, CSS, and JavaScript"),
            ("📝", "Build a basic todo list with local storage"),
            ("🎲", "Create a simple dice rolling game")
        ]
    elif current_recursion <= 125:
        # Balanced Mode - Moderate complexity
        main_examples = [
            ("🧮", "Create a calculator web app with HTML, CSS, and JavaScript with memory functions"),
            ("📝", "Build a todo list app with local storage, filters, and edit functionality"),
            ("🔌", "Create a FastAPI REST API with SQLite database and basic CRUD operations")
        ]
    else:
        # Complex Mode - Advanced projects
        main_examples = [
            ("🧮", "Create an advanced calculator with HTML, CSS, and JavaScript featuring scientific functions, history, and keyboard support"),
            ("📝", "Build a comprehensive todo list app with local storage, categories, due dates, search, and import/export features"),
            ("🔌", "Create a complete FastAPI REST API with SQLite database, authentication, data validation, and API documentation")
        ]
    
    # Adjust columns based on number of examples
    cols = st.columns(len(main_examples), gap="small")
    for i, (icon, full) in enumerate(main_examples):
        with cols[i]:
            if st.button(icon, key=f"quick_ex_{i}", help=full, use_container_width=True):
                st.session_state.prompt_input = full

# Main input
st.markdown('<p style="font-size: 1.3rem; color: #e0e0e0; font-weight: 700; text-align: center; margin-bottom: 1rem;">What do you want to build?</p>', unsafe_allow_html=True)

user_prompt = st.text_area(
    "Project Description",
    value=st.session_state.prompt_input,
    height=140,
    placeholder="e.g., Create a modern todo app with HTML, CSS, and JavaScript with dark mode toggle...",
    label_visibility="collapsed"
)

generate_button = st.button("✨ Generate Project", type="primary")

if generate_button and user_prompt:
    with st.spinner("🔄 Planning, architecting, and coding your project..."):
        start_time = time.time()
        
        # Initialize project root with unique folder
        project_root = init_project_root(user_prompt)
        
        # Progress tracking with interactive indicators
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Create status indicators container
        status_container = st.container()
        with status_container:
            col1, col2, col3 = st.columns(3)
            with col1:
                planner_status = st.empty()
            with col2:
                architect_status = st.empty()
            with col3:
                coder_status = st.empty()
        
        try:
            # Initialize status indicators
            planner_status.markdown("⏳ **Planner** - Starting...")
            architect_status.markdown("⏸️ **Architect** - Waiting...")
            coder_status.markdown("⏸️ **Coder** - Waiting...")
            
            # Phase 1: Planning with dynamic updates
            planner_status.markdown("🔄 **Planner** - Analyzing request...")
            status_text.text("🧠 Planner Agent: Analyzing your request...")
            progress_bar.progress(5)
            time.sleep(0.2)
            
            planner_status.markdown("🔄 **Planner** - Understanding requirements...")
            status_text.text("🧠 Planner Agent: Understanding project requirements...")
            progress_bar.progress(10)
            time.sleep(0.3)
            
            planner_status.markdown("🔄 **Planner** - Identifying technologies...")
            status_text.text("🧠 Planner Agent: Identifying technologies needed...")
            progress_bar.progress(15)
            time.sleep(0.2)
            
            planner_status.markdown("✅ **Planner** - Complete!")
            status_text.text("🧠 Planner Agent: Creating project structure...")
            progress_bar.progress(20)
            
            # Phase 2: Architecture with dynamic updates
            architect_status.markdown("🔄 **Architect** - Breaking down tasks...")
            status_text.text("🏗️ Architect Agent: Breaking down into tasks...")
            progress_bar.progress(25)
            time.sleep(0.3)
            
            architect_status.markdown("🔄 **Architect** - Planning dependencies...")
            status_text.text("🏗️ Architect Agent: Planning file dependencies...")
            progress_bar.progress(30)
            time.sleep(0.2)
            
            architect_status.markdown("✅ **Architect** - Complete!")
            status_text.text("🏗️ Architect Agent: Organizing implementation steps...")
            progress_bar.progress(35)
            time.sleep(0.3)
            
            # Run the agent
            status_text.text("🤖 AI Agent: Starting project generation...")
            progress_bar.progress(40)
            
            result = agent.invoke(
                {"user_prompt": user_prompt},
                {"recursion_limit": recursion_limit}
            )
            
            # Phase 3: Coding with dynamic updates
            coder_status.markdown("🔄 **Coder** - Creating HTML...")
            status_text.text("💻 Coder Agent: Creating HTML structure...")
            progress_bar.progress(50)
            time.sleep(0.4)
            
            coder_status.markdown("🔄 **Coder** - Writing CSS...")
            status_text.text("💻 Coder Agent: Writing CSS styles...")
            progress_bar.progress(65)
            time.sleep(0.3)
            
            coder_status.markdown("🔄 **Coder** - JavaScript logic...")
            status_text.text("💻 Coder Agent: Implementing JavaScript logic...")
            progress_bar.progress(80)
            time.sleep(0.4)
            
            coder_status.markdown("🔄 **Coder** - Documentation...")
            status_text.text("📝 Coder Agent: Generating documentation...")
            progress_bar.progress(90)
            time.sleep(0.2)
            
            coder_status.markdown("✅ **Coder** - Complete!")
            status_text.text("✨ Finalizing project files...")
            progress_bar.progress(95)
            
            end_time = time.time()
            generation_time = end_time - start_time
            
            progress_bar.progress(100)
            status_text.text("🎉 Project generated successfully!")
            
            # Success animation effect
            st.balloons()
            time.sleep(0.3)
            
            # Store results
            st.session_state.project_generated = True
            st.session_state.generation_time = generation_time
            st.session_state.result = result
            
            # Success message
            st.success(f"🎉 Project generated in {generation_time:.2f} seconds!")
            
            # Metrics
            st.markdown('<p style="font-size: 1.1rem; color: #00d4ff; font-weight: 700; margin-top: 1.5rem;">📊 Generation Metrics</p>', unsafe_allow_html=True)
            
            plan = result.get('plan')
            col_m1, col_m2, col_m3 = st.columns(3)
            
            with col_m1:
                st.metric("⏱️ Time", f"{generation_time:.1f}s")
            with col_m2:
                # Count actual files created in the project directory
                files_count = 0
                if os.path.exists(project_root):
                    files_count = sum([len(files) for r, d, files in os.walk(project_root)])
                elif plan and hasattr(plan, 'files'):
                    files_count = len(plan.files)  # Fallback to plan if project dir doesn't exist yet
                st.metric("📄 Files", files_count)
            with col_m3:
                estimated_tokens = len(user_prompt) * 50
                tokens_per_sec = int(estimated_tokens / generation_time) if generation_time > 0 else 0
                st.metric("⚡ Speed", f"{tokens_per_sec} t/s")
            
            # Files
            st.markdown('<p style="font-size: 1.1rem; color: #00d4ff; font-weight: 700; margin-top: 1.5rem;">📁 Generated Files</p>', unsafe_allow_html=True)
            if plan and hasattr(plan, 'files'):
                for file in plan.files:
                    st.markdown(f"- `{file.path}` - {file.purpose}")
            
            # Location
            st.markdown('<p style="font-size: 1.1rem; color: #00d4ff; font-weight: 700; margin-top: 1.5rem;">📂 Project Location</p>', unsafe_allow_html=True)
            st.code(project_root, language="bash")
            
            # Download button
            st.markdown('<p style="font-size: 1.1rem; color: #00d4ff; font-weight: 700; margin-top: 1.5rem;">📥 Download Project</p>', unsafe_allow_html=True)
            try:
                if os.path.exists(project_root) and os.listdir(project_root):
                    zip_data = create_project_zip(project_root)
                    project_name = user_prompt.replace(" ", "_").replace(",", "")[:30]  # Clean filename
                    st.download_button(
                        label="📦 Download ZIP File",
                        data=zip_data,
                        file_name=f"{project_name}_project.zip",
                        mime="application/zip",
                        type="primary"
                    )
                    st.success("✅ Your project is ready for download!")
                else:
                    st.warning("⚠️ No files were generated to download.")
            except Exception as e:
                st.error(f"❌ Error creating download: {str(e)}")
            
            # Next steps
            st.markdown('<p style="font-size: 1.1rem; color: #00d4ff; font-weight: 700; margin-top: 1.5rem;">🎯 Next Steps</p>', unsafe_allow_html=True)
            st.markdown("""
            1. **Download the ZIP file** using the button above
            2. **Extract** the ZIP file to your desired location
            3. **Open `index.html`** in a browser (for web projects)
            4. **Or run** the appropriate command for your project type
            """)
            
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            progress_bar.progress(0)
            status_text.text("")

elif generate_button and not user_prompt:
    st.warning("⚠️ Please enter a project description first!")

# Footer
with st.expander("📈 System Information", expanded=False):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **Model Configuration**
        - Model: Groq (openai/gpt-oss-120b)
        - Framework: LangGraph
        - Agents: 3 (Planner, Architect, Coder)
        """)
    with col2:
        st.markdown("""
        **Capabilities**
        - File Operations: 4 tools
        - Pattern: ReAct (Reasoning + Acting)
        - Speed: 300+ tokens/second
        """)

st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 20px;'>
    <p style='color: #666; font-size: 0.9rem;'>
        Built with ❤️ using <span style='color: #00d4ff;'>LangGraph</span> & <span style='color: #00d4ff;'>Groq</span>
    </p>
    <p style='color: #999; font-size: 0.8rem; margin-top: 10px;'>
        <strong style='background: linear-gradient(90deg, #00d4ff 0%, #7b2cbf 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>
            Architect AI
        </strong> - Transforming Ideas into Code
    </p>
</div>
""", unsafe_allow_html=True)
