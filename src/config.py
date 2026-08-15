"""
Configuración central del proyecto: rutas y constantes compartidas entre notebooks y módulos.

TODO: define aquí, como constantes, cosas como:
  - las rutas a data/raw, data/interim, data/processed, models/ (usa pathlib, no strings sueltos)
  - la zona horaria de referencia del proyecto (decidiste esto en la Fase 2 de la guía, ¿recuerdas?)
  - la ubicación/latitud-longitud de referencia si trabajas con un punto concreto de Cataluña

Pista: importar esto desde los notebooks en vez de repetir rutas hardcodeadas en cada uno te
ahorrará dolores de cabeza el día que reorganices carpetas.
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = PROJECT_ROOT / 'data' / 'raw'

"""
File name constants
"""

PVGIS_DATA_FILENAME = 'pvgis_timeseries_dataset_2005_2023.csv'
COPERNICUS_DATA_FILENAME = 'copernicus_reanalysis-era5-single-levels-timeseries.csv'

# TODO: deriva el resto de rutas (RAW_DATA_DIR, PROCESSED_DATA_DIR, MODELS_DIR, ...) a partir de PROJECT_ROOT
