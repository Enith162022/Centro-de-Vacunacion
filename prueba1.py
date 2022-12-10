# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 17:20:39 2022
@author: Enith
"""
#BARRA LATERAL
########################################################
import gdown
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import urllib.request
import base64
from pyecharts import options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts
from streamlit_echarts import st_echarts
###################################################
st.title(':syringe: Centros de Vacunación') 
st.subheader("Integrantes")
st.write(""" - Aguilar Rojas, Enith""")  
st.write(""" - Lizarbe Fuertes, Mirko Frank""")
st.write(""" - Rojas Rua, Rocio""")

st.sidebar.header("Barra de menú")

    
######################################################
st.subheader("¿Cual es el objetivo:") 
st.write("""Facilitar al usuario la disponibilidad de centros de vacunación en todo el país, dada por una estrategia para poder promocionar y facilitar la Vacunación en diversos departamentos y respectivos distritos de todo el Perú""") 
st.subheader("Contexto") 
st.write("""El acceso equitativo a vacunas   seguras  y eficaces es fundamental para poner fin a la pandemia de COVID-19, por lo que es enormemente alentador ver que hay tantas vacunas en fase de prueba. La OMS  está trabajando incansablemente con asociados para desarrollar, fabricar y desplegar vacunas seguras y eficaces.""")
#st.markdown("![Alt Text](https://lottiefiles.com/21474-medical-frontliners)")
file_ = open("21474-medical-frontliners.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()
st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True, ) 
#from PIL import Image
#image = Image.open('centro_vacuna.jpg')
#st.image(image)
##############################################################################
st.subheader("¿Cuáles son los síntomas del Coronavirus?") 
col1, col2, col3= st.columns(3)
with col1:
    st.subheader("Síntomas habituales:frowning:")   
    st.write("""- Cansancio""")
    st.write("""- Tos""")
    st.write("""- Fiebre""")
    st.write("""- Pérdida del gusto o del olfato
    """)
with col2:
    st.subheader("Síntomas menos habituales:confused:") 
    st.write("""- Dolor de garganta""")
    st.write("""- Molestias""")
    st.write("""- Erupción cutánea""")
    st.write("""- Diarrea
    """) 
with col3:
    st.subheader("Síntomas graves:mask:") 
    st.write("""-  Dificultad para respirar o falta de aire""")
    st.write("""- Pérdida del habla o la movilidad, o confusión""")
    st.write("""- Dolor en el pecho
    """)
st.write("**Fuente:** ONU https://www.who.int/es/health-topics/coronavirus#tab=tab_3")
option = ["Departamentos", "nombre"]
model = st.sidebar.selectbox("Elija una opción",option)
################################################################
st.subheader("Base de datos") 
st.write("""La base de datos trabaja con un total de 19385 Centros de Vacunación en todo el país""")  
archivo_excel = "DATOSF.xlsx"
hoja_excel = "TABLA1"
df = pd.read_excel(archivo_excel,
                   sheet_name = hoja_excel,
                   usecols = "A:C", )
st.dataframe(df)
pie_chart = px.pie(df, 
                   title = 'Cantidad de Centros de Vacunación por cada departamento', 
                   values = 'C.Vac',
                   names = 'Departamento') 
st.plotly_chart(pie_chart) 
#############################departamentos##############################################
st.subheader("Seleccione el departamento donde requiere vacunarse") 
st.write("Se le presentará diversos Centros de Vacunación en el departamento de su elección")
coli1, coli2= st.columns(2)
with coli1:
    result =st.button("Amazonas")
    if result:
        archivo_excel = "departamentos.xlsx"
        hoja_excel = "Amazonas"
        df = pd.read_excel(archivo_excel,
                       sheet_name = hoja_excel,
                       usecols = "A:B",)
        st.dataframe(df)
with coli2:
    result =st.button("Ancash") 
    if result:
        archivo_excel = "departamentos.xlsx"
        hoja_excel = "Ancash"
        df = pd.read_excel(archivo_excel,
                       sheet_name = hoja_excel,
                       usecols = "A:B",
                      )
        st.dataframe(df)
        
cole1, cole2= st.columns(2)
with cole1:
    result =st.button("Apurimac")
    if result:
        archivo_excel = "departamentos.xlsx"
        hoja_excel = "Apurimac"
        df = pd.read_excel(archivo_excel,
                       sheet_name = hoja_excel,
                       usecols = "A:B", )
        st.dataframe(df)
with cole2:
    result =st.button("Arequipa")
    if result:
        archivo_excel = "departamentos.xlsx"
        hoja_excel = "Arequipa"
        df = pd.read_excel(archivo_excel,
                       sheet_name = hoja_excel,
                       usecols = "A:B", )
        st.dataframe(df)
cola1, cola2= st.columns(2)
with cola1:
    result =st.button("Ayacucho")
    if result:
        archivo_excel = "departamentos.xlsx"
        hoja_excel = "Ayacucho"
        df = pd.read_excel(archivo_excel,
                       sheet_name = hoja_excel,
                       usecols = "A:B",
                      )
        st.dataframe(df)
with cola2:
    result =st.button("Cajamarca")
    if result:
        archivo_excel = "departamentos.xlsx"
        hoja_excel = "Cajamarca"
        df = pd.read_excel(archivo_excel,
                       sheet_name = hoja_excel,
                       usecols = "A:B",
                      )
        st.dataframe(df)
colio1, colio2= st.columns(2)
with colio1:
    result =st.button("Callao")
    if result:
        archivo_excel = "departamentos.xlsx"
        hoja_excel = "Callao"
        df = pd.read_excel(archivo_excel,
                       sheet_name = hoja_excel,
                       usecols = "A:B", )
        st.dataframe(df)
with colio2:
    result =st.button("Cuzco")
    if result:
        archivo_excel = "departamentos.xlsx"
        hoja_excel = "Cuzco"
        df = pd.read_excel(archivo_excel,
                       sheet_name = hoja_excel,
                       usecols = "A:B", )
        st.dataframe(df)
colia1, colia2= st.columns(2)
with colia1:
    result =st.button("Huancavelica")
    if result:
        archivo_excel = "departamentos.xlsx"
        hoja_excel = "Huancavelica"
        df = pd.read_excel(archivo_excel,
                       sheet_name = hoja_excel,
                       usecols = "A:B", )
        st.dataframe(df)
with colia2:
    result =st.button("Huanuco")
    if result:
        archivo_excel = "departamentos.xlsx"
        hoja_excel = "Huanuco"
        df = pd.read_excel(archivo_excel,
                       sheet_name = hoja_excel,
                       usecols = "A:B", )
        st.dataframe(df)
colu1, colu2= st.columns(2)
with colu1:
    result =st.button("Ica")
    if result:
        archivo_excel = "departamentos.xlsx"
        hoja_excel = "Ica"
        df = pd.read_excel(archivo_excel,
                       sheet_name = hoja_excel,
                       usecols = "A:B", )
        st.dataframe(df)
with colu2:  
    result =st.button("Junín")
    if result:
        archivo_excel = "departamentos.xlsx"
        hoja_excel = "Junín"
        df = pd.read_excel(archivo_excel,
                       sheet_name = hoja_excel,
                       usecols = "A:B",
                      )
        st.dataframe(df)
colum1, colum2= st.columns(2)
with colum1:
    result =st.button("La Libertad")    
    if result:
        archivo_excel = "departamentos.xlsx"
        hoja_excel = "La Libertad"
        df = pd.read_excel(archivo_excel,
                       sheet_name = hoja_excel,
                       usecols = "A:B",
                      )
        st.dataframe(df)
with colum2:
    result =st.button("Lambayeque")
    if result:
        archivo_excel = "departamentos.xlsx"
        hoja_excel = "Lambayeque"
        df = pd.read_excel(archivo_excel,
                       sheet_name = hoja_excel,
                       usecols = "A:B",
                      )
        st.dataframe(df)
column1, column2= st.columns(2)
with column1:
    result =st.button("Lima")
    if result:
        archivo_excel = "departamentos.xlsx"
        hoja_excel = "Lima"
        df = pd.read_excel(archivo_excel,
                       sheet_name = hoja_excel,
                       usecols = "A:B",
                      )
        st.dataframe(df)
with column2:
    result =st.button("Loreto")
    if result:
        archivo_excel = "departamentos.xlsx"
        hoja_excel = "Loreto"
        df = pd.read_excel(archivo_excel,
                       sheet_name = hoja_excel,
                       usecols = "A:B",
                      )
        st.dataframe(df)
columna1, columna2= st.columns(2)
with columna1:
    result =st.button("Madre de Dios")    
    if result:
        archivo_excel = "departamentos.xlsx"
        hoja_excel = "Madre de Dios"
        df = pd.read_excel(archivo_excel,
                       sheet_name = hoja_excel,
                       usecols = "A:B",
                      )
        st.dataframe(df)
with columna2:
    result =st.button("Moquegua")
    if result:
        archivo_excel = "departamentos.xlsx"
        hoja_excel = "Moquegua"
        df = pd.read_excel(archivo_excel,
                       sheet_name = hoja_excel,
                       usecols = "A:B",
                      )
        st.dataframe(df)
colt1, colt2= st.columns(2)
with colt1:
    result =st.button("Pasco")
    if result:
        archivo_excel = "departamentos.xlsx"
        hoja_excel = "Pasco"
        df = pd.read_excel(archivo_excel,
                       sheet_name = hoja_excel,
                       usecols = "A:B",
                      )
        st.dataframe(df)
with colt2:
    result =st.button("Piura")
    if result:
        archivo_excel = "departamentos.xlsx"
        hoja_excel = "Piura"
        df = pd.read_excel(archivo_excel,
                       sheet_name = hoja_excel,
                       usecols = "A:B",
                      )
        st.dataframe(df)
coln1, coln2= st.columns(2)
with coln1:
    result =st.button("Puno")
    if result:
        archivo_excel = "departamentos.xlsx"
        hoja_excel = "Puno"
        df = pd.read_excel(archivo_excel,
                       sheet_name = hoja_excel,
                       usecols = "A:B",
                      )
        st.dataframe(df)
with coln2:
    result =st.button("San Martin")
    if result:
        archivo_excel = "departamentos.xlsx"
        hoja_excel = "San Martin"
        df = pd.read_excel(archivo_excel,
                       sheet_name = hoja_excel,
                       usecols = "A:B",
                      )
        st.dataframe(df)
colm1, colm2= st.columns(2)
with colm1:
    result =st.button("Tacna")    
    if result:
        archivo_excel = "departamentos.xlsx"
        hoja_excel = "Tacna"
        df = pd.read_excel(archivo_excel,
                       sheet_name = hoja_excel,
                       usecols = "A:B",
                      )
        st.dataframe(df)
with colm2:
    result =st.button("Tumbes")
    if result:
        archivo_excel = "departamentos.xlsx"
        hoja_excel = "Tumbes"
        df = pd.read_excel(archivo_excel,
                       sheet_name = hoja_excel,
                       usecols = "A:B",
                      )
        st.dataframe(df)   
result =st.button("Ucayali")
if result:
    archivo_excel = "departamentos.xlsx"
    hoja_excel = "Ucayali"
    df = pd.read_excel(archivo_excel,
                   sheet_name = hoja_excel,
                   usecols = "A:B",
                  )
    st.dataframe(df)
##########################################################################################
#id=13iNig4VIvt5Gm0znUt2eq3_YnGCgCQHM
#@st.experimental_nemo
#def dowload_data():
    #url="https://drive.google.com/uc?id=13iNig4VIvt5Gm0znUt2eq3_YnGCgCQHM"
    #output="data.csv"
    #gdown.download(url,output,quiet=False)    
