# NYC Yellow Taxi Data Engineering & Analytics Project

## 🚕 Contexte

Ce projet a pour objectif de simuler une mission data engineering & data analytics pour le secteur du transport urbain. Il s’appuie sur le jeu de données public des taxis jaunes new-yorkais afin d’analyser la performance du service, identifier des leviers d’optimisation et fournir des indicateurs stratégiques pour la prise de décision.  

L’ensemble des étapes a été modélisé comme un projet réel : de l’ingestion des données brutes jusqu’à la restitution d’indicateurs via des vues métier (Business Views), en passant par la transformation, l’orchestration et l’automatisation des traitements.

---

## 🏗️ Architecture et pipeline

- **Stockage** : Google Cloud Storage (GCS)  
- **Ingestion / Transformation** : BigQuery (requêtes SQL avancées, calculs de KPI)  
- **Orchestration** : Apache Airflow (Cloud Composer)  
- **Analyse exploratoire** : Python / BigQuery  
- **Visualisation** : Business Views pour dashboards  

---

## 🔎 Problématiques business

- Évolution des revenus des taxis jaunes dans le temps  
- Analyse du prix moyen par course en fonction de la distance, de l’heure et du secteur  
- Étude des modes de paiement et leur évolution  
- Analyse du comportement de pourboire des clients selon contexte (période, montant, localisation)  
- Répartition géographique des trajets et volumes selon les zones de NYC  
- Analyse spécifique des trajets aéroportuaires (JFK, LaGuardia, Newark)  
- Fréquences et durées moyennes des courses  
- Identification des heures et zones de pics d’activité  
- Impact des charges additionnelles (taxes, surcharges)  
- Prévisions de la demande et recommandations pour optimiser la flotte  

---

## 🧩 Technologies utilisées

- **Python** (scripts d’analyse, intégration BigQuery)  
- **SQL / BigQuery** (transformations, modélisation analytique)  
- **GCP / GCS** (stockage cloud)  
- **Apache Airflow (Cloud Composer)** (orchestration des pipelines)  
- **GitHub** (versionning et documentation)  
- **Business Views** (vues orientées métier pour restitution)  
