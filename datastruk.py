import streamlit as st
from datetime import datetime, time


date = datetime.now()
date_slice = date.date()
Hour = (int(date.strftime("%H"))+7)%24
Minutes = int(date.strftime("%M"))
Seconds = int(date.strftime("%S"))
time_fix = time(Hour,Minutes, Seconds)


st.title('Data Struk Crisbar')

Pemesanan = st.selectbox('Jenis Pemesanan', ['Makan di Tempat', 'Take Away'])
if Pemesanan == 'Makan di Tempat' :
    JenisKelamin = st.selectbox('Jenis Kelamin Pelanggan', ['Laki-Laki', 'Perempuan'])
if Pemesanan == 'Take Away' :
    Metode = st.selectbox('Metode Pemesanan', ['Datang Langsung', 'On Demand Services'])
    if Metode == 'On Demand Services' :
        st.selectbox('Jenis On Demand Services', ['Go Food', 'Grab Food', 'Shopee Food'])
    else :
        st.selectbox('Jenis Kelamin Pelanggan', ['Laki-Laki', 'Perempuan'])
Pembayaran = st.selectbox('Metode Pembayaran', ['Tunai', 'Cashless'])
if Pembayaran == 'Cashless' :
    st.selectbox('Jenis Pembayaran Cashless', ['Debit', 'Ovo', 'Dana', 'Gopay', 'Shopeepay'])
st.date_input('Tanggal Pembuatan Struk', value= date_slice)
st.time_input('Waktu Pembuatan Struk', value= time_fix)

