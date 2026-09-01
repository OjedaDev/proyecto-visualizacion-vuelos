# Rendimiento Aereo: Visualizacion de Retrasos y Eficiencia Operacional en Vuelos Comerciales (2023)

##  Informacion General
* **Asignatura:** EIN092B - Visualizacion de Datos
* **Institucion:** Universidad Tecnica Federico Santa Maria
* **Integrantes:**
  * [Joaquin Ojeda] 
  * [Benjamin Garcia] 
  * [Matias Pinto] 
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

---

## 📁 Estructura del Repositorio
```text
proyecto-visualizacion/
├── data/
│   ├── raw/            # Datos originales sin modificar
│   └── processed/      # Datos limpios y procesados
├── notebooks/
│   └── 01_exploracion.ipynb  # Análisis exploratorio inicial
├── src/                # Scripts auxiliares y módulos reutilizables
├── figures/            # Gráficos generados para presentaciones
├── app/                # Prototipo y aplicación interactiva
├── .gitignore          # Archivos excluidos de Git
└── README.md           # Documentación principal del proyecto
