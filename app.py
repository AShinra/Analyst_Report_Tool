import streamlit as st
from sidebar import main_sidebar
import tools
import settings
import report


if __name__ == "__main__":

    st.set_page_config(
        page_title="Analyst Tools",
        page_icon="⚙️",
        layout="centered",      # or "wide"
        initial_sidebar_state="expanded")

    with st.sidebar:
        selected = main_sidebar()

    if selected=='Tools':
        tools.main_window()
    
    if selected=='Report':
        report.main_window()
    
    if selected=='Settings':
        settings.main_window()





