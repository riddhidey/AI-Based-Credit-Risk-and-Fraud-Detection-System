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

## Folder Structure

Credit_Risk_Analyzer/
├── app.py
├── credit_model.pkl
├── scaler.pkl
├── imputer.pkl
├── DATASET/
│   └── credit_risk_dataset.csv
├── requirements.txt
├── README.md

## Installation & Running the App
1: **Clone the repository:**
git clone https://github.com/PRATHIRTH-M/Credit_Risk_Analyzer.git

2: **Navigate to the project folder:**
cd AIBF_CREDIT_RISK

3: **Activate your virtual environment:**

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

4: **Install dependencies:**
pip install -r requirements.txt

5: **Run the Streamlit app:**
streamlit run app.py

**Usage**
1.Open the app in your browser.
2.Enter the applicant’s information in the sidebar:
- Age, Income, Loan Amount, Interest Rate, Employment Length, Debt-to-Income Ratio
3.Click Analyze Risk.
4.The app will display:
- Low Risk or High Risk
- Probability of default
- Visual risk indicator (progress bar)

**Tools & Libraries**
- Python 3.x
- Streamlit
- Pandas
- Scikit-learn
- Joblib

**Author**
Prathirth Mohite – Developed as part of the FinTech AI Software Application assignment.

**Impact**
This project shows how AI can support FinTech decision-making by providing automated credit risk assessment, saving time, and reducing human error in the loan approval process.
