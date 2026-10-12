import pandas as pd
import numpy as np

def generate_sample_data(n_samples=10000):
    """Genera un dataset sintético con las variables reales de la BTS y clima para desarrollo."""
    np.random.seed(42)
    dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="h")
    
    carriers = ['Delta (DL)', 'American (AA)', 'United (UA)', 'Southwest (WN)', 'Alaska (AS)']
    airports = ['ATL', 'ORD', 'DFW', 'DEN', 'LAX', 'JFK', 'MIA', 'SFO']
    
    data = {
        'FlightDate': np.random.choice(dates, n_samples),
        'Carrier': np.random.choice(carriers, n_samples, p=[0.25, 0.25, 0.20, 0.20, 0.10]),
        'Flight_Number': np.random.randint(100, 9000, n_samples),
        'Origin': np.random.choice(airports, n_samples),
        'Dest': np.random.choice(airports, n_samples),
        'Distance': np.random.randint(200, 2800, n_samples),
        'CRSDepTime': np.random.randint(5, 23, n_samples), # Hora programada
        'WindSpeed': np.random.gamma(shape=2, scale=5, size=n_samples), # mph
        'Visibility': np.random.uniform(1.0, 10.0, n_samples), # millas
        'Precipitation': np.random.exponential(scale=0.1, size=n_samples) # pulgadas
    }
    
    df = pd.DataFrame(data)
    # Evitar origen == destino
    df = df[df['Origin'] != df['Dest']].copy()
    
    # Simular retraso (Y) en función de la hora, el clima y ruido
    base_delay = (df['CRSDepTime'] - 5) * 1.5 + (df['WindSpeed'] * 1.2) - (df['Visibility'] * 2)
    noise = np.random.normal(0, 15, len(df))
    raw_delay = base_delay + noise
    
    df['DepDelay'] = np.where(raw_delay < -10, -5, np.round(raw_delay, 1))
    
    # Categoría de severidad (Y cualitativo)
    conditions = [
        (df['DepDelay'] < 15),
        (df['DepDelay'] >= 15) & (df['DepDelay'] <= 45),
        (df['DepDelay'] > 45)
    ]
    choices = ['A tiempo / Menor (<15m)', 'Moderado (15-45m)', 'Severo (>45m)']
    df['DelaySeverity'] = np.select(conditions, choices, default='A tiempo / Menor (<15m)')
    
    # Rango de distancia
    df['DistanceGroup'] = pd.cut(df['Distance'], bins=[0, 500, 1500, 5000], labels=['Corta (<500 mi)', 'Media (500-1500 mi)', 'Larga (>1500 mi)'])
    
    return df

def clean_flight_data(df):
    """Limpia y valida tipos de datos."""
    df['FlightDate'] = pd.to_datetime(df['FlightDate'])
    df['Month'] = df['FlightDate'].dt.month_name()
    df['DayOfWeek'] = df['FlightDate'].dt.day_name()
    return df