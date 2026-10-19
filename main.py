
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load data from the CSV file
df = pd.read_csv("student.csv")

# 2. Display the project title
print("=" * 45)
print("STUDENT STUDY DATA ANALYZER")
print("=" * 45)

# 3. Display the student records
print("\n--- Student Records ---")
print(df)

# 4. Display the first five student records
print("\n--- First Five Students ---")
print(df.head())

# 5. Display basic information about the dataset
print("\n--- Dataset Information ---")
df.info()

# 6. Inspect the data

print("\n--- Missing Values ---")
print(df.isnull().sum())

# 7. Clean the data

# Remove Duplicate row 
df = df.drop_duplicates()

# Convert numeric columns to numbers.
# Invalid text values become missing values.
df["Study_Hours"] = pd.to_numeric(
    df["Study_Hours"], errors="coerce"
)

df["Exam_Score"] = pd.to_numeric(
    df["Exam_Score"], errors="coerce"
)

# Remove rows missing student names or exam scores
df = df.dropna(subset=["Student", "Exam_Score"])

# Fill missing study hours with the average
if df["Study_Hours"].notna().any():
    df["Study_Hours"] = df["Study_Hours"].fillna(
        df["Study_Hours"].mean()
    )

print("\n--- Cleaned Student Data ---")
print(df)

print("\n--- Missing Values After Cleaning ---")
print(df.isnull().sum())

# 8. Analyze study hours
print("\n--- Study Hours Analysis ---")
print("Total study hours:", df["Study_Hours"].sum())
print("Average study hours:", df["Study_Hours"].mean())
print("Highest study hours:", df["Study_Hours"].max())
print("Lowest study hours:", df["Study_Hours"].min())

# 9. Analyze exam scores
print("\n--- Exam Score Analysis ---")
print("Average exam score:", df["Exam_Score"].mean())
print("Highest exam score:", df["Exam_Score"].max())
print("Lowest exam score:", df["Exam_Score"].min())

# 10. Create a bar chart

if not df.empty:
    average_score = df["Exam_Score"].mean()

    plt.figure(figsize=(8, 5))

    plt.bar(df["Student"], df["Exam_Score"])
    plt.axhline(
        y=average_score, 
        color="r", 
        linestyle="--", 
        label=f"Average Score: {average_score:.2f}")

    plt.title("Student Exam Scores")
    plt.xlabel("Students")
    plt.ylabel("Exam Scores")
    plt.legend()    
    plt.tight_layout()

    # Save the bar chart as an image file
    plt.savefig("exam_scores_chart.png")
    print("\nBar chart saved as 'exam_scores_chart.png'.")

    #Display the bar chart
    plt.show()
else:
    print("\nNo valid exam data available for charting.")
  

# 11. Find students scoring 70 or above
print("\n--- Students Scoring 70 or Above ---")
high_scorers = df[df["Exam_Score"] >= 70]
print(high_scorers)

# 12. Find students scoring below 50
print("\n--- Students Scoring Below 50 ---")
low_scorers = df[df["Exam_Score"] < 50]
print(low_scorers)

print("\nAnalysis completed!")
