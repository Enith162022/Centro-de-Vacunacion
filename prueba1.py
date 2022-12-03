# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 17:20:39 2022
@author: Enith
"""
#BARRA LATERAL#############################################
import streamlit as st
import pandas as pd
import numpy as np
import gdown

########################################################
#id = 1Y9A1gXBN8OgLXoNVAOE3Wm7zfCkpf9Y8
@st.experimental_memo
def download_data():
    url = "https://drive.google.com/uc?id= 1Y9A1gXBN8OgLXoNVAOE3Wm7zfCkpf9Y8"
    output = "data.csv"
    gdown.download(url,output,quiet = False)
download_data()
df = pd.read_csv('data.csv',sep = ";",  skip_blank_lines=True, nrows=19388,parse_dates=['latitud', 'longitud']

###################################################
st.sidebar.header("Barra de menú")
#st.header("sidebar")
#descripcion inicial
st.title("Centros de vacunación")
st.subheader("Integrantes")
st.write(""" - Aguilar Rojas, Enith""")  
st.write(""" - Fuertes Lizarbe, Mirko""")
st.write(""" - Rojas Rua, Rocio""")

st.subheader("¿Cual es el objetivo:") 
st.write("""Facilitar al usuario la disponibilidad de centros de vacunación, dada por una estrategia para poder promocionar y facilitar la Vacunación en el país""") 

st.subheader("Contexto") 
st.write("""El acceso equitativo a vacunas   seguras  y eficaces es fundamental""")
st.write("""para poner fin a la pandemia de COVID-19, por lo que es enormemente""")
st.write("""alentador ver que hay tantas vacunas en fase de prueba.La OMS  esta""")
st.write("""rabajando incansablemente con asociados para desarrollar , fabricar""")
st.write("""y desplegar vacunas seguras y eficaces.""")

from PIL import Image
image = Image.open('centro_vacuna.jpg')
st.image(image)


st.subheader("¿Cuáles son los síntomas del Coronavirus?") 
##############################################################################
col1, col2, col3= st.columns(3)
with col1:
    st.subheader("Síntomas habituales") 
    st.write("""- Fiebre""")  
    st.write("""- Cansancio""")
    st.write("""- Tos""")
    st.write("""- Pérdida del gusto o del olfato        
             """)
with col2:
    st.subheader("Síntomas menos habituales") 
    st.write("""- Dolor de garganta""")
    st.write("""- Molestias""")
    st.write("""- Diarrea""")
    st.write("""- Erupción cutánea        
             """)
    
with col3:
    st.subheader("Síntomas graves") 
    st.write("""-  Dificultad para respirar o falta de aire""")
    st.write("""- Pérdida del habla o la movilidad, o confusión""")
    st.write("""- Dolor en el pecho""")

st.write("**Fuente:** ONU https://www.who.int/es/health-topics/coronavirus#tab=tab_3")

option = st.selectbox(
    "Elija una modalidad de vacunación, Centros de Vacunacion o Vacuna Car",
    ("Centros de Vacunacion","Vacuna Car"))

st.write("Seleccionó:", option)
if option == 'Centros de Vacunación':   
#ENCABEZADO DE LA PÁGINA#######################################################
    st.title("       Centro de vacunación COVID19")
    st.write("Elija el departamento dónde desea vacunarse.")
    
    option = st.selectbox(
        "Departamentos",
        ("Abancay","Ayacucho","Junín","Lima","Loreto"))
    
    
    
