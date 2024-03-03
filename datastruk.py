import streamlit as st
from datetime import datetime, time
import mysql.connector
from sqlalchemy import create_engine, Column, Integer, String, Date, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

host= st.secrets.connections.mysql.host
port = str(st.secrets.connections.mysql.port)
user= st.secrets.connections.mysql.username
password= st.secrets.connections.mysql.password
database= st.secrets.connections.mysql.database


engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}", pool_pre_ping=True)

Base = declarative_base()

class Data(Base):
    __tablename__ = 'datastruk'

    id = Column(Integer, primary_key=True, autoincrement='auto')
    metode_pemesanan = Column(String(45))
    jenis_kelamin = Column(String(45))
    on_demand = Column(String(45))
    metode_pembayaran = Column(String(45))
    biaya_pemesanan = Column(Integer)
    tanggal_pemesanan = Column(Date)
    waktu_pemesanan = Column(Time)

# Buat session untuk interaksi dengan database
Session = sessionmaker(bind=engine)
session = Session()

tanggal = datetime.now()
date_slice = tanggal.date()
hour = (int(tanggal.strftime("%H"))+7)%24
minutes = int(tanggal.strftime("%M"))
seconds = int(tanggal.strftime("%S"))
time_fix = time(hour,minutes, seconds)


st.title('Data Struk Crisbar')

with st.form("first_form2"):
      metode = st.selectbox('Metode Pemesanan', ['Datang Langsung', 'On Demand Services'])
      change = st.form_submit_button("Change")
      if metode == 'Datang Langsung':
            jenis_kelamin_box = st.selectbox('Jenis Kelamin Pelanggan', ['Laki-Laki', 'Perempuan'])
      else:
            jenis_on_demand = st.selectbox('Jenis On Demand Services', ['Go Food', 'Grab Food', 'Shopee Food'])
      pembayaran = st.selectbox('Metode Pembayaran', ['Tunai', 'QRIS', 'OVO', 'Dana', 'Gopay', 'ShopeePay'])
      total_biaya = st.number_input('Total Biaya Pesanan(Rupiah)', min_value=0, max_value=100000000, value=0)
      tanggal_struk = st.date_input('Tanggal Pembuatan Struk', value= date_slice)
      waktu_struk = st.time_input('Waktu Pembuatan Struk', value= time_fix)
      submit = st.form_submit_button("Submit")

if submit :
    if metode == 'Datang Langsung' :
         new_data = Data(metode_pemesanan = metode, jenis_kelamin = jenis_kelamin_box, metode_pembayaran = pembayaran, biaya_pemesanan = total_biaya, tanggal_pemesanan = tanggal_struk, waktu_pemesanan = waktu_struk)
    elif metode == 'On Demand Services' :
                  new_data = Data(metode_pemesanan = metode, on_demand = jenis_on_demand, metode_pembayaran = pembayaran, biaya_pemesanan = total_biaya, tanggal_pemesanan = tanggal_struk, waktu_pemesanan = waktu_struk)
    session.add(new_data)
    session.commit()
    st.success("Data berhasil disimpan!")
session.close()
