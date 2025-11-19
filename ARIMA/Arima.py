# ARIMA Practical Implementation
# Course: CS531 - Data Science, Yuan Ze University

# ==============================
# 1. Setup and Data Loading
# ==============================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error

import warnings
warnings.filterwarnings("ignore")

# Load the airline passengers dataset
data = pd.read_csv(
    'https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv',
    index_col='Month',
    parse_dates=True
)
data.index.freq = 'MS'  # Month Start frequency

series = data['Passengers']

print("--- Initial Data Snapshot ---")
print(series.head())
print(f"\nTotal Data Points: {len(series)}")

# ==============================
# 2. Stationarity Check (ADF)
# ==============================
def adf_test(series):
    result = adfuller(series.dropna())
    print('\n--- Augmented Dickey-Fuller Test Results ---')
    labels = ['ADF Statistic','p-value','#Lags Used','Number of Observations Used']
    for value, label in zip(result[:4], labels):
        print(f'{label}: {value:.4f}')

    if result[1] <= 0.05:
        print("\nConclusion: Reject H0 (Unit Root). Series is likely Stationary.")
    else:
        print("\nConclusion: Fail to Reject H0. Series is Non-Stationary.")

print("\n" + "="*50)
print("STEP 1: CHECK INITIAL STATIONARITY (ADF)")
adf_test(series)

# ==============================
# 3. Log Transform + Differencing
# ==============================
series_log = np.log(series)
series_log_diff = series_log.diff().dropna()

print("\n" + "="*50)
print("STEP 2: APPLY LOG + DIFFERENCING (d=1) AND CHECK NEW STATIONARITY")
adf_test(series_log_diff)

plt.figure(figsize=(12, 4))
series_log_diff.plot(title='Log-Transformed and First-Differenced Series')
plt.show()

# ==============================
# 4. ACF / PACF (Identify p, q)
# ==============================
print("\n" + "="*50)
print("STEP 3: ACF/PACF TO IDENTIFY p AND q ORDERS")

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

plot_acf(series_log_diff, lags=9, ax=axes[0])
axes[0].set_title('ACF of Differenced Series')

plot_pacf(series_log_diff, lags=9, ax=axes[1])
axes[1].set_title('PACF of Differenced Series')

plt.tight_layout()
plt.show()

# (For this demo we still choose ARIMA(1,1,1), acknowledging that SARIMA is
#  more appropriate for such strongly seasonal data.)

# ==============================
# 5. Model Fitting (ARIMA(1,1,1))
# ==============================
train_size = int(len(series_log) * 0.9)
train, test = series_log.iloc[:train_size], series_log.iloc[train_size:]

print("\n" + "="*50)
print(f"STEP 4: FIT ARIMA(1, 1, 1) MODEL (Train Size: {len(train)})")

model = ARIMA(train, order=(1, 1, 1))
model_fit = model.fit()

print(model_fit.summary())

# ==============================
# 6. Forecasting and Visualization
# ==============================
print("\n" + "="*50)
print("STEP 5: FORECASTING AND VISUALIZATION")

# Forecast on the test index
predictions_log = model_fit.predict(start=test.index[0], end=test.index[-1])

# Back-transform from log scale
predictions = np.exp(predictions_log)
actual = np.exp(test)

rmse = np.sqrt(mean_squared_error(actual, predictions))
print(f'\nRoot Mean Squared Error (RMSE): {rmse:.2f}')

plt.figure(figsize=(12, 6))
series.plot(label='Original Data')
actual.plot(label='Actual Test Data', color='red')
predictions.plot(label='ARIMA(1,1,1) Forecast', color='green', linestyle='--')
plt.title('ARIMA(1, 1, 1) Forecast vs. Actual (Airline Passengers)')
plt.legend()
plt.grid(True)
plt.show()

# ==============================
# 7. Residual Diagnostics + Next 12 Months
# ==============================
print("\n" + "="*50)
print("STEP 6: MODEL DIAGNOSTICS - RESIDUAL ANALYSIS")

residuals = model_fit.resid

plt.figure(figsize=(8, 4))
residuals.plot(kind='kde', title='Residual Density')
plt.show()

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
plot_acf(residuals.dropna(), lags=20, ax=axes[0])
axes[0].set_title('ACF of Residuals')
plot_pacf(residuals.dropna(), lags=20, ax=axes[1])
axes[1].set_title('PACF of Residuals')
plt.tight_layout()
plt.show()

# Next 12 months forecast on original scale
forecast_log = model_fit.get_forecast(steps=12).summary_frame()

forecast = pd.DataFrame({
    'mean': np.exp(forecast_log['mean']),
    'lower 95%': np.exp(forecast_log['mean_ci_lower']),
    'upper 95%': np.exp(forecast_log['mean_ci_upper'])
})

print("\n--- Next 12 Months Forecast (Original Scale) ---")
print(forecast)
