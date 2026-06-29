import streamlit as st
import pandas as pd
import common

def media_type(df):
    
    # replace media type AM Radio and FM Radio to Radio, Cable TV to TV
    df['Media Type'] = df['Media Type'].replace({
        'AM Radio':'Radio',
        'FM Radio':'Radio',
        'Cable TV':'TV'})
    
    return df
    
def cleaning_formatting(df):
    return media_type(df)


def deduplicate(df, dedup_state):

    data = common.jsonfile_to_dict('json_files/json_columns.json')
    column_list = data['Columns']
    
    if dedup_state=='delete':
        initial_count = df.shape[0]
        df_cleaned = df.drop_duplicates(subset=column_list)
        final_count = df_cleaned.shape[0]
        dedup_note = f'Found {initial_count-final_count} duplicates, removed {initial_count-final_count}'
        st.write(dedup_note)
    
    elif dedup_state=='validate':
        # Flag all rows that belong to a duplicate group (first occurrence included)
        dup_mask = df.duplicated(subset=column_list, keep=False)

        # Collect those rows into a separate dataframe
        df_duplicates = df[dup_mask].copy()

        # Remove duplicates, removing the first occurrence
        df_cleaned = df.drop_duplicates(subset=column_list, keep=False)

        st.dataframe(df_duplicates)
    
    return df_cleaned