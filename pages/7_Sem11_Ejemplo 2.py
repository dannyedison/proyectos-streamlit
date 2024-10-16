import streamlit as st
import pandas as pd
import numpy as np

st.title("Ejemplo 2 - semana 11")

st.text("st.area_chart")

# Crear el DataFrame con los ingresos de tres tiendas en cuatro trimestres
data = {
    'Tienda': ['Tienda 1', 'Tienda 1', 'Tienda 1', 'Tienda 1', 'Tienda 2', 'Tienda 2', 'Tienda 2', 'Tienda 2', 'Tienda 3', 'Tienda 3', 'Tienda 3', 'Tienda 3'],
    'Trimestre': ['Q1', 'Q2', 'Q3', 'Q4', 'Q1', 'Q2', 'Q3', 'Q4', 'Q1', 'Q2', 'Q3', 'Q4'],
    'Ingresos': [100, 120, 110, 130, 80, 190, 100, 110, 270, 80, 85, 90]
}

df = pd.DataFrame(data)

# Mostrar el DataFrame
st.write(df)

# Graficar el DataFrame con un gráfico de área
df_pivot = df.pivot(index='Tienda', columns='Trimestre', values='Ingresos')
st.area_chart(df_pivot)