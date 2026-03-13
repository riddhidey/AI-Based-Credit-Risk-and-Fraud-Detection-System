# AI-Based Credit Risk and Fraud Detection System 
“AI-Based Credit Risk and Fraud Detection System  – FinTech Project”

# 💳AI-Based Credit Risk and Fraud Detection System 

## Project Overview
This is a **FinTech software application** that predicts the credit risk of a loan applicant using a trained **Logistic Regression model**.  
The app is developed with **Python** and deployed as a **Streamlit web application**, making it easy to run on any system.

The project demonstrates how AI can help in **automating credit risk assessment**, assisting financial institutions in making faster and informed lending decisions.

## Features
- Predicts **Low Risk** or **High Risk** of loan default
- Shows **probability of default** for detailed insights
- Interactive and user-friendly **Streamlit interface**
- Automatically handles **missing input values**
- Lightweight and easy to run on any PC

## Dataset
The model uses the following features:

| Feature                     | Description                          |
|-------------------------------|--------------------------------------|
| `person_age`                | Age of the applicant                 |
| `person_income`             | Annual income of the applicant       |
| `loan_amnt`                 | Requested loan amount                |
| `loan_int_rate`             | Loan interest rate (%)               |
| `person_emp_length`         | Employment length (years)            |
| `loan_percent_income`       | Debt-to-income ratio (%)             |

The target variable is `loan_status` (`0` = Low Risk, `1` = High Risk).  
The dataset is included in the `DATASET/` folder as `credit_risk_dataset.csv`.

---

