import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

#header website
col1,col2 = st.columns([2,8])
with col1:
  logo=Image.open('logo.png')
  st.image(logo, width=170)
with col2:
  st.title ("Dashboard Nagari Tanjung Balik")
  st.subheader ("Tanjuang Balik, Kecamatan X Koto Diatas, Kabupaten Solok, Sumatera Barat")
st.write("---")

st.write("Pilih Tahun")
domain = st.selectbox("Pilih Statistik Tahun",['2022','2023','2024'])

st.subheader ("Data Program Bantuan")
st.text ("Lorem ipsum dolor sit amet")
datapb = pd.read_csv('data/program_bantuan.csv')
st.dataframe(datapb)
st.line_chart(datapb)