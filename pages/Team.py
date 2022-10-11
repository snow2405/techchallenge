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



st.subheader("Our Team")

st.markdown("<p style='text-align: left; '>Ava G.</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: left; '>Chrissy H.</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: left; '>Fabian W.</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: left; '>Lilla S.</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: left; '>Lion S.</p>", unsafe_allow_html=True)
   