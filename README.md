

# 📊Telecom Churn Analysis

A data-driven project focused on understanding and predicting customer churn in the telecom industry using Exploratory Data Analysis (EDA), machine learning models, and performance evaluation metrics.
**Live Demo**: 👉[https://telecom-churn-analysis-gl3a.onrender.com/]


## 📌Project Description
Customer churn is a critical metric for telecom companies, reflecting how many customers leave over a given period. In this project, we analyze a customer dataset to uncover key patterns, build predictive models, and deliver business insights to reduce churn and improve customer retention strategies.
## 🛠️Tech Stack


**Languages & Libraries:** Python, NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn

**IDE/Tools:** Jupyter Notebook / VS Code

**Models Used:** 
Multiple classification models were trained and evaluated:

- Logistic Regression
- Decision Tree
- Random Forest
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Gradient Boosting
- AdaBoost
- **Voting Classifier (Ensemble Method)**

Final Accuracy Score: 0.8161 (~81.6%)

This ensemble outperformed most standalone models, demonstrating the effectiveness of combining multiple classifiers.

## 📌Features
The prediction is made using the following customer attributes:

Demographics:

- Gender
- SeniorCitizen
- Partner
- Dependents
Account and Service Details:

- tenure (Months of subscription)
- PhoneService
- MultipleLines
- InternetService
- OnlineSecurity
- OnlineBackup
- DeviceProtection
- TechSupport
- StreamingTV
- StreamingMovies
- Contract
- PaperlessBilling
- PaymentMethod
Financials:
- MonthlyCharges
- TotalCharges

  
## 📌Acknowledgements

This project was inspired by real-world customer retention challenges in the telecom sector.

## 🤝Contributions

Contributions are always welcome!



## 📌Run Locally

Clone the project

```bash
  git clone https://github.com/Ananyasiingh/Telecom-Churn-Analysis
```

Create and activate virtual environment

```bash
  python -m venv myenv
  source myenv/bin/activate
```

Install required libraries

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  streamlit run app.py
```
Or check it live🔗

https://telecom-churn-analysis-gl3a.onrender.com







