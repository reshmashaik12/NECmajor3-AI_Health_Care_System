import numpy as np
import joblib

def test_diabetes_model():

    model = joblib.load(
        "models/disease_prediction/diabetes_model.pkl"
    )

    sample = np.array([[2,120,70,20,85,28.5,0.35,25]])

    pred = model.predict(sample)

    assert pred is not None
    print("Diabetes Model Test Passed")


def test_heart_model():

    model = joblib.load(
        "models/disease_prediction/heart_model.pkl"
    )

    sample = np.array([[55,1,2,145,250,1,130,1]])

    pred = model.predict(sample)

    assert pred is not None
    print("Heart Model Test Passed")


def test_kidney_model():

    model = joblib.load(
        "models/disease_prediction/kidney_model.pkl"
    )

    sample = np.array([[60,80,1.020,0,0,100,25,1.0,15.0]])

    pred = model.predict(sample)

    assert pred is not None
    print("Kidney Model Test Passed")


if __name__ == "__main__":

    test_diabetes_model()
    test_heart_model()
    test_kidney_model()