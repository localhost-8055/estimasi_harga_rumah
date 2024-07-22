import pickle
import streamlit as st

model = pickle.load(open('estimasi_rumah.sav', 'rb'))

st.title('Estimasi Harga Rumah')

luasb = st.number_input('Masukkan Luas Bangunan')
luast = st.number_input('Masukkan Luas Tanah (meter persegi)')
kamart = st.number_input('Masukkan Jumlah Kamar Tidur')
kamarm = st.number_input('Masukkan Jumlah Kamar Mandi')
garasi = st.number_input("Masukkan Jumlah Garasi")

predict = ''

if st.button('Estimasi Harga Rumah'):
    predict = model.predict(
        [[luasb, luast, kamart, kamarm, garasi]]
    )
    st.write('Estimasi Harga Rumah : ', predict)