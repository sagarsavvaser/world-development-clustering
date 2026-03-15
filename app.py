import streamlit as st
import pandas as pd
from predict import predict_cluster

st.title("Global Development Cluster Prediction")

st.write("Enter country indicators to predict development cluster")

gdp = st.number_input("GDP")

life_female = st.number_input("Life Expectancy Female")

life_male = st.number_input("Life Expectancy Male")

infant_mortality = st.number_input("Infant Mortality Rate")

internet_usage = st.number_input("Internet Usage")

birth_rate = st.number_input("Birth Rate")

health_exp = st.number_input("Health Exp % GDP")

if st.button("Predict Cluster"):

    input_data = pd.DataFrame([[

        gdp,
        life_female,
        life_male,
        infant_mortality,
        internet_usage,
        birth_rate,
        health_exp

    ]], columns=[

        "GDP",
        "Life Expectancy Female",
        "Life Expectancy Male",
        "Infant Mortality Rate",
        "Internet Usage",
        "Birth Rate",
        "Health Exp % GDP"

    ])

    cluster = predict_cluster(input_data)

    st.success(f"This country belongs to Cluster {cluster}")