import streamlit as st
import pandas as pd
import io

st.title("Actividad 1 - semana 10")

#leer el archivo csv
df = pd.read_csv('pages\static\estudiantes.cvs')

st.text("Mostrar los datos de Estudiantes")
#mostrar los primeros x datos
st.dataframe(df)

st.text("----------")

st.text("Agrupar por Género")
# Agrupando por 'Género' y crear un objeto
group_genero = df.groupby('Género')
#Muestra el objeto group_genero
st.dataframe(group_genero)
st.dataframe(df.groupby('Género'))

st.text("----------")

st.text("Resumen de Edad")
# Agrupando por 'Género'
# Muestra el objeto GroupBy
st.dataframe(df.groupby('Género'))

# Calculando la edad promedio por ciudad:
edad = group_genero['Edad']
st.dataframe(edad) 
