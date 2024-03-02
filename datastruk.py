import streamlit as st
from datetime import datetime, time
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    port = 3306,
    user="root",
    password="kjkszpj",
    database="data_struk_crisbar"
)

cursor = conn.cursor()

date = datetime.now()
date_slice = date.date()
hour = (int(date.strftime("%H"))+7)%24
minutes = int(date.strftime("%M"))
seconds = int(date.strftime("%S"))
time_fix = time(hour,minutes, seconds)


st.title('Data Struk Crisbar')

with st.form("first_form2"):
      metode = st.selectbox('Metode Pemesanan', ['Datang Langsung', 'On Demand Services'])
      change = st.form_submit_button("Change")
      if metode == 'Datang Langsung':
            jenis_kelamin = st.selectbox('Jenis Kelamin Pelanggan', ['Laki-Laki', 'Perempuan'])
      else:
            jenis_on_demand = st.selectbox('Jenis On Demand Services', ['Go Food', 'Grab Food', 'Shopee Food'])
      pembayaran = st.selectbox('Metode Pembayaran', ['Tunai', 'QRIS', 'Ovo', 'Dana', 'Gopay', 'ShopeePay'])
      total_biaya = st.number_input('Total Biaya Pesanan(Rupiah)', min_value=0, max_value=100000000, value=0)
      tanggal_struk = st.date_input('Tanggal Pembuatan Struk', value= date_slice)
      waktu_struk = st.time_input('Waktu Pembuatan Struk', value= time_fix)
      submit = st.form_submit_button("Submit")

if submit :
    if metode == 'Datang Langsung' :
        sql = "INSERT INTO datastruk_crisbar (metode_pemesanan, jenis_kelamin, metode_pembayaran, biaya_pemesanan, tanggal_pemesanan, waktu_pemesanan) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (metode, jenis_kelamin, pembayaran, total_biaya, tanggal_struk, waktu_struk)
    elif metode == 'On Demand Services' :
        sql = "INSERT INTO datastruk_crisbar (metode_pemesanan, on_demand, metode_pembayaran, biaya_pemesanan, tanggal_pemesanan, waktu_pemesanan) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (metode, jenis_on_demand, pembayaran, total_biaya, tanggal_struk, waktu_struk)
    cursor.execute(sql, val)
    conn.commit()
    st.success("Data berhasil disimpan!")
conn.close()
