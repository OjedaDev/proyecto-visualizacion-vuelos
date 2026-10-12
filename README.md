# Rendimiento Aereo: Visualizacion de Retrasos y Eficiencia Operacional en Vuelos Comerciales (2023)

##  Informacion General
* **Asignatura:** EIN092B - Visualizacion de Datos
* **Institucion:** Universidad Tecnica Federico Santa Maria
* **Integrantes:**
  * Joaquin Ojeda 
  * Benjamin Garcia
  * Matias Pinto 
---

##  Problema y Motivacion
La aviacion comercial opera bajo ventanas de tiempo sumamente ajustadas. Los retrasos en salida y llegada no solo generan perdidas millonarias, sino que provocan un efecto domino sobre toda la red aerea. Este proyecto busca transformar registros masivos de vuelos en visualizaciones analiticas que permitan identificar cuellos de botella y factores criticos de impuntualidad en rutas clave.

---

##  Pregunta de Investigacion y Estructura X, Y, T
**Pregunta principal:**  
*Como influyen las caracteristicas del vuelo, la congestion del aeropuerto y el horario programado en los minutos de retraso y causas de impuntualidad en rutas comerciales?*

* **(X) Variables explicativas:** Aerolinea operadora, aeropuertos de origen y destino, distancia de ruta y bloque horario programado.
* **(Y) Fenomeno objetivo:** Minutos de retraso (salida/llegada) y causas de demora (operacional, clima, congestion NAS).
* **(T) Contexto temporal:** Registro historico continuo consolidado durante el año 2023.

---

## 📊 Dataset y Fuente
* **Fuente:** *Bureau of Transportation Statistics (BTS) / U.S. Department of Transportation* (Airline On-Time Performance Data).
* **Unidad de observación:** Un vuelo comercial individual programado y operado.
* **Instrucciones para obtener los datos:**
  1. Descargar el archivo `.csv` desde el portal oficial de la BTS o repositorio complementario.
  2. Guardar el archivo en la ruta local `data/raw/flights_2023.csv`.


## 🚀 Instrucciones para Ejecutar la Aplicación Streamlit

###  Clonar el repositorio

1. git clone [https://github.com/OjedaDev/proyecto-visualizacion-vuelos.git](https://github.com/OjedaDev/proyecto-visualizacion-vuelos.git)
cd proyecto-visualizacion-vuelos
2. Instalar dependencias
pip install -r requirements.txt
3. Iniciar la aplicación interactiva
python -m streamlit run app/app.py
---




## 📁 Estructura del Repositorio
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