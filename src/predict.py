# import joblib

# model = joblib.load("models/fraud_model.pkl")

# def predict_transaction(data):

#     prediction = model.predict(data)

#     probability = model.predict_proba(data)

#     return prediction,probability

import joblib
import numpy as np

model = joblib.load("models/fraud_model.pkl")


def predict_risk(features):

    data = np.array(features).reshape(1, -1)

    probability = model.predict_proba(data)[0][1]

    risk_score = probability * 100

    THRESHOLD = 0.6

    prediction = (
    "Fraud"
    if probability > THRESHOLD
    else "Legitimate"
    )
    return prediction, risk_score