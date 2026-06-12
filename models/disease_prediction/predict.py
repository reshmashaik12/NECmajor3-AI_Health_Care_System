import numpy as np
import joblib
import os

BASE_DIR = os.path.dirname(__file__)

diabetes_model = joblib.load(os.path.join(BASE_DIR, "diabetes_model.pkl"))
heart_model = joblib.load(os.path.join(BASE_DIR, "heart_model.pkl"))
kidney_model = joblib.load(os.path.join(BASE_DIR, "kidney_model.pkl"))


def predict_diabetes(data):
    data = np.array(data).reshape(1, -1)
    return diabetes_model.predict(data)[0]


def predict_heart(data):
    data = np.array(data).reshape(1, -1)
    return heart_model.predict(data)[0]


def predict_kidney(data):
    data = np.array(data).reshape(1, -1)
    return kidney_model.predict(data)[0]