import pandas as pd
import os

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Build absolute path to CSV
csv_path = os.path.join(BASE_DIR, "data", "student_satisfaction.csv")

print("Looking for CSV at:")
print(csv_path)

# Load CSV
df = pd.read_csv(csv_path)

# Verification
print("\nCSV loaded successfully")
print("Total rows:", len(df))
print("Columns:", list(df.columns))
print("\nFirst 5 rows:")
print(df.head())
