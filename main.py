import numpy as np

# 1. Sample student data
students = np.array(["A", "B", "C", "D", "E"])
study_hours = np.array([2, 4, 9, 7, 3])
exam_scores = np.array([55, 68, 96, 88, 62])

# 2. Display the original data
print("=" * 40)
print("STUDENT STUDY DATA ANALYZER")
print("=" * 40)

print("\nStudent Records:")
for i in range(len(students)):
    print(
        f"Student {students[i]}: "
        f"{study_hours[i]} study hours, "
        f"{exam_scores[i]} exam score"
    )

# 3. Calculate statistics
print("\n--- Study Statistics ---")
print("Total study hours:", np.sum(study_hours))
print("Average study hours:", np.mean(study_hours))
print("Highest study hours:", np.max(study_hours))
print("Lowest study hours:", np.min(study_hours))

print("\n--- Exam Statistics ---")
print("Average exam score:", np.mean(exam_scores))
print("Highest exam score:", np.max(exam_scores))
print("Lowest exam score:", np.min(exam_scores))

# 4. Find students scoring 70 or above
print("\n--- Students Scoring 70 or Above ---")
passed = exam_scores >= 70

for i in range(len(students)):
    if passed[i]:
        print(f"Student {students[i]}: {exam_scores[i]}")

# 5. Simulate adding one study hour
print("\n--- Study Hours After Adding One Hour ---")
new_study_hours = study_hours + 1
print(new_study_hours)

print("\nAnalysis completed!")
