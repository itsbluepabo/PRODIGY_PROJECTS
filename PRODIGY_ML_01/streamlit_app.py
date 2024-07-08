# streamlit_app.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import streamlit as st

# Load the dataset
df = pd.read_csv('train.csv')

# Select features and target variable
features = ["GrLivArea", "BedroomAbvGr", "FullBath"]
X = df[features]
y = df["SalePrice"]

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Streamlit app
st.title("House Price Prediction App")

# Input fields for new data
st.sidebar.header("Input Features")
GrLivArea = st.sidebar.number_input("GrLivArea", value=2000)
BedroomAbvGr = st.sidebar.number_input("BedroomAbvGr", value=3)
FullBath = st.sidebar.number_input("FullBath", value=2)

# Button to trigger prediction
if st.sidebar.button("Predict"):
    new_data = pd.DataFrame({'GrLivArea': [GrLivArea], 'BedroomAbvGr': [BedroomAbvGr], 'FullBath': [FullBath]})
    new_data_scaled = scaler.transform(new_data)
    predicted_price = model.predict(new_data_scaled)
    st.subheader(f'Predicted Price: ${predicted_price[0]:,.2f}')



y_pred = model.predict(X_test)


