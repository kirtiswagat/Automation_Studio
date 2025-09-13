import streamlit as st
from .action_manager import ActionManager
from .workflow_manager import WorkflowManager
from .code_generator import CodeGenerator
from .ui import UIManager

class StreamlitApp:
    """
    The main class that orchestrates the application by initializing
    and coordinating the different managers (Action, Workflow, Code, UI).
    """
    def __init__(self):
        st.set_page_config(
            page_title="AI Agent: Excel Automation Designer",
            page_icon="🤖",
            layout="wide"
        )
        self.action_manager = ActionManager()
        self.workflow_manager = WorkflowManager()
        self.code_generator = CodeGenerator(self.action_manager)
        self.ui_manager = UIManager(self.action_manager, self.workflow_manager, self.code_generator)

    def run(self):
        """Renders the main layout of the Streamlit application."""
        self.ui_manager.render_main_layout()
