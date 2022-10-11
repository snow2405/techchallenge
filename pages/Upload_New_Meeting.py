from http import server
import streamlit as st
import pandas as pd

###################################
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import JsCode

###################################

from functionforDownloadButtons import download_button

###################################



def _max_width_():
    max_width_str = f"max-width: 1800px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )

st.set_page_config(page_icon="🤝", page_title="Uploader")

st.image(
    "https://i.ibb.co/kHH7yvK/logo-include.png",
    width=200,
)

st.title("include.us")



uploaded_file = st.file_uploader(
    "",
    key="1",
    help="To activate 'wide mode', go to the hamburger menu > Settings > turn on 'wide mode'",
)

if uploaded_file is not None:
    st.success(
        f"""
            Upload successful!
            """
    )

    

else:
    st.info(
        f"""
            👆 Upload a .mp3 or .mp4 file for the data evaluation. What is a [.mp4?](https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley)
            """
    )

    st.stop()





st.text("")


st.text("")