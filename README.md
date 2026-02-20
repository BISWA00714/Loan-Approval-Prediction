# Loan-Approval-Prediction

**📊 Loan Approval Prediction using Machine Learning**

**🔍 Project Overview**

This project focuses on building a Machine Learning classification model to predict whether a loan application will be approved based on applicant demographic and financial information.

The goal of this project is to transform raw financial data into actionable insights and develop a predictive system that assists in data-driven loan approval decisions.

**🎯 Problem Statement**

Financial institutions receive thousands of loan applications.
Manually evaluating each application is time-consuming and prone to bias.

This project aims to:

Analyze applicant data

Identify key approval factors

Build a predictive model for loan approval status

**📁 Dataset Information**

- The dataset contains applicant details such as:
- Gender
- Marital Status
- Dependents
- Applicant Income
- Coapplicant Income
- Loan Amount
- Loan Term
- Credit History
- Property Area
- Loan Status (Target Variable)

Target Variable:
Loan_Status → Approved (1) / Not Approved (0)

**🧹 Data Preprocessing**

- Handled missing values using statistical imputation

- Converted categorical variables into numerical format

- Cleaned inconsistent data entries

- Feature engineering for improved prediction

- Converted boolean features into numeric values

**📊 Exploratory Data Analysis (EDA)**

- Performed analysis to understand:

- Loan approval distribution

- Impact of credit history

- Income vs loan amount relationship

Applicant demographic patterns

🤖 Models Used
*1️⃣ Logistic Regression*

Baseline classification model

Achieved 78.86% accuracy

Provided stable and interpretable predictions

*2️⃣ Decision Tree Classifier*

Compared performance with Logistic Regression

Lower accuracy but useful for comparison

**📈 Model Evaluation Metrics**

Accuracy Score

Confusion Matrix

Precision & Recall

F1 Score

Logistic Regression was selected as the final model due to better overall performance.

**🧠 Key Insights**

Credit history strongly influences loan approval.

Proper preprocessing significantly improves model results.

Model evaluation requires more than accuracy — recall and precision are critical.

Logistic Regression performed more consistently than Decision Tree.

**🛠️ Technologies Used**

Python

Pandas

NumPy

Scikit-learn

Matplotlib

Seaborn

Jupyter Notebook

# 📌 Project Structure
loan-approval-prediction-ml/
│
├── Loan_Prediction.ipynb
├── dataset.csv
└── README.md

**🚀 Future Improvements**

Apply Random Forest & XGBoost

Hyperparameter tuning

Handle class imbalance

Deploy model using Streamlit

👨‍💻 Author

Biswajit
Data Science & AI Enthusiast
