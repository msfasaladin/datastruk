import streamlit as st
import datetime as datetime


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
st.date_input('Tanggal Pembuatan Struk', value= "today")
st.time_input('Waktu Pembuatan Struk', value= datetime)
print(datetime.date)