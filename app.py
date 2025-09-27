import streamlit as st
import pandas as pd
import plotly.graph_objects as go


# Configurar la página
st.title('Análisis de Vehículos Usados')
st.header('Exploración de datos de vehículos')

# Cargar los datos
@st.cache_data
def load_data():
    return pd.read_csv('vehicles_us.csv')

# Cargar el dataset
car_data = load_data()

# Mostrar información básica del dataset
st.subheader('Vista previa de los datos')
st.write('Primeras 5 filas del dataset:')
st.dataframe(car_data.head())


# Crear un botón en la aplicación Streamlit
hist_checkbox = st.checkbox('Construir histograma')

graph_checkbox = st.checkbox('Construir grafico de dispersion')

# Lógica a ejecutar cuando se hace clic en el botón
if hist_checkbox:
    # Escribir un mensaje en la aplicación
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Usar nombre especifico para esta figura
    fig_hist = go.Figure(data=[go.Histogram(x=car_data['model_year'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig_hist.update_layout(title_text='Año del modelo')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig_hist, use_container_width=True)


# Lógica a ejecutar cuando se hace clic en el botón
if graph_checkbox:
    # Escribir un mensaje en la aplicación
    st.write('Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')

       # Crear un gráfico de dispersión utilizando plotly.graph_objects
    fig_scatter = go.Figure(data=[
        go.Scatter(
            x=car_data['model_year'],   # Eje X
            y=car_data['price'],        # Eje Y (ejemplo con precio)
            mode='markers'              # 'markers' para dispersión
        )
    ])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig_scatter.update_layout(
        title_text='Relación entre el año del modelo y el precio del coche',
        xaxis_title='Año del modelo',
        yaxis_title='Precio'
    )

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    st.plotly_chart(fig_scatter, use_container_width=True)