import streamlit as st
import uuid

class WorkflowManager:
    """Manages the sequence of steps in the user's workflow."""
    def __init__(self):
        if 'workflow_steps' not in st.session_state:
            st.session_state.workflow_steps = []
        self.steps = st.session_state.workflow_steps

    def add_step(self, action_key, action_manager):
        step_id = str(uuid.uuid4())
        action = action_manager.get_action(action_key)
        if not action:
            return

        new_step = {"id": step_id, "type": action_key, "params": {}}
        # Initialize default params
        for param in action["params"]:
            if param['type'] == 'checkbox':
                new_step['params'][param['id']] = param.get('default', False)
            elif param['type'] == 'selectbox':
                new_step['params'][param['id']] = param['options'][0]
            else:
                new_step['params'][param['id']] = ""
        self.steps.append(new_step)

    def remove_step(self, step_id):
        st.session_state.workflow_steps = [s for s in self.steps if s['id'] != step_id]

    def move_step(self, step_id, direction):
        try:
            idx = [i for i, s in enumerate(self.steps) if s['id'] == step_id][0]
            if direction == 'up' and idx > 0:
                self.steps.insert(idx - 1, self.steps.pop(idx))
            elif direction == 'down' and idx < len(self.steps) - 1:
                self.steps.insert(idx + 1, self.steps.pop(idx))
        except IndexError:
            st.error("Could not move the step.")
