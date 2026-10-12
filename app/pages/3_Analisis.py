import streamlit as st
import plotly.express as px
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.clean_data import generate_sample_data, clean_flight_data

st.set_page_config(page_title="Análisis de la Pregunta", page_icon="🔍", layout="wide")

st.title("🔍 Análisis Relacional (X vs Y, T) y Hallazgos Clave")

@st.cache_data
def load_data():
    return clean_flight_data(generate_sample_data(8000))

df = load_data()

st.subheader("1. Patrón Temporal (T): Efecto del Bloque Horario sobre el Retraso")

hourly_delay = df.groupby('CRSDepTime')['DepDelay'].mean().reset_index()

fig_line = px.line(
    hourly_delay, x='CRSDepTime', y='DepDelay',
    title="Evolución del Retraso Promedio a lo largo del Día",
    labels={'CRSDepTime': 'Hora Programada de Salida (24h)', 'DepDelay': 'Retraso Promedio (min)'},
    markers=True
)
fig_line.add_vrect(x0=16, x1=20, fillcolor="red", opacity=0.15, line_width=0, annotation_text="Ventana Crítica (16-20h)")
st.plotly_chart(fig_line, use_container_width=True)

st.caption("**Hallazgo Clave 1:** Se observa un incremento sistemático de los retrasos a partir de las 14:00 horas, alcanzando su punto pico en el bloque 16:00-20:00. Esto confirma la hipótesis de la propagación en cadena del retraso operacional a lo largo de la jornada.")

st.divider()

st.subheader("2. Impacto de Variables Meteorológicas Cruzadas (X) en los Retrasos (Y)")

col1, col2 = st.columns(2)

with col1:
    fig_scatter = px.scatter(
        df, x="WindSpeed", y="DepDelay", color="DelaySeverity",
        title="Relación Velocidad del Viento vs Retraso en Salida",
        labels={'WindSpeed': 'Velocidad del Viento (mph)', 'DepDelay': 'Minutos de Retraso'},
        trendline="ols"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
    st.caption("**Hallazgo Clave 2:** Existe una tendencia positiva moderada entre la velocidad del viento y la magnitud del retraso. Vientos superiores a 20 mph incrementan significativamente la probabilidad de retrasos severos (>45m).")

with col2:
    heatmap_data = df.pivot_table(index='Origin', columns='CRSDepTime', values='DepDelay', aggfunc='mean')
    fig_heat = px.imshow(
        heatmap_data,
        title="Mapa de Calor: Congestión de Retraso por Aeropuerto Origen y Hora",
        labels=dict(x="Hora del Día", y="Aeropuerto Origen", color="Retraso Promedio")
    )
    st.plotly_chart(fig_heat, use_container_width=True)
    st.caption("**Hallazgo Clave 3:** Los aeropuertos Hub principales (como ORD y ATL) concentran mayores niveles de retraso acumulado en horas de la tarde en comparación con aeropuertos regionales.")