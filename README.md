# Spain Solar Power Forecast

This project forecasts solar power generation (solar_mw) in Spain using time-series analysis with Prophet. It includes data preprocessing, model training, and visualization of predictions and components (trends, seasonality).

## Files
- `etl_pipeline.ipynb`: Jupyter notebook with Prophet-based forecasting pipeline.
- `spain_renewables_master_2020_2024.csv`: Dataset of solar power output (2020-2024).
- `plots/forecast_plot.png`: Forecasted solar_mw with historical data.
- `plots/components_plot.png`: Trend and seasonality breakdown.

## Setup
1. Clone the repo: `git clone https://github.com/sommernesto/GreenGrid-Predictor.git`
2. Install dependencies: `pip install pandas prophet`
3. Run `etl_pipeline.ipynb` in a Jupyter environment with the dataset uploaded.
