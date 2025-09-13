class ActionManager:
    """Manages the definitions and retrieval of all available actions."""
    def __init__(self):
        self.action_categories = {
            "File Operations": {
                "read_excel": {
                    "name": "Read Excel to DataFrame",
                    "icon": "📄",
                    "params": [
                        {"id": "path", "label": "File Path", "type": "text_input", "placeholder": "e.g., C:/data/sales.xlsx"},
                        {"id": "sheet_name", "label": "Sheet Name (optional)", "type": "text_input", "placeholder": "e.g., Sheet1 or 0"}
                    ]
                },
                "df_to_excel": {
                    "name": "Save DataFrame to Excel",
                    "icon": "💾",
                    "params": [
                        {"id": "path", "label": "File Path", "type": "text_input", "placeholder": "e.g., C:/data/output.xlsx"},
                        {"id": "sheet_name", "label": "Sheet Name", "type": "text_input", "placeholder": "e.g., Report"},
                        {"id": "index", "label": "Include Index", "type": "checkbox"}
                    ]
                },
            },
            "Data Cleaning": {
                "sanitize_columns": {"name": "Sanitize Column Names", "icon": "✨", "params": []},
                "remove_nulls": {"name": "Remove Null Rows", "icon": "🗑️", "params": []},
                "fill_nulls": {
                    "name": "Fill Null Values",
                    "icon": "💧",
                    "params": [{"id": "value", "label": "Fill with Value", "type": "text_input", "placeholder": "e.g., 0 or N/A"}]
                },
                "drop_duplicates": {"name": "Remove Duplicate Rows", "icon": "👥", "params": []},
            },
            "Filtering & Sorting": {
                "filter_rows": {
                    "name": "Filter Rows",
                    "icon": "🔍",
                    "params": [
                        {"id": "column", "label": "Column", "type": "text_input", "placeholder": "e.g., Sales"},
                        {"id": "operator", "label": "Operator", "type": "selectbox", "options": ['==', '!=', '>', '<', '>=', '<=', 'contains']},
                        {"id": "value", "label": "Value", "type": "text_input", "placeholder": 'e.g., 100 or "USA"'}
                    ]
                },
                "select_columns": {
                    "name": "Select Columns",
                    "icon": "📊",
                    "params": [{"id": "columns", "label": "Columns (comma-separated)", "type": "text_input", "placeholder": "e.g., Product,Sales"}]
                },
                "sort_values": {
                    "name": "Sort by Column",
                    "icon": "📶",
                    "params": [
                        {"id": "column", "label": "Column to Sort By", "type": "text_input", "placeholder": "e.g., Date"},
                        {"id": "ascending", "label": "Ascending", "type": "checkbox", "default": True}
                    ]
                },
            },
            "Data Manipulation": {
                "add_column": {
                    "name": "Add/Update Column",
                    "icon": "➕",
                    "params": [
                        {"id": "new_column", "label": "New Column Name", "type": "text_input", "placeholder": "e.g., Profit"},
                        {"id": "formula", "label": "Formula (use df)", "type": "text_input", "placeholder": "e.g., df['Sales'] - df['Cost']"}
                    ]
                },
                "rename_column": {
                    "name": "Rename Column",
                    "icon": "✏️",
                    "params": [
                        {"id": "old_name", "label": "Old Column Name", "type": "text_input", "placeholder": "e.g., CustomerID"},
                        {"id": "new_name", "label": "New Column Name", "type": "text_input", "placeholder": "e.g., Customer_ID"}
                    ]
                },
            },
            "Grouping & Aggregation": {
                "group_by_aggregate": {
                    "name": "Group By & Aggregate",
                    "icon": "📈",
                    "params": [
                        {"id": "group_by_cols", "label": "Group By (comma-separated)", "type": "text_input", "placeholder": "e.g., Region,Country"},
                        {"id": "agg_col", "label": "Aggregate Column", "type": "text_input", "placeholder": "e.g., Sales"},
                        {"id": "agg_func", "label": "Function", "type": "selectbox", "options": ['sum', 'mean', 'count', 'min', 'max']}
                    ]
                },
            }
        }
        self.all_actions = {k: v for category in self.action_categories.values() for k, v in category.items()}

    def get_action(self, action_key):
        return self.all_actions.get(action_key)
