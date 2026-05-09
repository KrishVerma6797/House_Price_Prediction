# House Price Prediction using Linear Regression

## Project Overview
- This project implements an end-to-end machine learning pipeline to predict house prices using structured housing data.
- The focus is on correct data preprocessing, appropriate evaluation for regression problems, and reliable prediction rather than complex models.

---

## Objective
- Predict house prices using property features
- Handle numerical and categorical data correctly
- Apply appropriate regression evaluation metrics
- Enable price prediction for new user inputs

---

## Dataset Description
- Dataset: Housing.csv
- Rows: 545
- Features: 12
- Target Variable: price

### Feature Types

#### Numerical Features
- area
- bedrooms
- bathrooms
- stories
- parking

#### Categorical Features
- mainroad (yes / no)
- guestroom (yes / no)
- basement (yes / no)
- hotwaterheating (yes / no)
- airconditioning (yes / no)
- prefarea (yes / no)
- furnishingstatus (furnished / semi-furnished / unfurnished)

- Although the dataset does not contain missing values, a robust preprocessing pipeline with imputation was implemented to make the system suitable for real-world data.

---

## Methodology

### Data Preprocessing
- Separated input features and target variable
- Automatically identified numerical and categorical columns
- Applied preprocessing steps:
  - Median imputation for numerical features
  - Most frequent (mode) imputation for categorical features
  - One-Hot Encoding for categorical variables
- Used ColumnTransformer and Pipeline to ensure consistent preprocessing during both training and prediction

---

### Model Used
- Linear Regression

---


## How to Run the Project

### Install dependencies
```bash
pip install -r requirements.txt
```
Run the project
```
python main1.py
```
--- 

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
