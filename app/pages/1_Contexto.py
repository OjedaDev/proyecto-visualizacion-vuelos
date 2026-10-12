import streamlit as st
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.clean_data import generate_sample_data, clean_flight_data

st.set_page_config(page_title="Contexto y Datos", page_icon="📌", layout="wide")

st.title("📌 Contexto del Proyecto y Calidad de Datos")

st.markdown("""
### Contexto del Proyecto
La red de transporte aéreo comercial opera como una infraestructura hiperconectada que absorbe miles de operaciones diarias bajo ventanas de tiempo sumamente ajustadas. Gran parte de esta oferta se concentra en aeropuertos de conexión masiva (*hubs*) y franjas de alta rotación de aeronaves, donde contingencias operacionales o meteorológicas desencadenan un efecto dominó sobre los itinerarios.
""")

col1, col2 = st.columns(2)

with col1:
    st.info("""
    **Pregunta Principal:**  
    ¿Cómo influyen las características del vuelo, la congestión del aeropuerto y el clima en la magnitud y severidad de los retrasos operacionales durante 2023?
    """)

with col2:
    st.success("""
    **Estructura X, Y, T:**
    * **(X) Variables:** Aerolínea, Origen, Destino, Nº Vuelo, Distancia, Hora, Viento, Visibilidad.
    * **(Y) Objetivo Dual:** Regresión (Minutos de retraso) y Clasificación (Severidad <15m, 15-45m, >45m).
    * **(T) Tiempo:** Año 2023 (resolución horaria, diaria y mensual).
    """)

st.divider()

st.subheader("📊 Muestra de Datos y Resumen de Calidad")

@st.cache_data
def load_data():
    raw = generate_sample_data(8000)
    return clean_flight_data(raw)

df = load_data()

m1, m2, m3, m4 = st.columns(4)
m1.metric("Total Registros", f"{len(df):,}")
m2.metric("Variables Totales", f"{df.shape[1]}")
m3.metric("Aerolíneas Evaluadas", f"{df['Carrier'].nunique()}")
m4.metric("Promedio Retraso Salida", f"{df['DepDelay'].mean():.1f} min")

st.markdown("#### Vista previa del Dataset Processed")
st.dataframe(df.head(10), use_container_width=True)

st.markdown("""
**Calidad y Limpieza de Datos:**
* **Valores Faltantes:** Se trataron registros con timestamps nulos imputando mediana por bloque horario.
* **Inconsistencias:** Se filtraron vuelos con origen igual a destino y distancias negativas/nulas.
* **Outliers:** Se mantuvieron los retrasos extremos (>180 min) pero se analizaron mediante métricas robustas (mediana y percentiles) para evitar sesgos.
""")