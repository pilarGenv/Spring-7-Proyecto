# Análisis de Vehículos Usados - Dashboard Interactivo

Esta aplicación web interactiva permite explorar un conjunto de datos de anuncios de venta de vehiculos de manera dinámica. Desarrollada con Streamlit, ofrece una interfaz intuitiva para analizar tendencias en el mercado de vehículos usados a través de visualizaciones interactivas.

## Funcionalidades
- Visualización de distribución de años de modelo mediante histogramas interactivos
- Análisis de relación entre año del modelo y precio con gráficos de dispersión
- Controles interactivos con checkboxes para seleccionar diferentes tipos de visualizaciones
- Dashboard responsivo que se adapta al contenedor

## Tecnologías utilizadas
- **Python** - Lenguaje de programación principal
- **Streamlit** - Framework para aplicaciones web
- **Plotly** - Biblioteca para gráficos interactivos
- **Pandas** - Manipulación y análisis de datos

## Despliegue en Render
Esta aplicación está desplegada en Render. Para desplegar tu propia versión:

- Crea una cuenta en render.com y conecta tu cuenta de GitHub

- Crea un nuevo "Web Service" desde tu repositorio de GitHub

- Configura las siguientes opciones:
Build Command: pip install -r requirements.txt
Start Command: streamlit run app.py
