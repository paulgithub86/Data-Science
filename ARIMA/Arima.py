# ARIMA Practical Implementation
# Course: CS531 - Data Science, Yuan Ze University

# 1. Setup and Data Loading
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller, acf, pacf
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error

# Ignore harmless warnings
import warnings
warnings.filterwarnings("ignore")

# Load a classic non-stationary time series dataset
# This dataset is built into statsmodels
data = pd.read_csv('https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv',
                   index_col='Month', parse_dates=True)
data.index.freq = 'MS' # Set frequency to Month Start

# Rename column and take a look
series = data['Passengers']
print("--- Initial Data Snapshot ---")
print(series.head())
print(f"\nTotal Data Points: {len(series)}")

# ----------------------------------------------------
# 2. Stationarity Check (ADF Test)
# ----------------------------------------------------
def adf_test(series):
    result = adfuller(series.dropna())
    print('\n--- Augmented Dickey-Fuller Test Results ---')
    labels = ['ADF Statistic','p-value','#Lags Used','Number of Observations Used']
    for value,label in zip(result,labels):
        print(f'{label}: {value:.4f}')

    if result[1] <= 0.05:
        print("\nConclusion: Reject H0 (Unit Root). Series is likely Stationary.")
    else:
        print("\nConclusion: Fail to Reject H0. Series is Non-Stationary.")

print("\n" + "="*50)
print("STEP 1: CHECK INITIAL STATIONARITY (ADF)")
adf_test(series)

# ----------------------------------------------------
# 3. Differencing to Achieve Stationarity (d=1)
# ----------------------------------------------------
# A common issue is increasing variance, so we apply log transformation first
series_log = np.log(series)
series_log_diff = series_log.diff().dropna()

print("\n" + "="*50)
print("STEP 2: APPLY DIFFERENCING (d=1) AND CHECK NEW STATIONARITY")
adf_test(series_log_diff)

# Plot the differenced series
plt.figure(figsize=(12,4))
series_log_diff.plot(title='Log-Transformed and First-Differenced Series')
plt.show()

# ----------------------------------------------------
# 4. Identification of AR (p) and MA (q) orders
# ----------------------------------------------------
# Note: For this highly seasonal data, SARIMA is better, but we'll use ARIMA(p,d,q) for teaching
# We look at the ACF/PACF of the *differenced* series.

print("\n" + "="*50)
print("STEP 3: ACF/PACF TO IDENTIFY p AND q ORDERS")

# ACF Plot
plt.figure(figsize=(10, 4))
plot_acf = plt.subplot(121)
plot_acf.set_title('ACF of Differenced Series')
plt.bar(range(10), acf(series_log_diff, nlags=9, alpha=0.05)[0][1:10], width=0.8)
plt.axhline(y=0, color='gray', linestyle='-')
plt.axhspan(acf(series_log_diff, nlags=9, alpha=0.05)[1][1:10][0][0], acf(series_log_diff, nlags=9, alpha=0.05)[1][1:10][0][1], alpha=0.2, color='blue') # Confidence Interval visualization

# PACF Plot
plot_pacf = plt.subplot(122)
plot_pacf.set_title('PACF of Differenced Series')
plt.bar(range(10), pacf(series_log_diff, nlags=9, alpha=0.05)[0][1:10], width=0.8)
plt.axhline(y=0, color='gray', linestyle='-')
plt.axhspan(pacf(series_log_diff, nlags=9, alpha=0.05)[1][1:10][0][0], pacf(series_log_diff, nlags=9, alpha=0.05)[1][1:10][0][1], alpha=0.2, color='blue') # Confidence Interval visualization
plt.tight_layout()
plt.show()

# Based on a typical interpretation of this data (ignoring strong seasonality for ARIMA)
# we might tentatively select p=1 and q=1.

# ----------------------------------------------------
# 5. Model Fitting (ARIMA(1, 1, 1))
# ----------------------------------------------------
# Split data into train/test (90% train, 10% test)
train_size = int(len(series_log) * 0.9)
train, test = series_log[:train_size], series_log[train_size:]

print("\n" + "="*50)
print(f"STEP 4: FIT ARIMA(1, 1, 1) MODEL (Train Size: {len(train)})")

# Fit the ARIMA model: p=1, d=1 (from differencing), q=1
model = ARIMA(train, order=(1, 1, 1))
model_fit = model.fit()

print(model_fit.summary())

# ----------------------------------------------------
# 6. Forecasting and Visualization
# ----------------------------------------------------
print("\n" + "="*50)
print("STEP 5: FORECASTING AND VISUALIZATION")

# Get start and end dates for prediction
start = len(train)
end = len(train) + len(test) - 1

# Forecast on the test set
predictions_log = model_fit.predict(start=start, end=end, dynamic=False)

# Convert predictions back to original scale (inverse log)
predictions = np.exp(predictions_log)
actual = np.exp(test)

# Calculate RMSE (Root Mean Squared Error) on the original scale
rmse = np.sqrt(mean_squared_error(actual, predictions))
print(f'\nRoot Mean Squared Error (RMSE): {rmse:.2f}')

# Plot the results
plt.figure(figsize=(12, 6))
series.plot(label='Original Data')
actual.plot(label='Actual Test Data', color='red')
predictions.plot(label='ARIMA(1,1,1) Forecast', color='green', linestyle='--')
plt.title('ARIMA(1, 1, 1) Forecast vs. Actual (Airline Passengers)')
plt.legend()
plt.grid(True)
plt.show()

# ----------------------------------------------------
# 7. Model Diagnostics (Residuals Check)
# ----------------------------------------------------
print("\n" + "="*50)
print("STEP 6: MODEL DIAGNOSTICS - RESIDUAL ANALYSIS")

# Plot the residuals
residuals = model_fit.resid
residuals.plot(kind='kde', title='Residual Density')
plt.show()

# Residuals should be close to a normal distribution centered at zero.
# An ACF/PACF plot of the residuals should show no significant spikes (i.e., White Noise).

# For a quick final forecast (e.g., next 12 periods)
final_forecast_log = model_fit.get_forecast(steps=12).summary_frame()
final_forecast = np.exp(final_forecast_log)

print("\n--- Next 12 Months Forecast (Original Scale) ---")
print(final_forecast[['mean', 'lower 95%', 'upper 95%']])
