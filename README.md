# ☀️ Photovoltaic Energy Forecast

> 🚧 **Work in progress** — this project is under active development. The data pipeline and exploratory analysis are done; feature engineering is underway and modelling comes next.

Hourly forecasting of solar irradiance and photovoltaic (PV) production for a location in Barcelona, built with historical irradiance and weather data and machine learning.

---

## 🎯 Goals

- **Forecast solar production hour by hour**, starting with a **48-hour horizon** (prototype) and later extending it to **7 days** using numerical weather prediction (NWP) inputs.
- **Model the Clear Sky Index** instead of raw power output. Dividing by the theoretical clear-sky value removes the strong daily and yearly seasonality driven by the sun's position, keeps the target in a bounded range and makes the model easier to reuse if the installed capacity changes.
- **Hourly granularity**, aligned with the hourly scheduling of the Spanish wholesale electricity market.
- **Learn end to end**: from raw data collection to a trained model and, eventually, a small dashboard to visualise forecasts.

## 📊 Data

| Source | What it provides |
|---|---|
| [PVGIS](https://joint-research-centre.ec.europa.eu/photovoltaic-geographical-information-system-pvgis_en) (EU JRC) | Hourly irradiance, PV power output, sun height and temperature |
| [Copernicus ERA5](https://cds.climate.copernicus.eu/) (reanalysis) | Hourly cloud cover and surface solar radiation |

- **Location:** Barcelona (41.383° N, 2.180° E)
- **Period:** 2006 – 2023 (the range both datasets share)
- **Timezone:** converted from UTC to Europe/Madrid (CET/CEST)

Raw data files are not included in the repository (see `data/`).

## 🔄 Process

| Step | Notebook | Status |
|---|---|---|
| 1. Data collection & understanding | `01_data_collection_and_understanding.ipynb` | ✅ Done |
| 2. Data cleaning & merging | `02_data_cleaning.ipynb` | ✅ Done |
| 3. Exploratory data analysis | `03_eda.ipynb` | ✅ Done |
| 4. Feature engineering | `04_feature_engineering.ipynb` | 🚧 In progress |
| 5. Modelling (baselines → ML models) | — | ⏳ Planned |
| 6. Evaluation | — | ⏳ Planned |
| 7. Dashboard | — | ⏳ Planned |

### Highlights so far

- Both datasets are complete: no missing rows, duplicated timestamps or gaps in the hourly series.
- Clean-up included dropping empty or redundant columns, clipping physically impossible negative radiation values and converting units (J/m² → W/m²).
- The EDA shows that most of the 24-hour predictability of irradiance comes from **astronomy (the sun's position)** rather than the weather, while cloud cover carries genuine "weather memory".
- The cloud–irradiance correlation changes with the season: it is weakest in summer (≈ -0.19) and strongest in winter (≈ -0.48).
- Feature engineering has started with solar position features computed with `pvlib`.

## 🗂️ Project structure

```
solar-energy-forecast/
├── data/            # raw, interim, processed and external data (not versioned)
├── notebooks/       # step-by-step analysis notebooks
├── src/
│   ├── data/        # ingestion, validation and preprocessing
│   ├── features/    # feature engineering
│   ├── models/      # model training (coming soon)
│   └── visualization/
├── models/          # trained models (coming soon)
├── reports/figures/ # generated plots
└── dashboard/       # forecast dashboard (coming soon)
```

## 🛠️ Tech stack

`Python` · `pandas` · `NumPy` · `pvlib` · `statsmodels` · `SciPy` · `Matplotlib` · `Jupyter`

## ⚙️ Setup

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS / Linux
pip install -r requirements.txt
```

---

*Made by [Isa](https://github.com/codingisads) as a personal project to grow into data science and energy forecasting.*
