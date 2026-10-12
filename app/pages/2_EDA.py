import streamlit as st
import plotly.express as px
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.clean_data import generate_sample_data, clean_flight_data

st.set_page_config(page_title="EDA Univariado", page_icon="📊", layout="wide")

st.title("📊 Análisis Exploratorio de Datos (EDA)")

@st.cache_data
def load_data():
    return clean_flight_data(generate_sample_data(8000))

df = load_data()

# Filtros Interactivos en Sidebar
st.sidebar.header("🎛️ Filtros Interactivos")
selected_carrier = st.sidebar.multiselect("Seleccionar Aerolínea:", options=df['Carrier'].unique(), default=df['Carrier'].unique())
selected_severity = st.sidebar.multiselect("Severidad del Retraso:", options=df['DelaySeverity'].unique(), default=df['DelaySeverity'].unique())

df_filtered = df[(df['Carrier'].isin(selected_carrier)) & (df['DelaySeverity'].isin(selected_severity))]

st.subheader("1. Distribución de la Variable Objetivo (Y: Retraso en Salida)")

col1, col2 = st.columns(2)

with col1:
    fig_hist = px.histogram(
        df_filtered, x="DepDelay", nbins=50, 
        title="Distribución de Minutos de Retraso (Histograma)",
        labels={'DepDelay': 'Minutos de Retraso'},
        color_discrete_sequence=['#0B2554']
    )
    st.plotly_chart(fig_hist, use_container_width=True)
    st.caption("**Interpretación:** Existe una clara asimetría positiva. La mayoría de los vuelos salen a tiempo o con demoras menores, pero existe una cola larga de eventos extremos.")

with col2:
    fig_box = px.box(
        df_filtered, x="Carrier", y="DepDelay", color="Carrier",
        title="Dispersión y Outliers de Retraso por Aerolínea",
        labels={'DepDelay': 'Minutos de Retraso', 'Carrier': 'Aerolínea'}
    )
    st.plotly_chart(fig_box, use_container_width=True)
    st.caption("**Interpretación:** Los gráficos de caja permiten observar que la variabilidad de retrasos difiere entre aerolíneas, identificando competidores con mayor consistencia operativa.")

st.divider()

st.subheader("2. Frecuencia de Categorías y Rangos Operacionales")

col3, col4 = st.columns(2)

with col3:
    severity_counts = df_filtered['DelaySeverity'].value_counts().reset_index()
    fig_pie = px.pie(
        severity_counts, values='count', names='DelaySeverity',
        title="Proporción por Severidad del Retraso",
        color_discrete_sequence=px.colors.sequential.RdBu
    )
    st.plotly_chart(fig_pie, use_container_width=True)

with col4:
    dist_counts = df_filtered['DistanceGroup'].value_counts().reset_index()
    fig_bar = px.bar(
        dist_counts, x='DistanceGroup', y='count',
        title="Volumen de Vuelos por Rango de Distancia",
        labels={'DistanceGroup': 'Rango de Distancia', 'count': 'Número de Vuelos'},
        color_discrete_sequence=['#2EA8F2']
    )
    st.plotly_chart(fig_bar, use_container_width=True)