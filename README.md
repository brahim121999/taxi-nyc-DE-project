# NYC Yellow Taxi Data Engineering & Analytics Project

## 🚕 Context

This project aims to simulate a data engineering and data analytics mission for the urban transport sector. It is based on the public dataset of New York yellow taxis, with the goal of analyzing service performance, identifying optimization levers, and providing strategic indicators to support decision-making.

All stages have been modeled as a real project: from raw data ingestion to the delivery of indicators through business views, including transformation, orchestration, and automation of the processing workflows.

**Dataset source**: [NYC Taxi Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

---

## 🏗️ Architecture and Pipeline

- **Storage**: Google Cloud Storage (GCS)
- **Ingestion / Transformation**: BigQuery (advanced SQL queries, KPI calculations)
- **Orchestration**: Apache Airflow (Cloud Composer)
- **Exploratory Analysis**: Python / BigQuery
- **Visualization**: Business Views for dashboards

---

## 🔎 Business Questions Addressed

- Evolution of yellow taxi revenues over time
- Analysis of average fare per ride depending on distance, time of day, and area
- Study of payment methods and their trends
- Analysis of customer tipping behavior depending on context (period, amount, location)
- Geographic distribution of rides and volumes across NYC zones
- Specific analysis of airport trips (JFK, LaGuardia, Newark)
- Ride frequencies and average durations
- Identification of peak hours and high-demand zones
- Impact of additional charges (taxes, surcharges)
- Demand forecasting and recommendations to optimize fleet deployment

---

## 🤖 Machine Learning with BigQuery ML

A dedicated section of the project explores predictive modeling using **BigQuery ML**, including:

- Creation of training and test datasets directly in BigQuery
- Training of several regression models: **Boosted Tree**, **Random Forest**, **DNN Regressor** and **Automl Regressor**
- Evaluation of models using common metrics (MAE, MSE, R²)
- Predictions on new data
- Analysis of **feature importance** to interpret model behavior

This part was built entirely with **SQL inside BigQuery**.

---

## 🧩 Technologies Used

- **Python** (analysis scripts, BigQuery integration)
- **SQL / BigQuery** (transformations, analytical modeling, ML models)
- **GCP / GCS** (cloud storage)
- **Apache Airflow (Cloud Composer)** (pipeline orchestration)
- **BigQuery ML** (machine learning via SQL)
- **GitHub** (version control and documentation)
- **Business Views** (business-oriented views for data delivery)
