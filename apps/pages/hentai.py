import streamlit as st
import webbrowser

# Importing the helper functions
from utils.calculateTime import calculateTime
from utils.randomColor import randomColor
from utils.downloadVideo import downloadVideo

WEBSITE_NAME = 'Hentai'
LIMIT = 1

# Global variables
DATA = st.session_state.videos_data
WEBSITE_COUNTS = st.session_state.WEBSITE_COUNTS
startIndex = 0
lastIndex = min(LIMIT, len(DATA))

st.title(f"Watch Awesome Videos from {WEBSITE_NAME}")
for i in range(startIndex, lastIndex):
    item = DATA[str(i)]

    if item['websiteName'] == WEBSITE_NAME and item['iFrameURL'] != "":
        st.write(f"#### Featured Video {item['ID']}")

        if item['imageURL'] != "":
            st.image(item['imageURL'], caption=item['name'], use_column_width=True)
        else:
            st.markdown(f'<iframe src="{item["iFrameURL"]}" width="100%" height="500" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
            st.write(f"##### <span style='color:{randomColor()};'>{item['name']}</span>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.write(f"Duration: <span style='color:{randomColor()};'>{calculateTime(item['exactTimeLength'])}</span>", unsafe_allow_html=True)
        with col2:
            tags = " ".join([f'<span style="color:{randomColor()};">{tag}</span>' for tag in item['tags']])
            if tags == "":
                st.markdown(f"**Tags:** No tags available", unsafe_allow_html=True)
            else:
                st.markdown(f"**Tags:** {tags}", unsafe_allow_html=True)

        col3, col4, col5, col6 = st.columns(4)
        with col3:
            st.button("Watch Instantly", on_click=lambda url=item['iFrameURL']: webbrowser.open_new_tab(url), key=item['ID'])
        with col4:
            if st.button("Download Video", key=item['imageURL']) and item['downloadURL'] != "":
                file_name = downloadVideo(item['downloadURL'])
                if file_name:
                    with open(file_name, "rb") as file:
                        btn = st.download_button(label="Download", data=file, file_name=file_name, key=item['downloadURL'])
        with col5:
            st.button("Visit Website", on_click=lambda url=item['videoURL']: webbrowser.open_new_tab(url), key=item['name'])
        with col6:
            st.button("More Videos", on_click=lambda url=item['websiteURL']: webbrowser.open_new_tab(url), key=item['iFrameURL'])

if WEBSITE_NAME in WEBSITE_COUNTS and LIMIT < WEBSITE_COUNTS[WEBSITE_NAME]:
    if st.button("Load More"):
        startIndex = lastIndex
        lastIndex = min(startIndex + LIMIT, len(DATA))
        st.session_state.LIMIT = lastIndex
        st.experimental_rerun()
