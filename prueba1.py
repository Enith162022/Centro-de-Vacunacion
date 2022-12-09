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

from pyecharts import options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts
from streamlit_echarts import st_echarts
###################################################
st.sidebar.header("Barra de menú")
st.title(':syringe: Centros de Vacunación') 
st.subheader("Integrantes")
st.write(""" - Aguilar Rojas, Enith""")  
st.write(""" - Fuertes Lizarbe, Mirko Frank""")
st.write(""" - Rojas Rua, Rocio""")
######################################################
st.subheader("¿Cual es el objetivo:") 
st.write("""Facilitar al usuario la disponibilidad de centros de vacunación en todo el país, dada por una estrategia para poder promocionar y facilitar la Vacunación en diversos departamentos y respectivos distritos de todo el Perú""") 
st.subheader("Contexto") 
st.write("""El acceso equitativo a vacunas   seguras  y eficaces es fundamental para poner fin a la pandemia de COVID-19, por lo que es enormemente alentador ver que hay tantas vacunas en fase de prueba.""")
st.write("""La OMS  está trabajando incansablemente con asociados para desarrollar, fabricar y desplegar vacunas seguras y eficaces.""")
from PIL import Image
image = Image.open('centro_vacuna.jpg')
st.image(image)
st.subheader("¿Cuáles son los síntomas del Coronavirus?") 
##############################################################################
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
################################################################
archivo_excel = 'CVF.xlsx' 
hoja_excel = 'TABLA' 
df = pd.read_excel(archivo_excel,
                   sheet_name = hoja_excel,
                   usecols = 'B:D')

st.sidebar.header("Departamentos del Perú:")
Depart = st.sidebar.multiselect(
    "Seleccione un departamento:",
    #options = df['Departamento'].unique(),
    default = df['Departamento'].unique() 
)

Centros = st.sidebar.multiselect(
    "Seleccione:",
    options = df['# Centros de Vacunación'].unique(),
    default = df['# Centros de Vacunación'].unique()
)

df_seleccion = df.query("Departamento == @Depart  & # Centros de Vacunación == @Centros" )

################################################################
#id=13iNig4VIvt5Gm0znUt2eq3_YnGCgCQHM
#@st.experimental_nemo
def dowload_data():
    url="https://drive.google.com/uc?id=13iNig4VIvt5Gm0znUt2eq3_YnGCgCQHM"
    output="data.csv"
    gdown.download(url,output,quiet=False)

#############################

"""st.write("Seleccionó:", option)
if option == 'Centros de Vacunación':   
#ENCABEZADO DE LA PÁGINA#######################################################
    st.title("       Centro de vacunación COVID19")
    st.write("Elija el departamento dónde desea vacunarse.")
    
    option = st.selectbox(
        "Departamentos",
        ("Abancay","Ayacucho","Junín","Lima","Loreo"))"""
    
    
    
