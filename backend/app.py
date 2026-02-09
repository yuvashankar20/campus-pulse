from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app)   # 🔥 THIS LINE FIXES DASHBOARD ISSUE

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(BASE_DIR, "data", "student_satisfaction.csv")

df = pd.read_csv(csv_path)

@app.route("/")
def home():
    return jsonify({"message": "Campus Pulse API is running"})

@app.route("/data")
def get_data():
    facility = request.args.get("facility")
    if facility:
        df_filtered = df[df["facility_rated"] == facility]
        return jsonify(df_filtered.to_dict(orient="records"))
    return jsonify(df.to_dict(orient="records"))

@app.route("/metrics")
def metrics():
    avg_score = round(df["satisfaction_score"].mean(), 2)
    facility_avg = df.groupby("facility_rated")["satisfaction_score"].mean().round(2).to_dict()

    return jsonify({
        "overall_average": avg_score,
        "average_by_facility": facility_avg,
        "best_facility": max(facility_avg, key=facility_avg.get),
        "worst_facility": min(facility_avg, key=facility_avg.get)
    })

if __name__ == "__main__":
    app.run(debug=True)
