import pandas as pd
import os

print("EDA started")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(BASE_DIR, "data", "student_satisfaction.csv")

df = pd.read_csv(csv_path)

print("Data loaded")
print("Rows:", len(df))
print("Columns:", df.columns.tolist())

# Basic stats
print("\nSatisfaction score distribution:")
print(df["satisfaction_score"].value_counts().sort_index())

print("\nAverage score by facility:")
print(df.groupby("facility_rated")["satisfaction_score"].mean())

print("\nAverage score by academic year:")
print(df.groupby("academic_year")["satisfaction_score"].mean())

# Save summary to CSV (proof of EDA)
summary_path = os.path.join(BASE_DIR, "data", "eda_summary.csv")
df.groupby("facility_rated")["satisfaction_score"].mean().to_csv(summary_path)

print("\nEDA completed successfully")
print("Summary saved to:", summary_path)
