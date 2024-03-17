import random
from matplotlib import pyplot as plt
import streamlit as st
import plotly.graph_objects as go
from datetime import datetime
import numpy as np
import pandas as pd

# app = mr.App(title="Hello in Mercury!", description="Samples app in Mercury")
def main():
    # Read the CSS file
    with open('C:/Users/kunjd/Desktop/Predicitive_Demand_Forecasting/36/source_code/web/style.css', 'r') as f:
        css = f.read()
    # Inject CSS styles using markdown
    st.markdown(f"<style>{css}</style>",unsafe_allow_html=True)
    # Display content with the custom style
if __name__ == "__main__":
    main()
st.markdown("# Product Demand Forecasting")
st.write('<hr>',unsafe_allow_html=True)
st.header("Basic Insights")
st.subheader("Approach")
st.write('<span style="font-size: 20px;">Our problem statement is to optimise availability of products considering different factors</span>',unsafe_allow_html=True)
st.write("<span style='font-size: 20px;'>The purpose behind this is to get insights about the products and the regions so as to provide more resources and deploy more manpower to cater to the needs of the user.</span>",unsafe_allow_html=True)
st.write("<span style='font-size: 20px;'>We will then advice the enterprise to deploy more warehouses amidst the centre of this clusters which reduces the important issue of delivery time and cost.</span>",unsafe_allow_html=True)
st.subheader("Data Pre-processing")
st.write("<span style='font-size: 20px;'>Dataset consists of product_id(there are total 416 unique products)</span> ",unsafe_allow_html=True)
st.write("<span style='font-size: 20px;'>region(28 different PIN codes are given)</span>",unsafe_allow_html=True)
st.write("<span style='font-size: 20px;'>purchased_date</span>",unsafe_allow_html=True)
st.write("<span style='font-size: 20px;'>In our dataset, we've pre-processed data in a w</span>",unsafe_allow_html=True)
st.subheader(" Data Analysis:")
# st.image('img1.png',use_column_width=True)



# st.markdown('<strong>Approach:</strong>',unsafe_allow_html=True)
st.subheader("Algorithms Used:")
st.write('<b>TIME SERIES ANALYSIS</b> is a statistical technique used to analyze data points collected or recorded over time intervals. It involves identifying patterns, trends, and relationships within the time series data to make predictions or extract meaningful insights.its key features are:</span>',unsafe_allow_html=True)
st.write("<span style='font-size: 20px;'>FORECASTING FUTURE VALUES: It enables forecasting future data points based on historical observations, which is crucial for decision-making and planning.</span>",unsafe_allow_html=True)
st.write("<span style='font-size: 20px;'>MODELLING DEPENDENCIES: Time series models capture dependencies between data points, allowing for accurate prediction by considering autocorrelation and other time-dependent relationships.</span>",unsafe_allow_html=True)
st.write("<span style='font-size: 20px;'>ALGORITHMS USED:Time series analysis algorithms include prophet,streamlit,XGboost.</span>",unsafe_allow_html=True)
st.write("<span style='font-size: 20px;'>STREAMLIT :</span>",unsafe_allow_html=True)
st.write("<span style='font-size: 20px;'>A Python library used for building interactive web applications for data science and machine learning projects</span>",unsafe_allow_html=True)
st.write("<span style='font-size: 20px;'>It allows developers to create interactive web applications directly from Python scripts</span>",unsafe_allow_html=True)
st.write("<span style='font-size: 20px;'>It can easily integrate popular data visualization</span>",unsafe_allow_html=True)

with st.container():
        # Apply custom styles to the form container
        with st.container():
            st.write("Please fill out the form:")
            st.subheader("")
        # Apply custom styles to the form container
        st.markdown('<div id="my-form-container" style="background-color:white;">', unsafe_allow_html=True)
        with st.form(key='basic_form'):
            region = st.text_input("Pin Code:")
            date = st.date_input("Date:")
            date_str =date.strftime('%Y-%m-%d')
            print(date_str)
            submit_button = st.form_submit_button(label='Submit')
        st.markdown('</div>', unsafe_allow_html=True)

        if submit_button:
            df=pd.read_csv("C:/Users/kunjd/Desktop/Predicitive_Demand_Forecasting/36/dataset/Final_csv.csv").sample(n=50000)
            new_product_id = []
            new_date = []
            uni_pro = {}
            count = 1
            product = list(df['product_id'])
            # print(list(df['product_id'])[2])
            for i in range(len(df)):
                if product[i] in uni_pro:
                    new_product_id.append(uni_pro[product[i]])
                else:
                    uni_pro[product[i]] ="product_"+ str(count)
                    count+=1
                    new_product_id.append(uni_pro[product[i]])
            df['new_product_id'] = new_product_id
            def predict_demand(region,date):
                outcome = {}
                region = int(region)
                dt = date[5:7]
                for i in range(len(df)):
                    if df['region'].iloc[i] == region and df["purchase_date"].iloc[i][5:7] == dt:
                        if df['product_id'].iloc[i] in outcome:
                            outcome[df['product_id'].iloc[i]] += df['frequency'].iloc[i]
                        else:
                            outcome[df['product_id'].iloc[i]] = df['frequency'].iloc[i]

                return outcome
            data = predict_demand(region,date_str)
            sorted_dict_keys = dict(sorted(data.items()))
            # print(sorted_dict_keys)
            st.write("<span style='font-size: 20px;'>Form submitted!</span>",unsafe_allow_html=True)
            st.write("<span style='font-size: 20px;'>Pin Code:</span>", sorted_dict_keys,unsafe_allow_html=True)
            st.write("<span style='font-size: 20px;'>Date</span>", date,unsafe_allow_html=True)
if __name__ == "__main__":
    main()
# data = predict_demand(region,date_str)
# sorted_dict_keys = dict(sorted(data.items()))
# print(sorted_dict_keys)


