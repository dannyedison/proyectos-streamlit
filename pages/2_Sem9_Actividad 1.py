import streamlit as st
import pandas as pd
import io

st.title("Actividad 1 - semana 9")



#leer el archivo csv
df = pd.read_csv('pages\static\datasets\datos_demograficos.csv')

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
#estadisticas = df.describe()

# Mostrar en Streamlit
st.dataframe(df.describe())

st.text("----------")

st.text("Encuentra los valores únicos de la columna País ")
#Crear df_pais donde se almacena el nuevo df con el valor único
df_pais= df['País'].unique()
# Mostrar en Streamlit
st.dataframe(df_pais)

st.text("----------")

st.text("Cuenta la cantidad de ocurrencias de cada valor en la columna Género")
#Crear df_genero donde se almacena el nuevo df con el valor de las ocurrencias
df_genero = df['Género'].value_counts()
# Mostrar en Streamlit
st.dataframe(df_genero)