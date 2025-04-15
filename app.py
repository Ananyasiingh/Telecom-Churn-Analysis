import pickle
import pandas as pd
import streamlit as st

st.header("Telecom Churn Prediction")

# Collecting user inputs
col1, col2 = st.columns(2)

# Gender input
gender = st.selectbox("gender", ["Male", "Female"])
g = 0 if gender == "Male" else 1

# Senior Citizen input
SeniorCitizen = st.number_input("Senior Citizen (0 or 1)", min_value=0, max_value=1, step=1)

# Partner input
Partner = st.selectbox("Partner", ["Yes", "No"])
Ptr = 1 if Partner == "Yes" else 0

# Dependents input
Dependents = st.selectbox("Dependents", ["Yes", "No"])
Dpd = 1 if Dependents == "Yes" else 0

# Tenure input
tn = st.number_input("Tenure (months)", min_value=0, step=1)

# Phone Service input
PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
ps = 1 if PhoneService == "Yes" else 0

# Multiple Lines input
MultipleLines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
ml = {"Yes": 1, "No": 0, "No phone service": -1}[MultipleLines]

# Internet Service input
InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
ins = {"DSL": 1, "Fiber optic": 2, "No": 0}[InternetService]

# Online Security input
OnlineSecurity = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
os = {"Yes": 1, "No": 0, "No internet service": -1}[OnlineSecurity]

# Online Backup input
OnlineBackup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
ob = {"Yes": 1, "No": 0, "No internet service": -1}[OnlineBackup]

# Device Protection input
DeviceProtection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
dp = {"Yes": 1, "No": 0, "No internet service": -1}[DeviceProtection]

# Tech Support input
TechSupport = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
ts = {"Yes": 1, "No": 0, "No internet service": -1}[TechSupport]

# Streaming TV input
StreamingTV = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
streaming_tv = {"Yes": 1, "No": 0, "No internet service": -1}[StreamingTV]

# Streaming Movies input
StreamingMovies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
streaming_movies = {"Yes": 1, "No": 0, "No internet service": -1}[StreamingMovies]

# Contract input
Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
ct = {"Month-to-month": 1, "One year": 2, "Two year": 3}[Contract]

# Paperless Billing input
PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
pb = 1 if PaperlessBilling == "Yes" else 0

# Payment Method input
PaymentMethod = st.selectbox(
    "Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
)
pm = {
    "Electronic check": 1,
    "Mailed check": 2,
    "Bank transfer (automatic)": 3,
    "Credit card (automatic)": 4,
}[PaymentMethod]

# Monthly Charges input
mc = st.number_input("Monthly Charges", min_value=0.0, step=0.1)

# Total Charges input
tc = st.number_input("Total Charges", min_value=0.0, step=0.1)

# Feature DataFrame construction
def features():
    return pd.DataFrame(
        {
            "gender": [g],
            "SeniorCitizen": [SeniorCitizen],
            "Partner": [Ptr],
            "Dependents": [Dpd],
            "tenure": [tn],
            "PhoneService": [ps],
            "MultipleLines": [ml],
            "InternetService": [ins],
            "OnlineSecurity": [os],
            "OnlineBackup": [ob],
            "DeviceProtection": [dp],
            "TechSupport": [ts],
            "StreamingTV": [streaming_tv],
            "StreamingMovies": [streaming_movies],
            "Contract": [ct],
            "PaperlessBilling": [pb],
            "PaymentMethod": [pm],
            "MonthlyCharges": [mc],
            "TotalCharges": [tc],
        }
    )

# Button for prediction
if st.button("Predict"):
    try:
        # Loading model
        model = pickle.load(open("model.pkl", "rb"))

        # Preparing features
        df = features()

        # Prediction
        prediction = model.predict(df)
        st.header(f"Churn Prediction: {'Yes' if prediction[0] else 'No'}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
