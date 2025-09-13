import streamlit as st

class UIManager:
    """The main class for rendering the Streamlit UI."""
    def __init__(self, action_manager, workflow_manager, code_generator):
        self.action_manager = action_manager
        self.workflow_manager = workflow_manager
        self.code_generator = code_generator

    def _render_sidebar(self):
        with st.sidebar:
            st.header("🔑 API Configuration")
            self.google_api_key = st.text_input("Enter your Google API Key", type="password", help="Get your key from Google AI Studio.")
            
            st.divider()

            st.header("Add a Step")
            action_options = {
                key: f"{details['icon']} {details['name']} ({category})"
                for category, actions in self.action_manager.action_categories.items()
                for key, details in actions.items()
            }

            selected_action_key = st.selectbox(
                "Choose an action to add to your workflow:",
                options=list(action_options.keys()),
                format_func=lambda x: action_options[x]
            )
            
            st.button(
                "Add Step to Workflow",
                on_click=self.workflow_manager.add_step,
                args=(selected_action_key, self.action_manager),
                use_container_width=True
            )

    def _render_workflow_panel(self):
        with st.container():
            st.header("📋 Your Workflow")
            if not self.workflow_manager.steps:
                st.info("Your workflow is empty. Add a step from the sidebar to get started.")
            
            for i, step in enumerate(self.workflow_manager.steps):
                action = self.action_manager.get_action(step['type'])
                with st.container(border=True):
                    st.subheader(f"Step {i+1}: {action['icon']} {action['name']}")
                    
                    for param in action['params']:
                        param_key = f"{param['id']}_{step['id']}"
                        if param['type'] == 'text_input':
                            step['params'][param['id']] = st.text_input(param['label'], value=step['params'].get(param['id'], ''), placeholder=param['placeholder'], key=param_key)
                        elif param['type'] == 'selectbox':
                             step['params'][param['id']] = st.selectbox(param['label'], options=param['options'], index=param['options'].index(step['params'].get(param['id'])) if step['params'].get(param['id']) in param['options'] else 0, key=param_key)
                        elif param['type'] == 'checkbox':
                            step['params'][param['id']] = st.checkbox(param['label'], value=step['params'].get(param['id'], False), key=param_key)

                    btn_cols = st.columns(4)
                    with btn_cols[0]:
                        st.button("⬆️ Up", key=f"up_{step['id']}", on_click=self.workflow_manager.move_step, args=(step['id'], 'up'), use_container_width=True, disabled=(i==0))
                    with btn_cols[1]:
                        st.button("⬇️ Down", key=f"down_{step['id']}", on_click=self.workflow_manager.move_step, args=(step['id'], 'down'), use_container_width=True, disabled=(i == len(self.workflow_manager.steps) - 1))
                    with btn_cols[3]:
                         st.button("❌ Remove", key=f"del_{step['id']}", on_click=self.workflow_manager.remove_step, args=(step['id'],), type="primary", use_container_width=True)

    def _render_code_panel(self):
        with st.container():
            st.header("🐍 AI-Generated Python Code")
    
            if st.button("🚀 Generate Code with Gemini AI", use_container_width=True, type="primary"):
                if not self.google_api_key:
                    st.warning("Please enter your Google API Key in the sidebar to generate code.")
                elif not self.workflow_manager.steps:
                    st.warning("Please add at least one step to your workflow before generating code.")
                else:
                    prompt = self.code_generator.build_prompt(self.workflow_manager.steps)
                    with st.spinner("🤖 Calling Gemini to generate your code..."):
                        self.code_generator.generate_code(self.google_api_key, prompt)

            st.code(st.session_state.generated_code, language="python")

            st.download_button(
                label="📥 Download Python Script",
                data=st.session_state.generated_code,
                file_name="ai_generated_script.py",
                mime="text/python",
                use_container_width=True
            )

    def render_main_layout(self):
        st.title("🤖 AI Agent: Excel Automation Designer")
        st.markdown("Visually build your Excel data processing workflow and let Gemini generate the Python script for you.")

        self._render_sidebar()

        col1, col2 = st.columns((1, 1), gap="large")
        with col1:
            self._render_workflow_panel()
        with col2:
            self._render_code_panel()
