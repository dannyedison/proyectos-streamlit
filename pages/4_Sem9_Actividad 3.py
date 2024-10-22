import streamlit as st
import pandas as pd
import io

st.title("Actividad 3 - semana 9")

#leer el archivo csv
df = pd.read_csv('pages\static\datasets\educacion.csv')
#Imprime todo el dataframe
#st.dataframe(df)

st.text("Mostrar las primeras cinco filas")
#mostrar los primeros x datos
st.dataframe(df.head(5))

st.text("----------")

st.text("Mostara la información del df")
# Captura la información en un buffer
buffer = io.StringIO()
df.info(buf=buffer)
info_str = buffer.getvalue()

# Mostrar la información en Streamlit
st.text(info_str)

st.text("----------")

st.text("Mostara la estadísticas descriptivas df")
# Calcular estadísticas descriptivas
# Mostrar en Streamlit
st.dataframe(df.describe())

st.text("----------")

st.text("Cuáles son los niveles educativos más comunes")
st.dataframe(df['Nivel_Educativo'].value_counts())

st.text("----------")

st.text("Cuál es la carrera más popular")
st.text(df['Carrera'].value_counts().idxmax())

st.text("----------")

st.text("Cuál es la institución con más estudiantes")
st.text(df['Institución'].value_counts().idxmax())

st.text("----------")

st.text("Filtra los estudiantes que tienen un posgrado")
df_posgrado = df[df['Nivel_Educativo'] == 'Posgrado']
st.dataframe(df_posgrado)

st.text("----------")

st.text("Filtra los estudiantes de Ingeniería Informática de la Universidad Complutense de Madrid")

df_ingenieria_madrid = df[(df['Carrera'] == 'Ingeniería Informática') & (df['Institución'] == 'Universidad Complutense de Madrid')]
st.dataframe(df_ingenieria_madrid)

st.text("----------")

st.text("Filtra los estudiantes de Honduras que tienen un nivel educativo universitario")

df_honduras_universitario = df[(df['País'] == 'Honduras') & (df['Nivel_Educativo'] == 'Universitario')]
st.dataframe(df_honduras_universitario)

st.text("----------")

st.text("Crea una tabla de frecuencia que muestre la cantidad de estudiantes por país y nivel educativo")
st.dataframe(pd.crosstab(df['País'], df['Nivel_Educativo']))

st.text("----------")

st.text("Calcula la edad promedio de los estudiantes por nivel educativo")
st.dataframe(df.groupby('Nivel_Educativo')['Edad'].mean())

st.text("----------")

st.text("Guarda el DataFrame filtrado 'df_posgrado' en un nuevo archivo CSV")
df_posgrado.to_csv('posgrado.csv', index=False) 