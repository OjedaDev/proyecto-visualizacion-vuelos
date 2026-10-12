# Rendimiento Aéreo: Visualización de Retrasos y Eficiencia Operacional en Vuelos Comerciales (2023) ✈️

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red.svg)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-5.17%2B-orange.svg)](https://plotly.com/)

## 📌 Información General
* **Asignatura:** EIN092B - Visualización de Datos
* **Institución:** Universidad Técnica Federico Santa María
* **Profesor:** Jesús A. Parra
* **Semestre:** 2026-II
* **Integrantes:**
  * Joaquín Ojeda
  * Benjamín García
  * Matías Pinto

---

## 🎯 Problema y Motivación
La aviación comercial opera bajo ventanas de tiempo altamente sincronizadas. Los retrasos en salida y llegada no solo generan pérdidas millonarias, sino que provocan un efecto dominó sobre toda la red aérea. Este proyecto busca transformar registros masivos de vuelos en una **aplicación analítica e interactiva desarrollada en Streamlit**, permitiendo identificar cuellos de botella, factores críticos de impuntualidad y el impacto de condiciones meteorológicas en rutas clave.

---

## ❓ Pregunta de Investigación y Estructura X, Y, T

### Pregunta Principal:
> *¿Cómo influyen las características del vuelo, la congestión del aeropuerto de origen y las condiciones meteorológicas cruzadas en los minutos de retraso, causas de impuntualidad y severidad del retraso en rutas comerciales durante el año 2023?*

### Estructura X, Y, T:
* **(X) Variables Explicativas:** Aerolínea operadora, aeropuerto de origen y destino, número de vuelo (`Flight_Number`), distancia de ruta (`Distance`), bloque horario programado (`CRSDepTime`) y variables meteorológicas cruzadas (`WindSpeed`, `Visibility`, `Precipitation`).
* **(Y) Fenómeno Objetivo Dual:** 
  * *Cuantitativo Continuo (Regresión):* Minutos de retraso en salida (`DepDelay`) y llegada (`ArrDelay`).
  * *Cualitativo Categorizado (Clasificación):* Severidad del retraso (`A tiempo / Menor <15m`, `Moderado 15-45m`, `Severo >45m`).
* **(T) Contexto Temporal:** Registro histórico continuo consolidado durante el año 2023 (analizado a nivel horario, diario, mensual y estacional).

---

## 📊 Dataset y Calidad de Datos
* **Fuente Primaria:** *Bureau of Transportation Statistics (BTS) / U.S. Department of Transportation* (*Airline On-Time Performance Data*).
* **Fuentes Secundarias:** Enriquecimiento con datos meteorológicos de estaciones aeroportuarias (*NOAA / Open-Meteo*).
* **Unidad de Observación:** Un vuelo comercial individual programado y operado.
* **Tratamiento de Calidad:**
  * Imputación de nulos en marcas de tiempo mediante la mediana del bloque horario.
  * Eliminación de registros inconsistentes (vuelos con origen igual a destino o distancias nulas).
  * Análisis mediante métricas robustas (mediana y percentiles) para evitar el sesgo causado por outliers de retraso extremo (>180 min).

---

## 🚀 Instrucciones para Ejecutar la Aplicación Streamlit

### 1. Clonar el repositorio
```bash
git clone [https://github.com/OjedaDev/proyecto-visualizacion-vuelos.git](https://github.com/OjedaDev/proyecto-visualizacion-vuelos.git)
cd proyecto-visualizacion-vuelos

git push origin main --force

python -m streamlit run app/app.py  

proyecto-visualizacion-vuelos/
├── data/
│   ├── raw/            # Datos originales de la BTS y clima (excluidos en .gitignore)
│   └── processed/      # Datasets limpios y transformados
├── notebooks/
│   ├── 01_exploracion.ipynb  # Carga inicial y exploración
│   └── 02_eda.ipynb          # Análisis exploratorio profundo
├── src/
│   └── clean_data.py   # Módulo de limpieza y generación de variables
├── app/
│   ├── app.py          # Punto de entrada principal de Streamlit
│   └── pages/
│       ├── 1_Contexto.py  # Página 1: Contexto, métricas y datos
│       ├── 2_EDA.py       # Página 2: EDA univariado y filtros
│       └── 3_Analisis.py  # Página 3: Relaciones X vs Y y hallazgos
├── .gitignore          # Exclusión de archivos pesados y cachés
├── requirements.txt    # Librerías y dependencias
└── README.md           # Documentación principal del proyecto