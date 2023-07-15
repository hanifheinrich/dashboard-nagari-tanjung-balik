import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

#header website
col1,col2 = st.columns([2,8])
with col1:
  logo=Image.open('logo.png')
  st.image(logo, width=170)
with col2:
  st.title ("Dashboard Nagari Tanjung Balik")
  st.subheader ("Tanjuang Balik, Kecamatan X Koto Diatas, Kabupaten Solok, Sumatera Barat")
st.write("---")

#pilihtahun
st.write("Pilih Tahun")
domain = st.selectbox("Pilih Statistik Tahun",['2022','2023','2024'])
st.write("---")

#demografiwilayah
st.header ("Data Demografi Wilayah")
st.text ("Lorem ipsum dolor sit amet")
datadw = pd.read_csv('data/wilayah_demografi.csv')
col1, col2 = st.columns([1,1])
with col1:
  st.dataframe(datadw)
with col2:
  st.line_chart(datadw)
st.write("---")

#datapendidikan
st.header ("Data Pendidikan dalam KK")
st.text ("Lorem ipsum dolor sit amet")
datapk = pd.read_csv('data/pendidikan_kk.csv')
col1, col2 = st.columns([1,1])
with col1:
  st.dataframe(datapk)
with col2:
  st.bar_chart(datapk)
st.write("---")

#datapendidikan2
st.subheader ("Data Pendidikan ditempuh")
st.text ("Lorem ipsum dolor sit amet")
datapk = pd.read_csv('data/pendidikan_kk.csv')
col1, col2 = st.columns([1,1])
with col1:
  st.dataframe(datapk)
with col2:
  st.bar_chart(datapk)
st.write("---")

#datapekerjaan
st.header ("Data Pekerjaan")
st.text ("Lorem ipsum dolor sit amet")
datapn = pd.read_csv('data/pekerjaan.csv')
col1, col2 = st.columns([1,1])
with col1:
  st.dataframe(datapn)
with col2:
  st.bar_chart(datapn)
st.write("---")

#datajeniskelamin
st.subheader ("Data Jenis Kelamin")
st.text ("Lorem ipsum dolor sit amet")
datajk = pd.read_csv('data/jeniskelamin.csv')
col1, col2 = st.columns([1,1])
with col1:
  st.dataframe(datajk)
with col2:
  labels = 'Laki-laki', 'Perempuan'
  sizes = [1179, 1134]
  explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

  fig1, ax1 = plt.subplots()
  ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
  ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
  st.pyplot(fig1)
st.write("---")

st.subheader ("Data Usia Penduduk")
st.text ("Lorem ipsum dolor sit amet")
datau = pd.read_csv('data/usia.csv')
col1, col2 = st.columns([1,1])
with col1:
  st.dataframe(datau)
with col2:
  st.bar_chart(datau)
st.write("---")