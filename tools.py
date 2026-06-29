import streamlit as st
import common
import pandas as pd
import tool_apps
import settings

def import_data():

    # common.label_name("File Upload")
    uploaded_file = st.file_uploader(
        label='File Upload',
        label_visibility='collapsed',
        key='file_uploader',
        type=['xlsx', "xls"])

    # st.markdown("""<div class="supported-files">Supported: XLSX • XLS</div>""", unsafe_allow_html=True)

    return uploaded_file

    

def main_window():

    if 'dedup_status' not in st.session_state:
        st.session_state.dedup_status=''

    # for st.file_uploader
    st.markdown("""
    <style>
    
    /* entire file uploader */
    [data-testid="stFileUploader"] {
    background-color: #2f1472;
    border: 5px solid #F90909;
    border-radius: 15px;
    padding: 0px;
    margin-top: 0px;
    }

    /* upload button */               
    [data-testid="stFileUploader"] button {
    background-color: #FFFFFF !important;
    color: #000000 !important;
    border: 5px solid #000000 !important;
    border-radius: 20px;
    font-weight: bold;    
    }
    
    /* upload button hover sta                      te */
    [data-testid="stFileUploader"] button:hover {
    border-color: #F90909 !important;
    background-color: #000000 !important;
    color: #ffffff !important;
    }

    /* drop zone */
    [data-testid="stFileUploaderDropzone"] {
    display: flex;
    flex-direction: column;
    justify-content: center;   /* vertical centering */
    align-items: center;       /* horizontal centering */
    min-height: 0px;
    }
    
    /* drop zone hover */
    [data-testid="stFileUploaderDropzone"]:hover {
    background-color: #000000;
    border-color: #FFFFFF;
    }
    
    /* drop zone instruction text */
    [data-testid="stFileUploaderDropzoneInstructions"] * {
    color: #FFFFFF !important;
    font-weight: bold !important;
    }
    
    </style>
    """, unsafe_allow_html=True)


    # add a page title
    common.page_title('REPORT TOOLS')

    uploaded_file = import_data()
    
    if uploaded_file:

        # convert uploaded file to pandas dataframe
        df = pd.read_excel(uploaded_file)

        cols = st.columns(3, gap='small')
        
        with cols[0]:
            with st.container(border=True):
                cb_deduplication = st.checkbox(
                    label='Deduplication',
                    key='cb_deduplication',
                    help=f'{st.session_state.dedup_status}')
                if st.button(label='Settings', key='btn_settings_deduplicate', width='stretch'):
                    settings.dialog_settings_deduplicate(df)
                
        with cols[1]:
            with st.container(border=True):
                cb_cleaning = st.checkbox(
                    label='Cleaning/Formatting',
                    key='cb_cleaning',
                    help='info')
                if st.button(label='Settings', key='btn_settings_clean', width='stretch'):
                    settings.dialog_settings_clean(df)
                    
        if st.button(label='Process',key='btn_process',width='stretch'):
            if cb_deduplication==True:
                data_dict = common.jsonfile_to_dict('json_files/json_dedup.json')
                dedup_state = data_dict['dedup_state']
                df_no_duplicates = tool_apps.deduplicate(df, dedup_state)

            if cb_cleaning==True:
                df_cleaned = tool_apps.cleaning_formatting(df_no_duplicates)
            
            st.download_button(
                label="Download Excel",
                data=common.to_excel(df_cleaned),
                file_name="cleaned_data.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheetml.sheet",)
