import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

st.subheader("Análisis y Filtrado de Datos")

df = pd.read_csv('pages/static/datasets/ventas.csv')


tad_descripcion, tab_Análisis_Exploratorio, tab_Filtrado_Básico, tab_Filtro_Final_Dinámico = st.tabs(["Descripción", "Análisis Exploratorio", "Filtrado Básico", "Filtro Final Dinámico"])

#----------------------------------------------------------
#Generador de datos
#----------------------------------------------------------
with tad_descripcion:      

    st.markdown('''
    ## Plantilla Básica para Proyecto Integrador

    ### Introducción

    -   ¿Qué es el proyecto?
    -   ¿Cuál es el objetivo principal?
    -   ¿Por qué es importante?

    ### Desarrollo

    -   Explicación detallada del proyecto
    -   Procedimiento utilizado
    -   Resultados obtenidos

    ### Conclusión

    -   Resumen de los resultados
    -   Logros alcanzados
    -   Dificultades encontradas
    -   Aportes personales
    ''')    

#----------------------------------------------------------
#Analítica 1
#----------------------------------------------------------
with tab_Análisis_Exploratorio:    
    st.title("Análisis Exploratorio")
    st.markdown("""
    * Muestra las primeras 5 filas del DataFrame.  **(df.head())**
    * Muestra la cantidad de filas y columnas del DataFrame.  **(df.shape)**
    * Muestra los tipos de datos de cada columna.  **(df.dtypes)**
    * Identifica y muestra las columnas con valores nulos. **(df.isnull().sum())**
    * Muestra un resumen estadístico de las columnas numéricas.  **(df.describe())**
    * Muestra una tabla con la frecuencia de valores únicos para una columna categórica seleccionada. **(df['columna_categorica'].value_counts())** 
    * Otra información importante           
    """)   

    st.text("----------")

    st.text("Muestra las primeras 5 filas del DataFrame.  (df.head())")
    #mostrar los primeros x datos
    st.dataframe(df.head(5))

    st.text("----------")

    st.text("Muestra la cantidad de filas y columnas del DataFrame.  (df.shape)")
    st.dataframe(df.shape)

    st.text("----------")

    st.text("Muestra los tipos de datos de cada columna.  (df.dtypes)")
    st.dataframe(df.dtypes)

    st.text("----------")

    st.text("Identifica y muestra las columnas con valores nulos. (df.isnull().sum())")
    st.dataframe(df.isnull().sum())

    st.text("----------")

    st.text("Muestra un resumen estadístico de las columnas numéricas.  (df.describe())")
    st.dataframe(df.describe())

    st.text("----------")

    st.text("Muestra una tabla con la frecuencia de valores únicos para una columna categórica seleccionada. **(df['columna_categorica'].value_counts())**")
    st.dataframe(df['Cantidad'].value_counts())


#----------------------------------------------------------
#Analítica 2
#----------------------------------------------------------
with tab_Filtrado_Básico:
    st.title("Filtro Básico")
    st.markdown("""
    * Permite filtrar datos usando condiciones simples. **(df[df['columna'] == 'valor'])**
    * Permite seleccionar una columna y un valor para el filtro. **(st.selectbox, st.text_input)**
    * Permite elegir un operador de comparación (igual, diferente, mayor que, menor que). **(st.radio)**
    * Muestra los datos filtrados en una tabla. **(st.dataframe)** 
    """)

    st.text("----------")

    st.text("Permite filtrar datos usando condiciones simples. (df[df['columna'] == 'valor'])")
    st.text("Se filtró por Cantidad == 15")
    st.dataframe((df[df['Cantidad']== 15]))

    st.text("----------")

    # st.text("Permite seleccionar una columna y un valor para el filtro. (st.selectbox, st.text_input)")
    # # Selección de la columna
    # columna = st.selectbox("Selecciona una columna:", df.columns)

    # # Input de texto para el valor a filtrar
    # valor = st.text_input("Introduce el valor a filtrar:")

    # # Filtrar el DataFrame si se ha introducido un valor
    # if valor:
    #     filtered_df = df[df[columna].astype(str).str.contains(valor, case=False)]
    #     st.write("DataFrame filtrado:")
    #     st.dataframe(filtered_df)
    # else:
    #     st.write("Introduce valor para filtrar.")

    st.text("----------")

    st.text("Permite elegir un operador de comparación (igual, diferente, mayor que, menor que). (st.radio)")
    #st.text("Seleccione una columna desde el ejercicio anterior")

    
    st.title("Filtro de DataFrame")

    # Selección de la columna
    columna_filt = st.selectbox("Selecciona una columna:", df.columns)

    # Input de texto para el valor a filtrar
    #valor_filt = st.text_input("Introduce el valor a filtrar:")
    # Selección del operador de comparación
    # operador = st.radio("Selecciona un operador de comparación:", 
    #                     ('Igual', 'Diferente', 'Mayor que', 'Menor que'))

    # # Filtrar el DataFrame según el operador seleccionado
    # if valor:
    #     if columna in ['Edad']:  # Asegurarse de que la columna es numérica para comparar
    #         valor = float(valor)
    #         if operador == 'Igual':
    #             filtered_df = df[df[columna] == valor]
    #         elif operador == 'Diferente':
    #             filtered_df = df[df[columna] != valor]
    #         elif operador == 'Mayor que':
    #             filtered_df = df[df[columna] > valor]
    #         elif operador == 'Menor que':
    #             filtered_df = df[df[columna] < valor]
    #     else:
    #         # Para columnas no numéricas (como 'Nombre' y 'Ciudad')
    #         if operador == 'Igual':
    #             filtered_df = df[df[columna].str.lower() == valor.lower()]
    #         elif operador == 'Diferente':
    #             filtered_df = df[df[columna].str.lower() != valor.lower()]
    #         # Mayor que y Menor que no se aplican a columnas de texto
    #         filtered_df = pd.DataFrame()  # Reiniciar si no se aplica

    #     # Mostrar el DataFrame filtrado
    #     if not filtered_df.empty:
    #         st.write("DataFrame filtrado:")
    #         st.dataframe(filtered_df)
    #     else:
    #         st.write("No se encontraron coincidencias.")
    # else:
    #     st.write("Introduce un valor para filtrar.")
    
    st.text('-----------')

    genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    index=None,
    )

    st.write("You selected:", genre)



#----------------------------------------------------------
#Analítica 3
#----------------------------------------------------------
with tab_Filtro_Final_Dinámico:
    st.title("Filtro Final Dinámico")
    st.markdown("""
    * Muestra un resumen dinámico del DataFrame filtrado. 
    * Incluye información como los criterios de filtrado aplicados, la tabla de datos filtrados, gráficos y estadísticas relevantes.
    * Se actualiza automáticamente cada vez que se realiza un filtro en las pestañas anteriores. 
    """)

    st.text('--------------------------')

    # Crear un DataFrame de ejemplo
    data = {
        'Nombre': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Edad': [24, 30, 22, 35, 28],
        'Ciudad': ['Madrid', 'Barcelona', 'Madrid', 'Sevilla', 'Barcelona']
    }
    df = pd.DataFrame(data)

    # Título de la aplicación
    st.title("Filtro de DataFrame con Resumen Dinámico")

    # Selección de la columna
    columna = st.selectbox("Selecciona una columna:", df.columns)

    # Input de texto para el valor a filtrar
    valor = st.text_input("Introduce el valor a filtrar:")

    # Selección del operador de comparación
    operador = st.radio("Selecciona un operador de comparación:", 
                            ('Igual', 'Diferente', 'Mayor que', 'Menor que'))

    # Inicializar el DataFrame filtrado
    filtered_df = df.copy()

    # Filtrar el DataFrame según el operador seleccionado
    if valor:
        if columna in ['Edad']:  # Asegurarse de que la columna es numérica para comparar
            try:
                valor = float(valor)
            except ValueError:
                st.error("Por favor, introduce un número válido para la columna 'Edad'.")
                valor = None

            if valor is not None:
                if operador == 'Igual':
                    filtered_df = df[df[columna] == valor]
                elif operador == 'Diferente':
                    filtered_df = df[df[columna] != valor]
                elif operador == 'Mayor que':
                    filtered_df = df[df[columna] > valor]
                elif operador == 'Menor que':
                    filtered_df = df[df[columna] < valor]
        else:
            # Para columnas no numéricas (como 'Nombre' y 'Ciudad')
            if operador == 'Igual':
                filtered_df = df[df[columna].str.lower() == valor.lower()]
            elif operador == 'Diferente':
                filtered_df = df[df[columna].str.lower() != valor.lower()]
            # Mayor que y Menor que no se aplican a columnas de texto

    # Mostrar el resumen dinámico
    st.subheader("Resumen de los Resultados Filtrados")

    # Mostrar criterios de filtrado
    if valor:
        st.write(f"Criterios de filtrado: **{columna} {operador} {valor}**")
    else:
        st.write("No se han aplicado criterios de filtrado.")

    # Mostrar la tabla de datos filtrados
    st.write("Datos filtrados:")
    st.dataframe(filtered_df)

    # Mostrar estadísticas relevantes
    if not filtered_df.empty:
        st.write("Estadísticas descriptivas:")
        st.write(filtered_df.describe(include='all'))

        # Gráficos: Histograma de edades si la columna 'Edad' está en el DataFrame
        if 'Edad' in filtered_df.columns:
            st.subheader("Distribución de Edades")
            plt.figure(figsize=(8, 4))
            plt.hist(filtered_df['Edad'], bins=5, color='skyblue', edgecolor='black')
            plt.xlabel('Edad')
            plt.ylabel('Frecuencia')
            plt.title('Histograma de Edades Filtradas')
            st.pyplot(plt)

    else:
        st.write("No se encontraron coincidencias.")

            




