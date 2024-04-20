import streamlit as st
from streamlit_file_browser import st_file_browser

st.header('Default Options')
event = st_file_browser("code", key='A')
st.write(event)

# st.header('With Artifacts Server, Allow choose file, disable download')
# event = st_file_browser("code", artifacts_site="http://localhost:1024", show_choose_file=True, show_download_file=False, key='B')
# st.write(event)

# st.header('Show only molecule files')
# event = st_file_browser("code", show_choose_file=True, show_download_file=False, key='C')
# st.write(event)
