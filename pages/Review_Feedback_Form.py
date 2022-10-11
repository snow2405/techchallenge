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

st.title("Create and Review your Feedback Form")
st.image(
    "https://i.ibb.co/QMCXXXk/Screenshot-2022-10-11-115236.png",
    width=700,
)



st.text("")