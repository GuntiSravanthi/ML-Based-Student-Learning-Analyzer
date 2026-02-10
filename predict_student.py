import pickle

# Load saved model
with open("student_risk_model.pkl", "rb") as f:
    model = pickle.load(f)

print("Model loaded successfully")

# Take new student input
attendance = float(input("Attendance (%): "))
study_hours = float(input("Study hours per day: "))
previous_score = float(input("Previous exam score: "))

# Predict
prediction = model.predict([[attendance, study_hours, previous_score]])

if prediction[0] == 1:
    print("⚠️ Student is AT RISK")
else:
    print("✅ Student is NOT at risk")
