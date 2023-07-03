
import os
import streamlit.components.v1 as components

# _DEVELOP_MODE = os.getenv('DEVELOP_MODE')
_DEVELOP_MODE = True

if _DEVELOP_MODE:
    _component_func = components.declare_component(
        "streamlit-template",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/dist")
    _component_func = components.declare_component("streamlit-template", path=build_dir) # noqa


def st_template(key = None): # noqa
    return _component_func(key=key) # noqa


if _DEVELOP_MODE:
    import streamlit as st
    event = st_template("test")
    st.write(event)
