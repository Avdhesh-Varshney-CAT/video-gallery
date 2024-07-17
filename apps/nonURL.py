import streamlit as st

DATA = st.session_state.videos_data

st.title("Some Non-Working Videos")

st.write("#### 🚀These videos does not have iframe URL.")
for i in range(len(DATA)):
    if DATA[str(i)]['iFrameURL'] == "":
        st.write(f"Video {DATA[str(i)]['ID']}")
        st.write(f"Name: {DATA[str(i)]['name']}")

st.markdown("---")
st.write("#### 🚀These videos does not have image URL.")
for i in range(len(DATA)):
    if DATA[str(i)]['imageURL'] == "":
        st.write(f"Video {DATA[str(i)]['ID']}")
        st.write(f"Name: {DATA[str(i)]['name']}")

st.markdown("---")
st.write("#### 🚀These videos does not have video URL.")
for i in range(len(DATA)):
    if DATA[str(i)]['videoURL'] == "":
        st.write(f"Video {DATA[str(i)]['ID']}")
        st.write(f"Name: {DATA[str(i)]['name']}")

st.markdown("---")
st.write("#### 🚀These videos does not have website name.")
for i in range(len(DATA)):
    if DATA[str(i)]['websiteName'] == "":
        st.write(f"Video {DATA[str(i)]['ID']}")
        st.write(f"Name: {DATA[str(i)]['name']}")

st.markdown("---")
st.write("#### 🚀These videos does not have download URL.")
for i in range(len(DATA)):
    if DATA[str(i)]['downloadURL'] == "":
        st.write(f"Video {DATA[str(i)]['ID']}")
        st.write(f"Name: {DATA[str(i)]['name']}")
