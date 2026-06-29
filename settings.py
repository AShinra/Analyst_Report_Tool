import streamlit as st
import common
import pandas as pd

def dialog_box_customization():

    return st.markdown("""
    <style>
    
    /* set dialog width and height */
    div[role="dialog"] {
        width: 500px !important;
        max-width: 90vw !important;     /* don't overflow on small screens */
        height: 600px !important;
        max-height: 90vh !important;
    }
    
    /* tighten space between dialog title and content */
    div[role="dialog"] h1,
    div[role="dialog"] h2 {
        margin-bottom: 0 !important;
        padding-bottom: 0 !important;
    }

    /* the vertical block that holds your content */
    div[role="dialog"] [data-testid="stVerticalBlock"] {
        gap: 0.25rem !important;   /* lower or set to 0 */
    }
    </style>
    """, unsafe_allow_html=True)


@st.dialog('Settings')
def dialog_settings_deduplicate(df):

    customized = dialog_box_customization()

    tabs = st.tabs(['Columns', 'Result'])

    with tabs[0]:
        setting_columns(df)
    with tabs[1]:
        setting_result()

    
        

def setting_columns(df):

    with st.container(border=True, height=250):
        data_dict = common.jsonfile_to_dict(file_path='json_files/json_columns.json')
        stored_columns = data_dict['Columns']

        df_columns = pd.DataFrame(stored_columns, columns=['Column Name'])
        df_columns.style.hide(axis="columns")
        st.markdown('Columns used in duplicate detection.', help=':red[⚠️Warning!] Stored column names may differ from the uploaded file.')
        st.table(df_columns.style.hide(axis="index"))

    
    choice = st.radio(
        label='',
        label_visibility='collapsed',
        options=['**:green[Use Default]**', '**:red[Re-Select]**'],
        horizontal=True)
    
    if choice=='**:red[Re-Select]**':
        column_list = df.columns.to_list()
        with st.container(border=True):
            selected_columns = st.multiselect(
                label='',
                label_visibility='collapsed',
                options=column_list)
            
            dict_columns = {}
            if st.button(label='Use Selection', width='stretch'):
                dict_columns['Columns'] = selected_columns
                common.dict_to_jsonfile(
                    data_dict=dict_columns,
                    filepath='json_files/json_columns.json')
                st.rerun()
            
def setting_result():

    data_dict = common.jsonfile_to_dict(file_path='json_files/json_dedup.json')
    if data_dict["dedup_state"]=='validate':
        st.markdown(f'**:blue[Current Status]**: Duplicates will not be deleted automatically, user will be asked to validate the results if they need to retain the records or delete them')
    elif data_dict["dedup_state"]=='delete':
        st.write(f'**:blue[Current Status]**: Duplicates will be deleted automatically.')
    
    if st.checkbox(label='Change State'):
        selected_state = st.selectbox(
            label='Chose State',
            options=['validate', 'delete'])
        
        dict_dedup = {}
        if st.button(label='Select', width='stretch'):
            dict_dedup['dedup_state'] = selected_state
            common.dict_to_jsonfile(
                data_dict=dict_dedup,
                filepath='json_files/json_dedup.json')
            st.rerun()



    
    

    
    
    
    
    
    
    
                
                

    

            






    # column_list = df.columns.to_list()

    # st.multiselect(
    #     label='Select Columns',
    #     options=column_list
    #     )








@st.dialog('Settings')
def dialog_settings_clean(df):

    customized = dialog_box_customization()
    
    tabs = st.tabs(['Media Types', 'Publication'])

    with tabs[0]:
        settings_media_type()


def settings_media_type():
    data_dict = common.jsonfile_to_dict(file_path='json_files/json_media_type.json')

    df = pd.DataFrame(
        data=data_dict.items(),
        columns=['Media Type', 'Replacement'])
    
    with st.container(border=True, height=250):
        st.dataframe(df, hide_index=True)
    
    choice = st.radio(
        label='',
        label_visibility='collapsed',
        options=['**:green[New Entry]**', '**:red[Delete Entry]**'],
        horizontal=True)

    if choice=='**:green[New Entry]**':
        # common.label_name("New Entry")
        with st.container(border=True):
            cols = st.columns(2, gap='xxsmall')
            with cols[0]:
                new_mediatype = st.text_input(label='📂 Media Type')
            with cols[1]:
                new_replacement = st.text_input(label='🔄 Replacement')
            if st.button(label='Add Media Type', key='btn_add_mediatype', width='stretch'):
                data_dict[new_mediatype] = new_replacement
                common.dict_to_jsonfile(
                    data_dict=data_dict,
                    filepath='json_files/json_media_type.json')
                st.rerun()
    
    if choice=='**:red[Delete Entry]**':
        # common.label_name("Delete Entry")

        media_types = []
        for k, v in data_dict.items():
            media_types.append(k)
        
        cols = st.columns(2, gap='xxsmall')

        with cols[0]:
            for_delete = st.selectbox(
                label='Media Types',
                options=media_types,
                label_visibility='collapsed')
        
        with cols[1]:
            if st.button(label='Delete', width='stretch'):
                del data_dict[for_delete]
                common.dict_to_jsonfile(
                    data_dict=data_dict,
                    filepath='json_files/json_media_type.json')
                st.rerun()


    





def main_window():
    common.page_title('SETTINGS')