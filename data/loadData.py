import streamlit as st
import json

@st.cache_data
def loadData(websiteName):
    try:
        with open('./data/data.json') as f:
            data = json.load(f)
            FILTERED_DATA = []
            for item in data:
                if item['websiteName'] == websiteName:
                    FILTERED_DATA.append(item)
    except FileNotFoundError:
        st.error("JSON file not found.")
        st.stop()
    except json.JSONDecodeError:
        st.error("Error decoding JSON.")
        st.stop()
    return FILTERED_DATA
