import streamlit as st
import pandas as pd
import numpy as np
import requests

st.title('Fake News Predictor Input Data Monitoring')

data_url = "https://api.news-wise-ai.com/article-data"
data_filename = "data_len.csv"

def get_data():
    try:
        response = requests.get(url=data_url).json()
    except:
        st.error("Data could not be fetched", icon="🚨")

    data_file = open(data_filename, "w")
    data_file.write(response["article_data"])
    data_file.close()

def show_data():

    data = pd.read_csv(data_filename, names=["datetime", "word_len"], header=None)

    st.line_chart(data=data, x="datetime", y="word_len")

st.button("Refresh", on_click=get_data())

show_data()