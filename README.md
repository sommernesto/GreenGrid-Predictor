# GreenGrid Predictor

**GreenGrid** in this project refers to a custom forecasting model for Spain's renewable energy grid, focusing on solar power generation (solar_mw). This project uses time-series analysis with Prophet to predict energy output, including data preprocessing, model training, and visualization of predictions and components (trends, seasonality).

## Files
- `etl_pipeline.ipynb`: Jupyter notebook with Prophet-based forecasting pipeline.
- `spain_renewables_master_2020_2024.csv`: Dataset of solar power output (2020-2024).
- `plots/forecast_plot.png`: Forecasted solar_mw with historical data.
- `plots/components_plot.png`: Trend and seasonality breakdown.
- `weather_era5_spain_2020_2024.csv`: Optional weather data for analysis (ERA5 reanalysis, 2020-2024).
- `requirements.txt`: Dependencies list (pandas, prophet).
- `optimization_results.csv`: Resource allocation optimized using SciPy based on the forecast.

## Setup
1. Clone the repo: `git clone https://github.com/sommernesto/GreenGrid-Predictor.git`
2. Install dependencies: `pip install pandas prophet`
3. Checkout the default branch: `git checkout develop`
4. Run `etl_pipeline.ipynb` in a Jupyter environment with the dataset uploaded.

## Usage
- Open `etl_pipeline.ipynb` in Jupyter to run the forecasting pipeline.
- View results in `plots/forecast_plot.png` (forecasted solar_mw) and `plots/components_plot.png` (trend/seasonality breakdown).
- Check `optimization_results.csv` for resource allocation optimized using SciPy based on the forecast.
