import streamlit as st
import pandas as pd

st.title("Ejemplo 6 - semana 11")

st.text("st.vega_lite_chart")

datos_peces = pd.DataFrame({
    'Especie': ['Trucha', 'Salmón', 'Bacalao', 'Atún', 'Sardina'],
    'Longitud (cm)': [30, 45, 60, 75, 20],
    'Peso (kg)': [2.5, 3.2, 4.8, 6.1, 0.5]
})

st.vega_lite_chart(datos_peces, {
    'mark': {'type': 'circle', 'tooltip': True},
    'encoding': {
        'x': {'field': 'Longitud (cm)', 'type': 'quantitative'},
        'y': {'field': 'Peso (kg)', 'type': 'quantitative'},
        'size': {'field': 'Longitud (cm)', 'type': 'quantitative'},
        'color': {'field': 'Especie', 'type': 'nominal'},
    },
})