import streamlit as st 
from sklearn import linear_model
import pandas as pd
import numpy as np

df = pd.read_csv("toyota.csv")

model_regresi_linier = linear_model.LinearRegression()
model_regresi_linier.fit(df[['tahun']], df.harga)

st.title('Prediksi Harga Rumah')
tahun = st.number_input ("Masukkan tahun Mobil", 0)

if st.button ("cek harga") :
    hasil = int(model_regresi_linier.predict([[tahun]]))
    st.succes(f"Prediksi Harga Mobil = RP.{hasil}")