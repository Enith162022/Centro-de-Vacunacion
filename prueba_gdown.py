
import streamlit as st
import pandas as pd
import gdown

#id=13iNig4VIvt5Gm0znUt2eq3_YnGCgCQHM
@st.experimental_nemo
def dowload_data():
	#https://drive.google.com/uc?id=MIOOO
	url="https://drive.google.com/uc?id=13iNig4VIvt5Gm0znUt2eq3_YnGCgCQHM"
	output="data.csv"
	gdown.download(url,output,quiet=False)
download_data()
#df = pd.read_csv(r'C:\Users\51952\Downloads\PositivosCovid\positivos_covid.csv',sep=";", skip_blank_lines=True, parse_dates=['id_centro_vacunacion', 'id_eess'])
df = pd.read_csv('data.csv',sep = ";",  skip_blank_lines=True, nrows=1000,parse_dates=['id_centro_vacunacion', 'id_eess'])
st.dataframe(data.head(20))
