import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca data
day_data = pd.read_csv(r'C:\Users\Citra\Documents\.bootcamp\Dicoding\Proyek Analisis Data\submission\dashboard\day.csv')
hour_data = pd.read_csv(r'C:\Users\Citra\Documents\.bootcamp\Dicoding\Proyek Analisis Data\submission\dashboard\hour.csv')

# Judul dashboard
st.title('Dashboard Bike Sharing')

# Sidebar untuk memilih dataset
st.sidebar.title('Pilih Dataset')
dataset_choice = st.sidebar.selectbox('Pilih dataset yang ingin dianalisis:', 
                                      ['day.csv (Agregat Harian)', 'hour.csv (Detail Per Jam)'])

# Memilih dataset berdasarkan pilihan
if dataset_choice == 'day.csv (Agregat Harian)':
    data = day_data
    st.subheader('Analisis Dataset Agregat Harian')
    st.write("Dataset ini mencakup jumlah penyewaan sepeda yang telah diagregasi berdasarkan hari.")
else:
    data = hour_data
    st.subheader('Analisis Dataset Detail Per Jam')
    st.write("Dataset ini mencakup jumlah penyewaan sepeda dengan detail per jam.")

# Menampilkan beberapa informasi dasar
st.write("Jumlah Data:", len(data))
st.write("Kolom Data:", data.columns.tolist())

# Visualisasi distribusi penyewaan sepeda berdasarkan musim
if 'season' in data.columns:
    st.subheader('Distribusi Penyewaan Sepeda Berdasarkan Musim')
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.countplot(x='season', data=data, ax=ax1)
    ax1.set_title('Distribusi Penyewaan Sepeda Berdasarkan Musim')
    ax1.set_xlabel('Musim')
    ax1.set_ylabel('Jumlah Penyewaan')
    st.pyplot(fig1)
else:
    st.write("Kolom 'season' tidak tersedia pada dataset ini.")

# Visualisasi suhu vs jumlah penyewaan sepeda
if 'temp' in data.columns and 'cnt' in data.columns:
    st.subheader('Hubungan Suhu dan Jumlah Penyewaan Sepeda')
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x='temp', y='cnt', data=data, ax=ax2)
    ax2.set_title('Hubungan Suhu dan Jumlah Penyewaan Sepeda')
    ax2.set_xlabel('Suhu')
    ax2.set_ylabel('Jumlah Penyewaan')
    st.pyplot(fig2)
else:
    st.write("Kolom 'temp' atau 'cnt' tidak tersedia pada dataset ini.")

# Visualisasi tambahan untuk hour.csv
if dataset_choice == 'hour.csv (Detail Per Jam)':
    if 'hr' in data.columns and 'cnt' in data.columns:
        st.subheader('Jumlah Penyewaan Berdasarkan Jam')
        fig3, ax3 = plt.subplots(figsize=(10, 6))
        sns.lineplot(x='hr', y='cnt', data=data, ax=ax3)
        ax3.set_title('Jumlah Penyewaan Berdasarkan Jam')
        ax3.set_xlabel('Jam')
        ax3.set_ylabel('Jumlah Penyewaan')
        st.pyplot(fig3)
    else:
        st.write("Kolom 'hr' atau 'cnt' tidak tersedia pada dataset ini.")