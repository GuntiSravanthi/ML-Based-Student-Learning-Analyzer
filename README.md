# ML-Based Student Learning Analyzer

## Project Overview
his project is a Machine Learning–based web application that predicts whether a student is academically at risk. The prediction is made using key academic indicators such as attendance percentage, study hours per day, and previous exam scores. The goal of this system is to help educators identify students who may need additional support at an early stage.

## Problem Statement
Early identification of academically at-risk students enables timely intervention, improves learning outcomes, and supports data-driven academic decision-making. This project demonstrates how machine learning can assist in educational analytics.
## Machine Learning Model
- Algorithm Used: Logistic Regression
- Type: Binary Classification
- Output:
- Low Risk
- High Risk
The model also provides a probability score indicating prediction confidence.
## Dataset
The dataset contains the following features:
- Attendance (%)
- Study Hours per Day
- Previous Exam Score
- Risk Level (Target)

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- pickle

## Project Structure
- `student_data.py` – Dataset creation
- `train_model.py` – Model training
- `predict_student.py` – Student risk prediction
- `student_performance.csv` – Dataset file
- `student_risk_model.pkl` – Trained ML model
- app.py – Streamlit web application
- requirements.txt – Required dependencies

## How to Run the Project
1. Clone the repository
2. Install required libraries:
## pip install pandas scikit-learn
3. Train the model:
## python train_model.py
4. Predict student risk:
## python predict_student.py

## Output
The model predicts whether a student is at **Low Risk** or **High Risk**.

## Author
**Sravanthi Gunti**

