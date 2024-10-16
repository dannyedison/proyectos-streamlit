import streamlit as st
import altair as alt
import pandas as pd

st.title("Ejemplo 5 - semana 11")

st.text("st.altair_chart")

# Sport popularity data
sports = ['Football', 'Basketball', 'Baseball', 'Tennis']
popularity = [300, 150, 100, 50]

# Create DataFrame
data = pd.DataFrame({
    'sport': sports,
    'popularity': popularity
})

# Create chart
c = alt.Chart(data).mark_circle().encode(
    x='sport',
    y='popularity',
    size='popularity'
)

st.altair_chart(c, use_container_width=True)