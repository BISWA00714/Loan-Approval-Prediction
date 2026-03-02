import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open("model.pkl","rb"))
model_columns = pickle.load(open("columns.pkl","rb"))

st.title("🏦 Loan Approval Prediction")

# Inputs
gender = st.selectbox("Gender", ["Male","Female"])
married = st.selectbox("Married", ["Yes","No"])
dependents = st.selectbox("Dependents", ["0","1","2","3+"])
education = st.selectbox("Education", ["Graduate","Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes","No"])
applicant_income = st.number_input("Applicant Income")
coapplicant_income = st.number_input("Coapplicant Income")
loan_amount = st.number_input("Loan Amount")
loan_term = st.number_input("Loan Term")
credit_history = st.selectbox("Credit History", [1,0])
property_area = st.selectbox("Property Area", ["Urban","Semiurban","Rural"])

if st.button("Predict"):

    input_dict = {
        "Dependents": 3 if dependents=="3+" else int(dependents),
        "ApplicantIncome": applicant_income,
        "CoapplicantIncome": coapplicant_income,
        "LoanAmount": loan_amount,
        "Loan_Amount_Term": loan_term,
        "Credit_History": credit_history,
        "Gender_Male": 1 if gender=="Male" else 0,
        "Married_Yes": 1 if married=="Yes" else 0,
        "Education_Not Graduate": 1 if education=="Not Graduate" else 0,
        "Self_Employed_Yes": 1 if self_employed=="Yes" else 0,
        "Property_Area_Semiurban": 1 if property_area=="Semiurban" else 0,
        "Property_Area_Urban": 1 if property_area=="Urban" else 0,
    }

    input_df = pd.DataFrame([input_dict])

    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Not Approved")