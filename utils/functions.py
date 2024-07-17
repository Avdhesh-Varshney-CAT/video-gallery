import streamlit as st
from auth.profile import profile
from data.loadData import loadData

DATA = loadData()
LIMIT = 1
WEBSITE_COUNTS = {}
for i in range(len(DATA)):
    website_name = DATA[str(i)]['websiteName']
    if website_name:
        if website_name in WEBSITE_COUNTS:
            WEBSITE_COUNTS[website_name] += 1
        else:
            WEBSITE_COUNTS[website_name] = 1

def logout():
  if st.session_state.logged_in:
    profile()
    if st.button("Log out"):
      st.session_state.logged_in = False
      st.rerun()

if 'videos_data' not in st.session_state:
    st.session_state.videos_data = DATA
if 'LIMIT' not in st.session_state:
    st.session_state.LIMIT = LIMIT
if 'WEBSITE_COUNTS' not in st.session_state:
    st.session_state.WEBSITE_COUNTS = WEBSITE_COUNTS

logout_page = st.Page(logout, title="My Profile", icon=":material/account_circle:")
dashboard = st.Page("apps/dashboard.py", title="Dashboard", icon=":material/dashboard:")
NonURL = st.Page("apps/nonURL.py", title="Non-URL", icon=":material/video_library:")

# Pages
brazzers = st.Page("apps/pages/brazzers.py", title="Brazzers", icon=":material/video_library:")
hentai = st.Page("apps/pages/hentai.py", title="Hentai", icon=":material/video_library:")
spankbang = st.Page("apps/pages/spankbang.py", title="SpankBang", icon=":material/video_library:")
xozilla = st.Page("apps/pages/xozilla.py", title="Xozilla", icon=":material/video_library:")

def load_functions():
  pages = {
    "": [dashboard],
    "Account": [logout_page],
    "Videos": [brazzers, hentai, spankbang, xozilla],
    "Under Working Data": [NonURL],
  }

  return pages
