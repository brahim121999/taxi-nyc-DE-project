# NYC Yellow Taxi Data Engineering & Analytics Project

## 🚕 Context

This project aims to simulate a data engineering and data analytics mission for the urban transport sector. It is based on the public dataset of New York yellow taxis, with the goal of analyzing service performance, identifying optimization levers, and providing strategic indicators to support decision-making.

All stages have been modeled as a real project: from raw data ingestion to the delivery of indicators through business views, including transformation, orchestration, and automation of the processing workflows.

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

## 🧩 Technologies Used

- **Python** (analysis scripts, BigQuery integration)
- **SQL / BigQuery** (transformations, analytical modeling)
- **GCP / GCS** (cloud storage)
- **Apache Airflow (Cloud Composer)** (pipeline orchestration)
- **GitHub** (version control and documentation)
- **Business Views** (business-oriented views for data delivery)
