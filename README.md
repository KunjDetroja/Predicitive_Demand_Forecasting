# Predicitive_Demand_Forecasting
E-commerce Predictive Demand Forecasting Challenge

Overview:

This project focuses on predictive demand forecasting for an e-commerce platform. The goal is to optimize product availability across stores, ensure timely and fulfillment of regional     demands, and maximize product demand. 

Approach:

-Our problem statement is to optimise availability of products considering different factors.
-The purpose behind this is to get insights about the products and the regions so as to provide more resources and deploy more manpower to cater to the needs of the user.
-We will then advice the enterprise to deploy more warehouses amidst the centre of this clusters which reduces the important issue of delivery time and cost. Furthermore to forecast the    inventory demand needed in order to cater with the sales in specific region in the future.

Optimizing Product Availability:

- Analyzing raw data to understand product and regional distribution.
- Pre-processing data to extract insights on product demand in specific season.
- Exploring various generative and predictive models, including FBProphet, XGBoost.

Strategies Applied:

- Initial exploration involved extracting insights from raw data, identifying 416 products, 28 region codes, and a 3-year date range (2018-2020).
- Data manipulation focused on aggregating data to analyze product frequency/quantity in specific regions.
- Experimentation with different models, with a shift towards time series analysis (bivariate) for improved accuracy.

Time Series Analysis:

- Utilized FBProphet for multivariate time series analysis, incorporating product ID and datestamp to predict quantity demand.
- Explored XGBoost Regressor for quantity prediction in conjunction with FBProphet.
- Challenges encountered in training FBProphet model with two input points (product ID and date) to predict quantity output.

User Interface Development:

- Focus on improving model accuracy and selecting the best-performing model.
- Development of a user-friendly web interface using Streamlit for model deployment.

Usage:
-To replicate this project:
1. Install the necessary dependencies (Python libraries, Streamlit).
2. Clone this repository.
3. Run the Streamlit app to interact with the predictive demand forecasting model.

Future Improvements:

- Enhance model accuracy through further experimentation and fine-tuning.
- Explore advanced techniques such as ensemble models and feature engineering.
- Incorporate real-time data updates for dynamic forecasting.
- Encorporate Region based Model trainings to tune the models better and particularly for a single region.
- Use FBPROPHET to do time serial multivariate analysis and focus on seasonality of the product sales as well.
