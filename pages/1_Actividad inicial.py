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

#slider
age = st.slider("Edad ", 1, 100, 20)
st.write("Edad por donde va el slider", age, "años")

#crea un tf desde la clumna Ciudad donde la ciudades sean la seleccionadas en el selectbox
#df_ciudad = df[df['Ciudad']== option]

#crea un tf desde la clumna Ciudad donde la ciudades sean la seleccionadas en el selectbox
#se le adiciona el df Edad 
df_ciudad = df[(df['Ciudad']== option) & (df['Edad']>age)]


#imprime todos las columnas
#df_ciudad

#seleccionar que columnas se quieren ver
df_ciudad[['Edad','Ingreso','Genero','Fecha_Nacimiento']]

