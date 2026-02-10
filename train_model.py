import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("student_performance.csv")

# Features and target
X = data[["Attendance", "Study_Hours", "Previous_Score"]]
y = data["At_Risk"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# SAVE MODEL
with open("student_risk_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved successfully")

# Accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)

# Prediction
print("\nEnter new student details:")
attendance = float(input("Attendance (%): "))
study_hours = float(input("Study Hours per day: "))
previous_score = float(input("Previous Exam Score: "))

prediction = model.predict([[attendance, study_hours, previous_score]])

if prediction[0] == 1:
    print("⚠️ Student is AT RISK")
else:
    print("✅ Student is NOT at risk")
