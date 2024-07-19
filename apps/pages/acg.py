# Animations, Cartoons & Graphics
import streamlit as st
from apps.pages.videos import showVideos
import random

def animated_text(text):
    colors = ["#ff6347", "#ffa500", "#ffff00", "#32cd32", "#00ced1", "#1e90ff", "#9370db"]
    animated_text = "".join([f'<span style="color:{random.choice(colors)};">{char}</span>' for char in text])
    return animated_text

st.set_page_config(page_title="Animated Worlds", page_icon="🌟", layout="wide")
st.markdown(f"<h1 style='text-align: center;'>{animated_text('Welcome to Animated Worlds 🌟')}</h1>", unsafe_allow_html=True)
st.markdown(f"<h2 style='text-align: center;'>Explore your favorite animated videos 🎥✨</h2>", unsafe_allow_html=True)
st.markdown(f"<h6 style='text-align: center;'>Dive into a world of animation, where imagination meets reality. Choose your favorite category and start watching! 🎬</h6>", unsafe_allow_html=True)

CATEGORY = st.selectbox("Choose a Category 🗂️", [None, "Hentai"])

if CATEGORY:
    st.markdown(f"<div style='text-align: center; font-size: 24px;'>You selected: <b>{CATEGORY} 🍿</b></div>", unsafe_allow_html=True)
    showVideos(CATEGORY, './data/acg.json')
else:
    st.info("Please select a category to view the videos.", icon="ℹ️")

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(f"<div style='text-align: center; font-size: 18px;'>Enjoy watching! 🎉</div>", unsafe_allow_html=True)
