import streamlit as st
import json

LIMIT = 5

try:
    with open('./data/data.json') as f:
        data = json.load(f)
except FileNotFoundError:
    st.error("JSON file not found.")
    st.stop()
except json.JSONDecodeError:
    st.error("Error decoding JSON.")
    st.stop()

st.title("Some Awesome Videos")

if 'num_videos' not in st.session_state:
    st.session_state.num_videos = LIMIT

for i in range(min(st.session_state.num_videos, len(data))):
    item = data[i]
    st.subheader(item['textData'])
    st.markdown(f'<iframe src="{item["videoURL"]}" width="600" height="400"></iframe>', unsafe_allow_html=True)

if st.session_state.num_videos < len(data):
    if st.button("Load More"):
        st.session_state.num_videos += LIMIT
        st.experimental_rerun()
