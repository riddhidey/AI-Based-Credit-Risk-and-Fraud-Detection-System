# app.py
import streamlit as st
import pandas as pd
import joblib
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="💳 AI Credit Risk Analyzer",
    page_icon="💰",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Title and description
st.title("💳 AI-Based Credit Risk Analyzer")
st.markdown("""
This application predicts the **credit risk** of a loan applicant using a trained AI model.  
Enter the applicant's information and click **Analyze Risk** to see the result.
""")

# Load model, scaler, imputer
@st.cache_resource
def load_files():
    model = joblib.load('credit_model.pkl')
    scaler = joblib.load('scaler.pkl')
    imputer = joblib.load('imputer.pkl')
    return model, scaler, imputer

try:
    model, scaler, imputer = load_files()
except Exception as e:
    st.error(f"Error loading files: {e}")
    st.stop()

# Sidebar for user input
st.sidebar.header("Applicant Information")

def user_input():
    age = st.sidebar.number_input("Age", 18, 100, 30)
    income = st.sidebar.number_input("Annual Income ($)", 1000, 1000000, 50000)
    loan_amnt = st.sidebar.number_input("Loan Amount ($)", 500, 500000, 10000)
    int_rate = st.sidebar.number_input("Interest Rate (%)", 1.0, 30.0, 10.5)
    emp_length = st.sidebar.number_input("Employment Length (Years)", 0, 50, 5)
    dti = st.sidebar.number_input("Debt-to-Income Ratio (%)", 0.0, 100.0, 15.0)
    return pd.DataFrame({
        'person_age':[age],
        'person_income':[income],
        'loan_amnt':[loan_amnt],
        'loan_int_rate':[int_rate],
        'person_emp_length':[emp_length],
        'loan_percent_income':[dti/100]
    })

input_df = user_input()

# Prediction button
if st.button("Analyze Risk"):
    try:
        # Apply imputer
        input_imputed = imputer.transform(input_df)
        # Scale input
        X_scaled = scaler.transform(input_imputed)
        # Predict
        pred = model.predict(X_scaled)[0]
        pred_prob = model.predict_proba(X_scaled)[0][1]  # Probability of high risk

        # Display result
        st.subheader("Result:")
        if pred == 0:
            st.success(f"✅ LOW RISK - Likely to repay loan\nProbability of default: {pred_prob*100:.2f}%")
        else:
            st.error(f"⚠️ HIGH RISK - May default on loan\nProbability of default: {pred_prob*100:.2f}%")

        # Optional: show a visual risk bar
        st.progress(int(pred_prob*100))

    except Exception as e:
        st.error(f"Error during prediction: {e}")

# Footer
st.markdown("""
---
Developed by **Prathirth Mohite** | FinTech AI Project
""")
