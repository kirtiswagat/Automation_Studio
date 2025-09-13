# AI Agent: Excel Automation Designer

This project provides a Streamlit web application that allows users to visually build an Excel data processing workflow. 

The application then uses the Google Gemini API to generate a complete, runnable Python script based on the user's workflow.

# Project Structure

The project has been refactored into a modular structure for better organization and scalability:
```
excel-automation-agent/
|
|-- app/                    # Main application package
|   |-- __init__.py         # Makes 'app' a Python package
|   |-- main.py             # Main app orchestrator (StreamlitApp class)
|   |-- action_manager.py   # Manages action definitions (ActionManager class)
|   |-- code_generator.py   # Handles Gemini API interaction (CodeGenerator class)
|   |-- ui.py               # Manages all Streamlit UI components (UIManager class)
|   |-- workflow_manager.py # Manages the user's workflow state (WorkflowManager class)
|
|-- .gitignore              # Standard Python gitignore
|-- requirements.txt        # Project dependencies
|-- run.py                  # The main entry point to run the application
```
# How to Run
1. Clone the repository and navigate to the root directory (excel-automation-agent/).

2. Create a virtual environment (recommended):

```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the application:
   ```
   streamlit run run.py
   ```
Your web browser will open with the application running. You will need to provide your Google API Key in the sidebar to enable code generation.

# Demo (Watch Out the Youtube)
```
<iframe width="560" height="315" src="https://www.youtube.com/embed/CtiRyDyZoSU?si=Pz7Ssu14mTBRWYiH" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
```

