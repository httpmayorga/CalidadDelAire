import pandas as pd
from typing import Set
import requests

def ej_1_cargar_datos_demograficos() -> pd.DataFrame:
    url_demographics = "https://public.opendatasoft.com/explore/dataset/us-cities-demographics/download/?format=csv&timezone=Europe/Berlin&lang=en&use_labels_for_header=true&csv_separator=%3B"
    demographics_data = pd.read_csv(url_demographics, sep=';')
    return demographics_data

def ej_2_cargar_calidad_aire(ciudades: Set[str]) -> None:
    air_quality_data = []

    for city in ciudades:
        api_url = f'https://api.api-ninjas.com/v1/airquality?city={city}'
        response = requests.get(api_url, headers={'X-Api-Key': '48wt2803rIwftk4D/ArPgA==fPSlk32FrsldSQCK'})  # Reemplaza 'YOUR_API_KEY' con tu clave de API
        if response.status_code == requests.codes.ok:
            air_quality = response.json()
            if 'data' in air_quality:
                concentration = air_quality['data'].get('concentration')
                air_quality_data.append({'City': city, 'AirQualityConcentration': concentration})
            else:
                air_quality_data.append({'City': city, 'AirQualityConcentration': None})
        else:
            air_quality_data.append({'City': city, 'AirQualityConcentration': None})

    air_quality_df = pd.DataFrame(air_quality_data)
    air_quality_df.to_csv('ciudades.csv', index=False)  # Guarda los datos en un archivo CSV