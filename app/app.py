import streamlit as st

st.set_page_config(
    page_title="Rendimiento Aéreo 2023",
    page_icon="✈️",
    layout="wide"
)

st.title("✈️ Rendimiento Aéreo y Análisis de Retrasos (2023)")
st.subheader("EIN092B - Visualización de Datos | UTFSM")

st.markdown("""
Bienvenido al prototipo analítico e interactivo para el estudio de la puntualidad operacional en vuelos comerciales.

Utiliza el **menú de la izquierda** para navegar a través de las páginas del proyecto:
1. **📌 Contexto y Datos:** Resumen del problema, alcance $X, Y, T$ y métricas de calidad de datos.
2. **📊 Análisis Exploratorio (EDA):** Distribuciones univariadas, estadísticas descriptivas y filtros interactivos.
3. **🔍 Análisis de la Pregunta:** Relación entre factores operacionales/climáticos ($X$) y retrasos ($Y$).
""")

st.info("💡 Consejo de evaluación: Explora los filtros interactivos en la barra lateral para dinámicamente actualizar las visualizaciones.")