# ML-Based Student Learning Analyzer

## Project Overview
This project uses Machine Learning to predict whether a student is at academic risk based on factors such as attendance, study hours, and previous exam scores.

## Problem Statement
Identifying students who are at academic risk early can help educators provide timely support and improve learning outcomes.

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
- Machine Learning (Classification)

## Project Structure
- `student_data.py` – Dataset creation
- `train_model.py` – Model training
- `predict_student.py` – Student risk prediction
- `student_performance.csv` – Dataset file
- `student_risk_model.pkl` – Trained ML model

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
