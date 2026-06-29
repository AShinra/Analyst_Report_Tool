import streamlit as st
from streamlit_option_menu import option_menu

def main_sidebar():
    selected = option_menu(
        menu_title="Menu",
        options=[
            "Tools",
            "Report",
            "Settings"
        ],
        icons=[
            "speedometer2",
            "file-earmark-text",
            "gear"
        ],
        menu_icon="cast",
        default_index=0,
        
        styles={
            "container": {
                "padding": "0!important",
                "border": "5px solid #f90909",
                "border-radius": "25px",
            },
            "nav-link": {
                "font-size": "15px",
                "padding": "6px 10px",      # Reduce vertical padding
                "line-height": "0",       # Reduce line spacing
                "margin": "0px 0",          # Reduce space between items
                "text-align": "left",
            },
            "nav-link-selected": {
                "background-color": "#000000",
            },
            "icon": {
                "font-size": "16px",
            },
            
        },
    )

    return selected