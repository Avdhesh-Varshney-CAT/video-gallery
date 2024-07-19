import streamlit as st
import webbrowser

# Importing the helper functions
from data.loadData import loadData
from utils.calculateTime import calculateTime
from utils.randomColor import randomColor
from utils.downloadVideo import downloadVideo

def showVideos(CATEGORY, FILE_PATH):
    DATA = loadData(CATEGORY, FILE_PATH)

    st.markdown(f"<h1 style='text-align: center;'>{CATEGORY} Videos 🎬</h1>", unsafe_allow_html=True)

    INDEX = 1
    for item in DATA:
        st.markdown(f"---")
        
        st.write(f"### 🌟 Featured Video {INDEX}")
        st.write(f'**Video ID:** {FILE_PATH}/{item["ID"]}')

        if item['imageURL'] != "":
            st.image(item['imageURL'], caption=item['name'], use_column_width=True)
        else:
            st.markdown(f'<iframe src="{item["iFrameURL"]}" width="100%" height="500" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
            st.write(f"#### <span style='color:{randomColor()};'>{item['name']}</span>", unsafe_allow_html=True)

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.write(f"⏳ **Duration:** <span style='color:{randomColor()};'>{calculateTime(item['timeStamp'])}</span>", unsafe_allow_html=True)
        with col2:
            tags = " / ".join([f'<span style="color:{randomColor()};">{tag}</span>' for tag in item['tags']])
            st.markdown(f"🏷️ **Tags:** {tags or 'No tags available'}", unsafe_allow_html=True)
        with col3:
            boys = " / ".join([f'<span style="color:{randomColor()};">{name}</span>' for name in item['boyName']])
            st.markdown(f"🎭 **Heros:** {boys or 'No names available'}", unsafe_allow_html=True)
        with col4:
            girls = " / ".join([f'<span style="color:{randomColor()};">{name}</span>' for name in item['girlName']])
            st.markdown(f"🌟 **Stars:** {girls or 'No names available'}", unsafe_allow_html=True)

        col5, col6, col7, col8 = st.columns(4)
        with col5:
            st.button("▶️ Watch Instantly", on_click=lambda url=item['iFrameURL']: webbrowser.open_new_tab(url), key=f"watch_{item['ID']}")
        with col6:
            if st.button("⬇️ Download Video", key=f"download_{item['ID']}_{item['name']}") and item['downloadURL'] != "":
                file_name = downloadVideo(item['downloadURL'])
                if file_name:
                    with open(file_name, "rb") as file:
                        st.download_button(label="Download", data=file, file_name=file_name, key=f"download_btn_{item['ID']}_{item['timeStamp']}")
        with col7:
            st.button("📺 Full Video", on_click=lambda url=item['videoURL']: webbrowser.open_new_tab(url), key=f"full_{item['ID']}_{item['imageURL']}")
        with col8:
            st.button("🔍 More Videos", on_click=lambda url=item['websiteURL']: webbrowser.open_new_tab(url), key=f'more_{item["ID"]}_{INDEX}')

        INDEX += 1
