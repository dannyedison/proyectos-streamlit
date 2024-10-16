import streamlit as st 
import matplotlib.pyplot as plt
import numpy as np

st.title("Ejemplo 4 - semana 11")

st.text("st.pyplot")

# Datos de insectos
mosca = 100
hormiga = 50 
mariposa = 20
escarabajo = 30

# Categorías de insectos
insectos = ['Moscas', 'Hormigas', 'Mariposas', 'Escarabajos']

# Frecuencia de insectos
frecuencias = [mosca, hormiga, mariposa, escarabajo]

# Crear el gráfico 
fig = plt.figure(figsize=(8,4))
ax = fig.add_subplot(111)  
ax.bar(insectos, frecuencias)

# Mostrar el gráfico  
st.pyplot(fig)