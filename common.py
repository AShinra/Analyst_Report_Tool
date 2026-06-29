import streamlit as st
import json
import pandas as pd
from io import BytesIO

def page_title(title):

    st.markdown("""
    <style>
    /* Reduce bottom margin of st.title */
    h1 {
        margin-bottom: 0.0rem !important;
    }

    /* Reduce top/bottom margin of divider */
    hr {
        margin-top: 0rem !important;
        margin-bottom: 0.0rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title(title, text_alignment='center')
    st.divider()

def label_name(label: str, font_color: str='black'):
    return st.markdown(f'<label style="color:{font_color};font-weight:bold;">{label}</label>', unsafe_allow_html=True)

def jsonfile_to_dict(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def dict_to_jsonfile(data_dict, filepath):
    
    json_string = json.dumps(data_dict, indent=4)
    
    with open(filepath, "w") as f:
        f.write(json_string)

def to_excel(df):
    buffer = BytesIO()
    with pd.ExcelWriter(buffer, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Sheet1")
    return buffer.getvalue()

