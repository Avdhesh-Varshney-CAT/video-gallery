import streamlit as st
import json

def loadData():
    try:
        with open('./data/data.json') as f:
            data = json.load(f)
    except FileNotFoundError:
        st.error("JSON file not found.")
        st.stop()
    except json.JSONDecodeError:
        st.error("Error decoding JSON.")
        st.stop()
    return data
