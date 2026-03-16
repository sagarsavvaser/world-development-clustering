\# World Development Clustering Project



\## Project Goal



The goal of this project is to group countries with similar development indicators using machine learning clustering techniques.



\## Dataset



The dataset contains global development indicators such as:



\* GDP

\* Birth Rate

\* Life Expectancy

\* Infant Mortality Rate

\* Internet Usage

\* Health Expenditure (% of GDP)



These indicators help analyze economic and social development across countries.



\## Algorithms Used



\### PCA (Principal Component Analysis)



PCA reduces many features into two components (PC1 and PC2) for visualization.



\### K-Means Clustering



K-Means groups countries with similar development patterns into clusters.



\## Streamlit Visualization



A Streamlit app was built to:



\* Load trained models

\* Predict cluster of a country

\* Show clustering visualization



\## Project Structure



app.py – Streamlit application

predict.py – prediction logic

Cluster\_Analysis.ipynb – model training notebook

scaler.pkl – saved scaler

pca\_model.pkl – saved PCA model

kmeans\_model.pkl – saved clustering model



\## How to Run



Install dependencies



pip install -r requirements.txt



Run Streamlit app



streamlit run app.py



