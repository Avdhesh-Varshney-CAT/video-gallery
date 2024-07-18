import streamlit as st
import webbrowser

# Importing the helper functions
from data.loadData import loadData
from utils.calculateTime import calculateTime
from utils.randomColor import randomColor
from utils.downloadVideo import downloadVideo

# Global variables
WEBSITE_NAME = 'Iporntv'
DATA = loadData(WEBSITE_NAME)

st.title(f"Watch Awesome Videos from {WEBSITE_NAME}")

for item in DATA:
    if item['websiteName'] == WEBSITE_NAME:
        st.write(f"#### Featured Video No. {item['ID']}")

        if item['imageURL'] != "":
            st.image(item['imageURL'], caption=item['name'], use_column_width=True)
        else:
            st.markdown(f'<iframe src="{item["iFrameURL"]}" width="100%" height="500" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
            st.write(f"##### <span style='color:{randomColor()};'>{item['name']}</span>", unsafe_allow_html=True)

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.write(f"Duration: <span style='color:{randomColor()};'>{calculateTime(item['timeStamp'])}</span>", unsafe_allow_html=True)
        with col2:
            tags = " ".join([f'<span style="color:{randomColor()};">{tag}</span>' for tag in item['tags']])
            if tags == "":
                st.markdown(f"**Tags:** No tags available", unsafe_allow_html=True)
            else:
                st.markdown(f"**Tags:** {tags}", unsafe_allow_html=True)
        with col3:
            boys = " ".join([f'<span style="color:{randomColor()};">{name}</span>' for name in item['boyName']])
            if boys == "":
                st.markdown(f"**Heros:** No names available", unsafe_allow_html=True)
            else:
                st.markdown(f"**Heros:** {boys}", unsafe_allow_html=True)
        with col4:
            girls = " ".join([f'<span style="color:{randomColor()};">{name}</span>' for name in item['girlName']])
            if girls == "":
                st.markdown(f"**Stars:** No names available", unsafe_allow_html=True)
            else:
                st.markdown(f"**Stars:** {girls}", unsafe_allow_html=True)

        col5, col6, col7, col8 = st.columns(4)
        with col5:
            st.button("Watch Instantly", on_click=lambda url=item['iFrameURL']: webbrowser.open_new_tab(url), key=item['ID'])
        with col6:
            if st.button("Download Video", key=item['imageURL']) and item['downloadURL'] != "":
                file_name = downloadVideo(item['downloadURL'])
                if file_name:
                    with open(file_name, "rb") as file:
                        btn = st.download_button(label="Download", data=file, file_name=file_name, key=item['downloadURL'])
        with col7:
            st.button("Full Video", on_click=lambda url=item['videoURL']: webbrowser.open_new_tab(url), key=item['name'])
        with col8:
            st.button("More Videos", on_click=lambda url=item['websiteURL']: webbrowser.open_new_tab(url), key=item['iFrameURL'])

        st.markdown(f"---")
