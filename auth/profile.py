import streamlit as st
from PIL import Image

def profile():
  st.title("👤 Profile Page")

  st.write(f"**Name:** {st.session_state.name}")
  st.write(f"**Username:** @{st.session_state.username}")
  
  st.markdown("---")
  
  # User details section
  st.write("### User Details")
  
  col3, col4 = st.columns(2)
  with col3:
    st.write(f"**🛠 Role:** {st.session_state.role}")
    st.write(f"**🎂 Age:** {st.session_state.age}")
  with col4:
    st.write(f"**⚥ Gender:** {st.session_state.gender}")
    st.write(f"**📧 Email:** {st.session_state.email}")
  
  st.markdown("---")
  
  # Adding some fun elements
  st.write("### About Me")
  st.write(st.session_state.about)
