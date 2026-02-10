import pandas as pd

# Create student performance data
data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "attendance": [50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
    "previous_marks": [35, 40, 45, 50, 55, 60, 65, 70, 75, 85],
    "risk": [1, 1, 1, 1, 0, 0, 0, 0, 0, 0]  # 1 = At Risk, 0 = Safe
}

df = pd.DataFrame(data)

# Save dataset
df.to_csv("student_performance.csv", index=False)

print("Dataset created successfully")
print(df)
