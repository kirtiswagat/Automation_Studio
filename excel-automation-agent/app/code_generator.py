import streamlit as st
import google.generativeai as genai

class CodeGenerator:
    """Builds prompts and generates Python code using the Gemini API."""
    def __init__(self, action_manager):
        self.action_manager = action_manager
        if 'generated_code' not in st.session_state:
            st.session_state.generated_code = "# Your AI-generated Python code will appear here."

    def build_prompt(self, workflow_steps):
        if not workflow_steps:
            return None

        prompt_lines = [
            "You are an expert Python developer specializing in the pandas library for data manipulation and Excel automation.",
            "Generate a complete, runnable Python script based on the following sequence of actions.",
            "The script should import all necessary libraries and include print statements to show the status after each major step (e.g., after loading data, after filtering, etc.).",
            "The primary DataFrame variable should be named 'df'.",
            "\nWorkflow Steps:",
        ]

        for i, step in enumerate(workflow_steps):
            action = self.action_manager.get_action(step['type'])
            prompt_lines.append(f"\n{i+1}. Action: {action['name']}")
            params = step['params']
            if not action['params']:
                prompt_lines.append("   - This action has no parameters.")
            else:
                for param_config in action['params']:
                    param_id = param_config['id']
                    param_label = param_config['label']
                    param_value = params.get(param_id, 'N/A')
                    prompt_lines.append(f"   - {param_label}: {param_value}")
        
        prompt_lines.append("\nProvide only the Python code as the response. Do not include any explanations, comments, or markdown formatting like ```python.")
        return "\n".join(prompt_lines)

    def generate_code(self, api_key, prompt):
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash-latest')
            response = model.generate_content(prompt)
            
            cleaned_code = response.text.strip()
            # Remove markdown code block formatting if present
            if cleaned_code.startswith("```python"):
                cleaned_code = cleaned_code[len("```python"):].strip()
            if cleaned_code.endswith("```"):
                cleaned_code = cleaned_code[:-3].strip()
            
            st.session_state.generated_code = cleaned_code
            return cleaned_code
        except Exception as e:
            st.session_state.generated_code = f"# Error generating code: {e}"
            return st.session_state.generated_code
