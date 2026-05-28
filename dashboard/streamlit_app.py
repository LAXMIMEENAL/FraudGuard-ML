
import streamlit as st
import pandas as pd
import joblib
import os
import matplotlib.pyplot as plt
import numpy as np

# Base directory
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

# Load model
model = joblib.load(model_path)

# Load preprocessor
preprocessor = joblib.load(
    preprocessor_path
)

# Streamlit config
st.set_page_config(
    page_title="FraudGuard ML",
    layout="centered"
)

st.title("FraudGuard ML")

st.subheader(
    "Real-Time Fraud Detection Platform"
)

st.write(
    "Analyze financial transaction risk."
)

# User Inputs
amount = st.number_input(
    "Transaction Amount",
    min_value=0.0
)

transaction_hour = st.slider(
    "Transaction Hour",
    0,
    23,
    12
)

merchant_category = st.selectbox(
    "Merchant Category",
    [
        "Food",
        "Travel",
        "Electronics",
        "Healthcare",
        "Luxury",
        "Grocery"
    ]
)

foreign_transaction = st.selectbox(
    "Foreign Transaction",
    ["Yes", "No"]
)

location_mismatch = st.selectbox(
    "Location Mismatch",
    ["Yes", "No"]
)

device_trust_score = st.slider(
    "Device Trust Score",
    0,
    100,
    50
)

velocity_last_24h = st.slider(
    "Transaction Velocity (24h)",
    0,
    50,
    5
)

cardholder_age = st.slider(
    "Cardholder Age",
    18,
    90,
    30
)

# Prediction
if st.button("Analyze Transaction"):

    # Create DataFrame
    features_df = pd.DataFrame([{

        'amount':
        amount,

        'transaction_hour':
        transaction_hour,

        'merchant_category':
        merchant_category,

        'foreign_transaction':
        foreign_transaction,

        'location_mismatch':
        location_mismatch,

        'device_trust_score':
        device_trust_score,

        'velocity_last_24h':
        velocity_last_24h,

        'cardholder_age':
        cardholder_age

    }])

    # Apply preprocessing
    processed_features = preprocessor.transform(
        features_df
    )

    # Predict probability
    probability = model.predict_proba(
        processed_features
    )[0][1]

    # THRESHOLD = 0.6

    
    risk_score = probability * 100

    if amount >= 1000000:

        risk_score += 50

    elif amount >= 500000:

        risk_score += 40

    elif amount >= 100000:

        risk_score += 30

    elif amount >= 50000:

        risk_score += 20

    if foreign_transaction == "Yes":

        risk_score += 15

    if location_mismatch == "Yes":

        risk_score += 20

    if device_trust_score < 20:

        risk_score += 20

    if velocity_last_24h > 20:

        risk_score += 15
    
    if transaction_hour >= 1 and transaction_hour <= 5:

        risk_score += 10



    if merchant_category == "Luxury":

        risk_score += 25

    elif merchant_category == "Electronics":

        risk_score += 20

    elif merchant_category == "Travel":

        risk_score += 15

    elif merchant_category == "Healthcare":

        risk_score += 5


# Young high-value anomaly
    if cardholder_age < 21 and amount > 50000:

        risk_score += 10
# Cap maximum score
    risk_score = min(risk_score, 100)




    # -----------------------------
# Explainable AI
# -----------------------------

    reasons = []


# Amount explanation
    if amount >= 1000000:

        reasons.append(
         "Extremely high transaction amount"
        )

    elif amount >= 100000:

        reasons.append(
        "High transaction amount"
        )


# Foreign transaction
    if foreign_transaction == "Yes":

        reasons.append(
        "Foreign transaction detected"
        )


# Location mismatch
    if location_mismatch == "Yes":

        reasons.append(
        "Location mismatch detected"
    )


# Low device trust
    if device_trust_score < 20:

        reasons.append(
        "Low device trust score"
        )


# High transaction velocity
    if velocity_last_24h > 20:

        reasons.append(
         "High transaction frequency"
        )


# Suspicious transaction hour
    if transaction_hour >= 1 and transaction_hour <= 5:

        reasons.append(
        "Late-night suspicious transaction"
    )


# Merchant category risk
    if merchant_category == "Luxury":

      reasons.append(
         "Luxury merchant category"
        )

    elif merchant_category == "Electronics":

        reasons.append(
        "Electronics merchant risk"
        )
    


    prediction = (
        1 if risk_score > 60 else 0
    )


    

    st.subheader("Prediction Result")




    if risk_score > 85:

        st.error(

            f"HIGH RISK TRANSACTION\n\n"
            f"Risk Score: {risk_score:.2f}%"

        )

    elif risk_score > 60:

        st.warning(

            f"SUSPICIOUS TRANSACTION\n\n"
            f"Risk Score: {risk_score:.2f}%"

        )

    elif risk_score > 40:

        st.info(

            f"MEDIUM RISK TRANSACTION\n\n"
            f"Risk Score: {risk_score:.2f}%"

        )

    else:

        st.success(

            f"LOW RISK TRANSACTION\n\n"
            f"Risk Score: {risk_score:.2f}%"

        )
    

    # Progress bar
    st.progress(
        int(risk_score)
    )


    # -----------------------------
# Explainable AI Output
# -----------------------------

    st.subheader("Why This Transaction Was Flagged")

    if len(reasons) > 0:

        for reason in reasons:

          st.write(f"• {reason}")

    else:

        st.write(
          "No major fraud indicators detected."
      )









# Risk interpretation
    st.subheader("Risk Interpretation")


    if risk_score > 85:

        st.write(
         "Transaction should be BLOCKED immediately."
        )

    elif risk_score > 60:

        st.write(
            "OTP Verification Recommended."
        )

    elif risk_score > 40:

        st.write(
          "Manual Review Recommended."
        )

    else:

        st.write(
            "Transaction appears safe."
        )



st.subheader("Fraud Risk Analytics")


# Generate sample risk data
sample_risk_scores = np.random.normal(
    loc=55,
    scale=20,
    size=100
)

sample_risk_scores = np.clip(
    sample_risk_scores,
    0,
    100
)


# Histogram
fig, ax = plt.subplots(figsize=(8, 4))

ax.hist(
    sample_risk_scores,
    bins=10
)

ax.set_xlabel("Risk Score")

ax.set_ylabel("Transaction Count")

ax.set_title("Fraud Risk Distribution")

st.pyplot(fig)


# Fraud statistics
high_risk = np.sum(sample_risk_scores > 80)

medium_risk = np.sum(
    (sample_risk_scores > 40) &
    (sample_risk_scores <= 80)
)

low_risk = np.sum(sample_risk_scores <= 40)


st.subheader("Fraud Statistics")

st.write(f"High Risk Transactions: {high_risk}")

st.write(f"Medium Risk Transactions: {medium_risk}")

st.write(f"Low Risk Transactions: {low_risk}")



# -----------------------------
# Simulated Fraud Locations
# -----------------------------

st.subheader("Fraud Location Heatmap")


# Sample coordinates
map_data = pd.DataFrame({

    'lat': np.random.uniform(
        8.0,
        37.0,
        50
    ),

    'lon': np.random.uniform(
        68.0,
        97.0,
        50
    )

})

st.map(map_data)