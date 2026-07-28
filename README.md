# 🚗 Used Vehicle Price Prediction using Machine Learning

An end-to-end Machine Learning project that predicts the selling price of used two-wheelers and four-wheelers using regression models. The project covers data preprocessing, exploratory data analysis (EDA), feature engineering, model training, hyperparameter tuning, and deployment via a Streamlit web application.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Scikit--learn](https://img.shields.io/badge/Scikit--learn-ML-orange)
![XGBoost](https://img.shields.io/badge/XGBoost-Regressor-green)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📑 Table of Contents

- [Project Overview](#-project-overview)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Technologies Used](#️-technologies-used)
- [Dataset](#-dataset)
- [Exploratory Data Analysis](#-exploratory-data-analysis)
- [Feature Engineering](#️-feature-engineering)
- [Machine Learning Models](#-machine-learning-models)
- [Model Evaluation](#-model-evaluation-metrics)
- [Streamlit Application](#-streamlit-application)
- [Installation](#-installation)
- [Screenshots](#-screenshots)
- [Requirements](#-requirements)
- [Future Improvements](#-future-improvements)
- [Learning Outcomes](#-learning-outcomes)
- [Author](#-author)
- [Contact](#-contact)

---

## 📌 Project Overview

The resale value of a vehicle depends on multiple factors such as:

- Brand
- Model
- Manufacturing Year
- Mileage
- Fuel Type
- Engine Capacity
- Transmission
- Accident History
- Clean Title
- Exterior & Interior Color

This project builds an intelligent Machine Learning model that predicts the estimated selling price of a used vehicle based on these features.

---

## 🚀 Features

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Multiple Regression Models
- Hyperparameter Tuning
- Model Comparison
- Streamlit Web Application
- Professional Project Structure
- Ready for Deployment

---


## 🛠️ Technologies Used

| Technology     | Purpose                  |
|----------------|---------------------------|
| Python         | Programming Language      |
| Pandas         | Data Manipulation         |
| NumPy          | Numerical Computing       |
| Matplotlib     | Data Visualization        |
| Seaborn        | Statistical Visualization |
| Plotly         | Interactive Charts        |
| Scikit-learn   | Machine Learning          |
| XGBoost        | Gradient Boosting         |
| Joblib         | Model Serialization       |
| Streamlit      | Web Application           |

---

## 📊 Dataset

The dataset contains information about used vehicles.

### Features

| Column          | Description                       |
|------------------|------------------------------------|
| Brand            | Vehicle Manufacturer              |
| Model            | Vehicle Model                     |
| Model Year       | Manufacturing Year                |
| Mileage          | Distance Driven                   |
| Fuel Type        | Petrol, Diesel, Electric, etc.     |
| Engine           | Engine Specification              |
| Transmission     | Automatic / Manual                |
| Exterior Color   | Vehicle Exterior Color            |
| Interior Color   | Vehicle Interior Color            |
| Accident         | Accident History                  |
| Clean Title      | Title Status                      |
| Price            | Target Variable                   |

---

## 📈 Exploratory Data Analysis

Analysis performed on:

- Price Distribution
- Mileage Distribution
- Brand Analysis
- Fuel Type Analysis
- Transmission Analysis
- Vehicle Age vs Price
- Mileage vs Price
- Correlation Heatmap
- Outlier Detection
- Feature Relationships

### Key Insights

- Vehicle prices are right-skewed.
- Luxury brands generally have higher resale values.
- Older vehicles tend to have lower selling prices.
- Increased mileage is associated with lower prices.
- Accident history negatively impacts resale value.
- Vehicles with a clean title generally command higher prices.

---

## ⚙️ Feature Engineering

Implemented:

- Vehicle Age Calculation
- Engine Size Extraction
- Missing Value Handling
- Duplicate Removal
- One-Hot Encoding
- Numerical Feature Processing

---

## 🤖 Machine Learning Models

The following regression algorithms were trained and evaluated:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Extra Trees Regressor
- Gradient Boosting Regressor
- XGBoost Regressor

---

## 📊 Model Evaluation Metrics

Models were evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

The best-performing model was selected after hyperparameter tuning.

---

## 🌐 Streamlit Application

The web application allows users to:

- Select Vehicle Brand
- Select Model
- Enter Model Year
- Enter Mileage
- Choose Fuel Type
- Select Transmission
- Enter Engine Size
- Select Accident History
- Select Clean Title
- Predict Vehicle Price

---

## 🚀 Installation

### 1. Clone Repository

```bash
git clone https://github.com/Surajbhatade007/Car_price_Prediction.git
cd Car_price_Prediction
```

### 2. Create Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Streamlit App

```bash
python -m streamlit run app.py
```



## 📦 Requirements

```
pandas
numpy
matplotlib
seaborn
plotly
scikit-learn
xgboost
joblib
streamlit
```

---

## 🎯 Future Improvements

- [ ] Support image-based vehicle analysis
- [ ] Vehicle recommendation system
- [ ] Price trend forecasting
- [ ] Cloud deployment
- [ ] Docker containerization
- [ ] REST API using FastAPI
- [ ] SHAP-based model explainability
- [ ] CI/CD pipeline for automated deployment

---

## 💡 Learning Outcomes

Through this project, practical experience was gained in:

- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Regression Algorithms
- Hyperparameter Tuning
- Model Evaluation
- Pipeline Development
- Streamlit Application Development
- End-to-End Machine Learning Workflow

---

## 👨‍💻 Author

**Suraj Bhatade**

**Skills:** Python · Machine Learning · Data Science · Scikit-learn · XGBoost · Pandas · NumPy · Streamlit · Git & GitHub


---

## 📧 Contact

- **GitHub:** https://github.com/Surajbhatade007
- **LinkedIn:**  www.linkedin.com/in/surajbhatade5709
- **Email:** surajbhatade5709@gmail.com


