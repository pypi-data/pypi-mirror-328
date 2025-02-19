import streamlit as st
from typing import Dict, Any

def render_config_form(schema: Dict[str, Any]) -> Dict[str, Any]:
    """Render a configuration form based on the provided schema"""
    config = {}

    for field_name, field_spec in schema.items():
        field_type = field_spec['type']

        if field_type == 'text':
            config[field_name] = st.text_input(
                field_name,
                value=field_spec.get('default', '')
            )

        elif field_type == 'select':
            config[field_name] = st.selectbox(
                field_name,
                options=field_spec['options'],
                index=field_spec['options'].index(field_spec['default'])
            )

        elif field_type == 'multiselect':
            config[field_name] = st.multiselect(
                field_name,
                options=field_spec['options'],
                default=field_spec['default']
            )

        elif field_type == 'number':
            config[field_name] = st.number_input(
                field_name,
                value=field_spec.get('default', 0),
                min_value=field_spec.get('min', None),
                max_value=field_spec.get('max', None)
            )

        elif field_type == 'boolean':
            config[field_name] = st.checkbox(
                field_name,
                value=field_spec.get('default', False)
            )

    return config
