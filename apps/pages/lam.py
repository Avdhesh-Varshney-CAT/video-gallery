# Live Action Movies
import streamlit as st
from apps.pages.videos import showVideos
import random

def animated_text(text):
    colors = ["#ff4500", "#ff8c00", "#ffd700", "#adff2f", "#00fa9a", "#00bfff", "#da70d6"]
    animated_text = "".join([f'<span style="color:{random.choice(colors)};">{char}</span>' for char in text])
    return animated_text

st.set_page_config(page_title="Live Action Movies", page_icon="🎬", layout='wide')
st.markdown(f"<h1 style='text-align: center;'>{animated_text('Welcome to Live Action Movies 🎥')}</h1>", unsafe_allow_html=True)
st.markdown(f"<h2 style='text-align: center;'>Discover and watch amazing live action movies 🎬✨</h2>", unsafe_allow_html=True)
st.write(f"<h6 style='text-align: center;'>From the latest blockbusters to timeless classics, choose your favorite category and start watching! 🍿</h6>", unsafe_allow_html=True)

CATEGORY = st.selectbox("Choose a Category 📂", [None, "Brutal", "Cheat", "Family", "Maid", "School", "Secretary", "Sister", "StepBrother", "StepMom", "StepSister", "Stranger", "Stuck"])

if CATEGORY:
    st.markdown(f"<div style='text-align: center; font-size: 24px;'>You selected: <b>{CATEGORY} 🎬</b></div>", unsafe_allow_html=True)
    showVideos(CATEGORY, './data/lam.json')
else:
    st.info("Please select a category to view the videos.", icon="ℹ️")

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(f"<div style='text-align: center; font-size: 18px;'>Enjoy the show! 🎉</div>", unsafe_allow_html=True)
