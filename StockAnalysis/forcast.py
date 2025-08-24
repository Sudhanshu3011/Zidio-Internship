# import streamlit as st
# import pandas as pd

# # Load forecast results
# forecast_arima = pd.read_csv('forecast_arima.csv', parse_dates=True, index_col=0)
# forecast_sarima = pd.read_csv('forecast_sarima.csv', parse_dates=True, index_col=0)
# forecast_prophet = pd.read_csv('forecast_prophet.csv', parse_dates=True)
# lstm_forecast = pd.read_csv('lstm_forecast.csv', parse_dates=True, index_col=0)

# # Load metrics
# metrics_arima = pd.read_csv('metrics_arima.csv')
# metrics_sarima = pd.read_csv('metrics_sarima.csv')
# metrics_prophet = pd.read_csv('metrics_prophet.csv')
# metrics_lstm = pd.read_csv('metrics_lstm.csv')


# # ARIMA Section
# st.subheader("ARIMA Forecast")
# st.line_chart(forecast_arima)
# st.markdown("**Accuracy Metrics:**")
# st.dataframe(metrics_arima)

# # SARIMA Section
# st.subheader("SARIMA Forecast")
# st.line_chart(forecast_sarima)
# st.markdown("**Accuracy Metrics:**")
# st.dataframe(metrics_sarima)


# # Prophet Section
# st.subheader("Prophet Forecast")
# st.line_chart(forecast_prophet[['ds', 'yhat']].set_index('ds').tail(30))
# st.markdown("**Accuracy Metrics:**")
# st.dataframe(metrics_prophet)

# # LSTM Section
# st.subheader("LSTM Forecast")
# st.line_chart(lstm_forecast)
# st.markdown("**Accuracy Metrics:**")
# st.dataframe(metrics_lstm)

# # Footer
# st.success("✅ All forecasts and metrics loaded successfully!")

import streamlit as st
import pandas as pd

# Load SARIMA forecast CSV
forecast_sarima = pd.read_csv('forecast_sarima.csv')
metrics_sarima = pd.read_csv('metrics_sarima.csv')

# Check and rename the column if needed
if 'predicted_mean' in forecast_sarima.columns:
    forecast_sarima.rename(columns={'predicted_mean': 'Forecast'}, inplace=True)
else:
    st.error("❌ 'predicted_mean' column not found in SARIMA CSV.")

# Create a numeric index (for plotting)
forecast_sarima.index = range(1, len(forecast_sarima) + 1)

# Display in Streamlit
st.subheader("SARIMA Forecast")
st.line_chart(forecast_sarima['Forecast'])

# Show metrics (assuming you have them)
st.markdown("**Accuracy Metrics:**")
st.dataframe(metrics_sarima)