import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

BASE_DIR = os.path.dirname(__file__)

# ---------------- DIABETES ----------------
df = pd.read_csv("datasets/diabetes.csv")

X = df.drop("Outcome", axis=1)
y = df["Outcome"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

joblib.dump(model, os.path.join(BASE_DIR, "diabetes_model.pkl"))

print("Diabetes model trained")

# ---------------- HEART ----------------
df = pd.read_csv("datasets/heart_disease.csv")

X = df.drop("HeartDisease", axis=1)
y = df["HeartDisease"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

joblib.dump(model, os.path.join(BASE_DIR, "heart_model.pkl"))

print("Heart model trained")

# ---------------- KIDNEY ----------------
df = pd.read_csv("datasets/kidney_disease.csv")

X = df.drop("CKD", axis=1)
y = df["CKD"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

joblib.dump(model, os.path.join(BASE_DIR, "kidney_model.pkl"))

print("Kidney model trained")