# 📊 CS531 — Class 2 Experiments: Data Types, APIs & Sampling [Google Colab]

This repository contains hands-on experiments from **CS531 Class 2** (Data Types & Acquisition) taught by Dr. Paul at Yuan Ze University.
All notebooks are Google Colab-ready and designed to demonstrate real-world scenarios involving structured, semi-structured, and unstructured data.

---

## 🔧 Setup Instructions

✅ All notebooks run on **Google Colab** — no setup needed. Just click and run!

To run locally:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn requests
```

---

## 📘 Experiments Overview

| # | Title                                      | Type             | Key Topics                          |
|---|--------------------------------------------|------------------|-------------------------------------|
| 1 | Simple Random Sampling on CSV              | Structured       | Pandas, `.sample()`, SRS           |
| 2 | NASA Public API JSON to DataFrame          | Semi-structured  | REST API, JSON, DataFrame parsing  |
| 3 | Stratified Sampling on Categorical Data    | Structured       | Stratification, class balance      |
| 4 | Open-Meteo Weather API (Semi-structured)   | Semi-structured  | JSON parsing, coordinates          |
| 5 | Unstructured Email Parsing                 | Unstructured     | Text parsing, regex, metadata      |

---

## 🧪 Experiment Details

### 🧩 01. Simple Random Sampling (SRS)

📄 `notebooks/01_random_sampling.ipynb`

**What we did**:
- Loaded the Iris dataset from a public URL.
- Used `df.sample(n=20)` to extract a simple random sample.
- Discussed reproducibility via `random_state`.

**What to try**:
- Vary sample size using `n` or `frac`.
- Visualize a feature distribution on the sample vs. full dataset.
- Observe effect of `random_state=None`.

---

### 🪐 02. Public API: NASA Near Earth Objects

📄 `notebooks/02_public_api_nasa.ipynb`

**What we did**:
- Queried NASA NEO API using `requests`.
- Parsed nested JSON with `pd.json_normalize`.
- Extracted asteroid name, magnitude, hazard flag.

**What to try**:
- Explore different API endpoints.
- Save the result to a CSV.
- Count how many asteroids are flagged hazardous.

---

### 🐧 03. Stratified Sampling on Penguins Dataset

📄 `notebooks/03_stratified_sampling_penguins.ipynb`

**What we did**:
- Loaded seaborn's `penguins` dataset.
- Performed stratified sampling by species using `train_test_split(..., stratify=...)`.
- Validated class balance in the output sample.

**What to try**:
- Try stratifying by a different variable like `island`.
- Visualize the stratified sample with `seaborn.pairplot()`.
- Compare to unstratified (random) sampling.

---

### 🌦️ 04. Weather API (Open-Meteo, Semi-structured JSON)

📄 `notebooks/04_weather_api_openmeteo.ipynb`

**What we did**:
- Called Open-Meteo API for hourly weather in Taipei.
- Extracted temperature over time to a DataFrame.
- Plotted basic time-series trends.

**What to try**:
- Change to your hometown coordinates.
- Plot line graph of temperature using `matplotlib`.
- Add other weather fields (rain, wind speed).

---

### 📧 05. Email Metadata Parsing (Unstructured)

📄 `notebooks/05_email_parser_unstructured.ipynb`

**What we did**:
- Parsed raw email-style plain text.
- Extracted headers (`From`, `To`, `Subject`) and cleaned the body.
- Introduced metadata vs. free-text body split.

**What to try**:
- Write regex to extract additional metadata (date/time).
- Try parsing multiple messages separated by `---`.
- Save metadata to a JSON or CSV.


---

## 👨‍🏫 Instructor

**Dr. A Paul**  
Assistant Professor, Department of Computer Science & Engineering  
Yuan Ze University, Taiwan  

---

## 📄 License

MIT License. Educational use encouraged. Attribution appreciated.
