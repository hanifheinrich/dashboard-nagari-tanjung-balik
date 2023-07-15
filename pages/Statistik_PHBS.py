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

st.write("Pilih Periode")
domain = st.selectbox("Pilih Periode Semester PHBS",['Semester 1 (Juni 2021)','Semester 2 (Desember 2021)','Semester 3 (Juni 2022)','Semester 4 (Desember 2022)','Semester 5 (Juni 2023)','Semester 6 (Desember 2023)','Semester 7 (Juni 2024)','Semester 8 (Desember 2024)','Lihat Semua'])
st.write("---")
st.subheader ("Data PHBS Pilot Project Nagari Tanjung Balik")
st.text ("Lorem ipsum dolor sit amet")
dataphbs = pd.read_csv('data/phbs.csv')
semester1=dataphbs.groupby('Indikator')['Juni 2021'].sum().reset_index()
semester2=dataphbs.groupby('Indikator')['Desember 2021'].sum().reset_index()
semester3=dataphbs.groupby('Indikator')['Juni 2022'].sum().reset_index()
semester4=dataphbs.groupby('Indikator')['Desember 2022'].sum().reset_index()
semester5=dataphbs.groupby('Indikator')['Juni 2023'].sum().reset_index()
semester6=dataphbs.groupby('Indikator')['Desember 2023'].sum().reset_index()
semester7=dataphbs.groupby('Indikator')['Juni 2024'].sum().reset_index()
semester8=dataphbs.groupby('Indikator')['Desember 2024'].sum().reset_index()

if domain=='Semester 1 (Juni 2021)':
  st.dataframe(semester1)
elif domain =='Semester 2 (Desember 2021)':
  st.dataframe(semester2)
elif domain =='Semester 3 (Juni 2022)':
  st.dataframe(semester3)
elif domain =='Semester 4 (Desember 2022)':
  st.dataframe(semester4)
elif domain =='Semester 5 (Juni 2023)':
  st.dataframe(semester5)
elif domain =='Semester 6 (Desember 2023)':
  st.dataframe(semester6)
elif domain =='Semester 7 (Juni 2024)':
  st.dataframe(semester7)
elif domain =='Semester 8 (Desember 2024)':
  st.dataframe(semester8)
else:
  st.dataframe(dataphbs)

st.write("---")

st.subheader ("Visualisasi Progress PHBS Pilot Project Nagari Tanjung Balik")
st.text ("Lorem ipsum dolor sit amet")

#progress1
tahun=['a','b','c','d','e','f','g','h']
value=dataphbs.iloc[:1,[1,2,3,4,5,6,7,8]].values
pg1=pd.DataFrame(
  [],
)

st.write(pg1)