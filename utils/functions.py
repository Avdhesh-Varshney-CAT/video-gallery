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

# Pages
brazzers = st.Page("apps/pages/brazzers.py", title="Brazzers", icon=":material/video_library:")
eporner = st.Page("apps/pages/eporner.py", title="Eporner", icon=":material/video_library:")
hentai = st.Page("apps/pages/hentai.py", title="Hentai", icon=":material/video_library:")
iporntv = st.Page("apps/pages/iporntv.py", title="Iporntv", icon=":material/video_library:")
okxxx = st.Page("apps/pages/okxxx.py", title="OkXXX", icon=":material/video_library:")
spankbang = st.Page("apps/pages/spankbang.py", title="SpankBang", icon=":material/video_library:")
xozilla = st.Page("apps/pages/xozilla.py", title="Xozilla", icon=":material/video_library:")
youjizz = st.Page("apps/pages/youjizz.py", title="YouJizz", icon=":material/video_library:")

def load_functions():
  pages = {
    "": [dashboard],
    "Account": [logout_page],
    "Videos": [brazzers, eporner, hentai, iporntv, okxxx, spankbang, xozilla, youjizz],
  }

  return pages
