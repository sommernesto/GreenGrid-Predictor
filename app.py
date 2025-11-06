import streamlit as st
import pandas as pd
import plotly.express as px
from prophet import Prophet
import joblib

st.title("Spain Solar Forecast")

@st.cache_data
def load():
    df = pd.read_csv("spain_renewables_master_2020_2024.csv", parse_dates=['datetime'])
    return df.rename(columns={'datetime': 'ds', 'solar_mw': 'y'})

df = load()

@st.cache_resource
def train():
    m = Prophet(yearly_seasonality=True, weekly_seasonality=True, daily_seasonality=True)
    m.fit(df)
    joblib.dump(m, "model.pkl")
    return m

m = train()

days = st.slider("Forecast days", 1, 14, 7)
future = m.make_future_dataframe(periods=days*24, freq='H')
forecast = m.predict(future)

fig = px.line(df, x='ds', y='y', title="Solar MW")
fig.add_scatter(x=forecast['ds'], y=forecast['yhat'], name="Forecast")
fig.add_ribbon(x=forecast['ds'], y1=forecast['yhat_lower'], y2=forecast['yhat_upper'], fillcolor="blue", opacity=0.2)
st.plotly_chart(fig)

st.pyplot(m.plot_components(forecast))
