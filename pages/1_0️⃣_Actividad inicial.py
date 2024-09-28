import streamlit as st
import pandas as pd

#leer el archivo csv
df = pd.read_csv('pages\static\datos.csv')

#imprimir columnas
#df.columns

#traer todas las ciudades
#df_ciudades = df['Ciudad']

#trae las ciudades sin repetirlas
df_ciudades = df['Ciudad'].unique()


option = st.selectbox(
    "Ciudad",
    df_ciudades,
)

#muestra la cuidad seleccionada
st.write("Ha seleccionado la ciudad de: ", option)

#crea un tf desde la clumna Ciudad donde la ciudades sean la seleccionadas en el selectbox
df_ciudad = df[df['Ciudad']== option]

#imprime todos las columnas
#df_ciudad

#seleccionar que columnas se quieren ver
df_ciudad[['Edad','Ingreso','Genero','Fecha_Nacimiento']]

