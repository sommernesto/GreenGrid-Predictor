# GreenGrid Predictor – Spain Solar Forecast

Predicts solar power output for Spain's grid using Prophet and SciPy optimization.  
Includes interactive dashboard and REST API, all open source and free to run.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1CZ8oRm08vO8jGgn2fvFJd_Zs6J8Fb8qK#scrollTo=3a096ad2)
[![Streamlit App](https://img.shields.io/badge/Live_Demo-FF4B4B?logo=streamlit)](https://colab.research.google.com/drive/1CZ8oRm08vO8jGgn2fvFJd_Zs6J8Fb8qK#scrollTo=3a096ad2)
[![Python](https://img.shields.io/badge/Python-3.11-blue)](requirements.txt)
[![License](https://img.shields.io/github/license/sommernesto/GreenGrid-Predictor)](LICENSE)

## Live Demo
[Interactive Forecast in Google Colab](https://colab.research.google.com/drive/1CZ8oRm08vO8jGgn2fvFJd_Zs6J8Fb8qK#scrollTo=3a096ad2)  
(Run the full pipeline instantly — Streamlit dashboard coming soon)

![demo](assets/demo.gif)

## What It Does
Predicts hourly solar output (solar_mw) using 2020–2024 data  
Models trend and seasonality with Prophet  
Optimizes resource allocation using SciPy  
Exports forecasts with confidence intervals  
Supports optional ERA5 weather data

## Tech Stack
| Layer | Tool |
|-------|------|
| Forecasting | Prophet |
| Optimization | SciPy |
| Visualization | Plotly, Matplotlib |
| Data | Pandas, CSV |

## Quick Start

```bash
git clone https://github.com/sommernesto/GreenGrid-Predictor.git
cd GreenGrid-Predictor
pip install -r requirements.txt
jupyter notebook etl_pipeline.ipynb
