import streamlit as st
import pandas as pd
import io
import numpy as np

st.title("Actividad 1 - semana 10")

#leer el archivo csv
df = pd.read_csv('pages\static\estudiantes.cvs')

st.text("Mostrar los datos de Estudiantes")
#mostrar los primeros x datos
st.dataframe(df)

st.text("----------")

st.text("Agrupa el DataFrame por la columna 'Género'")
# Agrupando por 'Género' y crear un objeto
group_genero = df.groupby('Género')
#Muestra el objeto group_genero
st.dataframe(group_genero)

st.text("----------")

st.text("Calcula la edad promedio de los estudiantes por género")
# Resumen de Edad
edad_promedio = group_genero['Edad'].mean()
st.dataframe(edad_promedio)

st.text("----------")

st.text("Calcula la calificación promedio por género")
# Resumen de Calificaciones
calificacion_promedio = group_genero['Calificación'].mean()
st.dataframe(calificacion_promedio)

st.text("----------")

st.text("Calcula la calificación máxima por género")
calificacion_maxima = group_genero['Calificación'].max()
st.dataframe(calificacion_maxima)

st.text("----------")

st.text("Tabla Resumen")
# Tabla de Resumen
resumen = pd.DataFrame({
    'Edad Promedio': edad_promedio,
    'Calificación Promedio': calificacion_promedio,
    'Calificación Máxima': calificacion_maxima
}).reset_index()

st.dataframe(resumen)


st.text("----------")

st.text("Calcular la cantidad de estudiantes por género")
group_genero = df.groupby('Género')
conteo_genero = group_genero['Género'].count()
#Muestra el objeto conteo_genero
st.dataframe(conteo_genero)

st.text("----------")

st.text("Ordenar la tabla de resumen por la calificación promedio de forma descendente")
resumen = pd.DataFrame({
    'Edad Promedio': edad_promedio,
    'Calificación Promedio': calificacion_promedio,
    'Calificación Máxima': calificacion_maxima
}).sort_values(by='Calificación Promedio', ascending=False)

st.dataframe(resumen)

st.text("----------")

st.text("Agregar una nueva columna al DataFrame con la categoría de edad (por ejemplo, Joven para estudiantes menores de 19 años y Adulto para estudiantes mayores o iguales a 19 años)")

# Agregar columna de categoría de edad
df['Categoría de Edad'] = np.where(df['Edad'] < 19, 'Joven', 'Adulto')
st.dataframe(df)



