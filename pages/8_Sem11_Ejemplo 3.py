import streamlit as st
import pandas as pd

st.title("Ejemplo 3 - semana 11")

st.text("st.bar_chart")

# Crear el DataFrame con la cantidad de animales por tipo
data = {
    'Tipo': ['Perro', 'Gato', 'Pájaro', 'Conejo', 'Hamster'],
    'Cantidad': [50, 30, 20, 10, 5]
}

df = pd.DataFrame(data)

# Mostrar el DataFrame
st.write(df)

# Graficar el DataFrame con un gráfico de barras
st.bar_chart(df.set_index('Tipo'))