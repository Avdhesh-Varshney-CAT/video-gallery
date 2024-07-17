import streamlit as st
from auth.profile import profile

def logout():
  if st.session_state.logged_in:
    profile()
    if st.button("Log out"):
      st.session_state.logged_in = False
      st.rerun()

logout_page = st.Page(logout, title="My Profile", icon=":material/account_circle:")

dashboard = st.Page("apps/dashboard.py", title="Dashboard", icon=":material/dashboard:")
videos = st.Page("apps/videos.py", title="Videos", icon=":material/video_library:")

def load_functions():
  pages = {
    "": [dashboard],
    "Account": [logout_page],
    "Videos": [videos],
  }

  return pages
