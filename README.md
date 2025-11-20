# GreenGrid-Predictor: Hourly Solar Power Forecasting for Spain

![Python](https://img.shields.io/badge/python-3.10-blue) 
![XGBoost](https://img.shields.io/badge/XGBoost-2.1-orange) 
![Pandas](https://img.shields.io/badge/pandas-2.2-green) 
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

**Data Science / ML Engineering portfolio project**  
**XGBoost + real weather data → 22.1% better than baseline**

## Problem
Spain added >30 GW of solar in 5 years. Grid operators need accurate hourly forecasts to integrate renewables and avoid blackouts.

Predicts `solar_mw` using 2020–2024 hourly data (~44k rows).

## Key Results (2024 Test Set)

| Model                        | MAE (MW) | RMSE (MW) | Improvement          |
|------------------------------|----------|-----------|----------------------|
| Persistence Baseline         | 921.7    | 1749.0    | -                    |
| **XGBoost + Weather (final)**| **718.4**| **1192.1**| **22.1% better** |

## Visual Proof

### Full Time Series (2020–2024)
![Full Solar Time Series](https://github.com/sommernesto/GreenGrid-Predictor/raw/develop/plots/01_full_timeseries.png)

### 7-Day Forecast vs Actual (Dec 2024) – with Temperature & Cloud Cover
![XGBoost 7-Day Forecast](https://github.com/sommernesto/GreenGrid-Predictor/raw/develop/plots/02_xgboost_forecast_7days.png)

## How It Works
1. **Data**: `spain_renewables_master_2020_2024.csv` → cleaned to `solar_mw` + timestamp
2. **Weather**: Hourly temperature & cloud cover from Open-Meteo API (Madrid proxy)
3. **Features**:
   - `hour`, `day_of_week`, `month`
   - `lag_24`, `lag_48`, `rolling_mean_24`
   - `temperature_2m`, `cloud_cover`
4. **Model**: XGBoost Regressor (500 trees, depth 6)
5. **Split**: Train 2020–2023 | Test 2024

## Run in Google Colab (1-Click)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sommernesto/GreenGrid-Predictor/blob/develop/notebooks/GreenGridFinalAnalysis.ipynb)

Upload your CSV → Run all → Get plots & results in <2 minutes

## Local Setup
```bash
git clone https://github.com/sommernesto/GreenGrid-Predictor.git
cd GreenGrid-Predictor
pip install -r requirements.txt
jupyter notebook notebooks/GreenGridFinalAnalysis.ipynb
