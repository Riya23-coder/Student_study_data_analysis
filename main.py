
import pandas as pd

# 1. Load data from the CSV file
df = pd.read_csv("student.csv")

# 2. Display the project title
print("=" * 45)
print("STUDENT STUDY DATA ANALYZER")
print("=" * 45)

# 3. Display the student records
print("\n--- Student Records ---")
print(df)

# 4. Display the first five rows
print("\n--- First Five Students ---")
print(df.head())

# 5. Display basic information about the dataset
print("\n--- Dataset Information ---")
df.info()

# 6. Analyze study hours
print("\n--- Study Hours Analysis ---")
print("Total study hours:", df["Study_Hours"].sum())
print("Average study hours:", df["Study_Hours"].mean())
print("Highest study hours:", df["Study_Hours"].max())
print("Lowest study hours:", df["Study_Hours"].min())

# 7. Analyze exam scores
print("\n--- Exam Score Analysis ---")
print("Average exam score:", df["Exam_Score"].mean())
print("Highest exam score:", df["Exam_Score"].max())
print("Lowest exam score:", df["Exam_Score"].min())

# 8. Find students scoring 70 or above
print("\n--- Students Scoring 70 or Above ---")
high_scorers = df[df["Exam_Score"] >= 70]
print(high_scorers)

# 9. Find students scoring below 50
print("\n--- Students Scoring Below 50 ---")
low_scorers = df[df["Exam_Score"] < 50]
print(low_scorers)

print("\nAnalysis completed!")
