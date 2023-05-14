import streamlit as st
from PIL import Image

image_ichimura = Image.open('businessCard_ichimura.png')

st.image(image_ichimura, use_column_width=False)

image_katsuki = Image.open('businessCard_katsuki.png')

st.image(image_katsuki, use_column_width=False)
