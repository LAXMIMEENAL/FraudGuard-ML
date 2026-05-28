from flask import Flask
from flask import request
from flask import jsonify

import joblib
import numpy as np
import pandas as pd
import os

app = Flask(__name__)

# Get current directory
BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

# Model path
model_path = os.path.join(
    BASE_DIR,
    "..",
    "models",
    "fraud_model.pkl"
)

# Preprocessor path
preprocessor_path = os.path.join(
    BASE_DIR,
    "..",
    "models",
    "preprocessor.pkl"
)

# Load preprocessor
preprocessor = joblib.load(
    preprocessor_path
)

# Load model
model = joblib.load(
    model_path
)


@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    try:

        # Convert incoming JSON into DataFrame
        features_df = pd.DataFrame([{

            'amount':
            data['amount'],

            'transaction_hour':
            data['transaction_hour'],

            'merchant_category':
            data['merchant_category'],

            'foreign_transaction':
            data['foreign_transaction'],

            'location_mismatch':
            data['location_mismatch'],

            'device_trust_score':
            data['device_trust_score'],

            'velocity_last_24h':
            data['velocity_last_24h'],

            'cardholder_age':
            data['cardholder_age']

        }])

        # Apply preprocessing
        processed_features = preprocessor.transform(
            features_df
        )

        # Predict probability
        probability = model.predict_proba(
            processed_features
        )[0][1]

        # Threshold
        THRESHOLD = 0.6

        prediction = (
    1   if risk_score > 60 else 0
)

        # Risk score
        risk_score = probability * 100


        # Rule-based risk boosting

        if data['amount'] >= 100000:

            risk_score += 25

        if data['foreign_transaction'] == "Yes":

            risk_score += 15

        if data['location_mismatch'] == "Yes":

            risk_score += 20

        if data['device_trust_score'] < 20:

            risk_score += 20

        if data['velocity_last_24h'] > 20:

            risk_score += 15

# Cap at 100
        risk_score = min(risk_score, 100)

        # Return response
        return jsonify({

            "prediction":
            int(prediction),

            "fraud_probability":
            float(probability),

            "risk_score":
            float(risk_score)

        })

    except Exception as e:

        return jsonify({

            "error":
            str(e)

        }), 500


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )