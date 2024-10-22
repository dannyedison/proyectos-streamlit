import streamlit as st
import pandas as pd
import io

st.title("Actividad 2 - semana 9")

#leer el archivo csv
df = pd.read_csv('pages\static\datasets\Ventas2.csv')
#Imprime todo el dataframe
#st.dataframe(df)

st.text("Selecciona las filas con índices 5 a 10.")
# Mostrar la información en Streamlit
st.dataframe(df.iloc[5:10]) 

st.text("----------")

st.text("Selecciona las columnas Producto y Precio")
# Mostrar la información en Streamlit
st.dataframe(df.loc[:,['Producto','Precio']])

st.text("----------")

st.text("Filtra las filas donde el 'Precio' es mayor que 100000.")
# Mostrar la información en Streamlit
st.dataframe(df[df['Precio'] > 100000])

st.text("----------")

st.text("Crea una nueva columna llamada Descuento con un 10% del Precio.")
# Crear nueva columna
df['Descuento'] = df['Precio'] * 0.9
# Mostrar la información en Streamlit
st.dataframe(df)

st.text("----------")

st.text("Elimina la columna Descuento del DataFrame.")
# Elimina la columna Descuento
df.drop('Descuento', axis=1, inplace=True)
st.dataframe(df)