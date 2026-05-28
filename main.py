
# from src.data_preprocessing import (
#     load_data,
#     preprocess_data
# )

# from src.train_model import train

# from src.evaluate_model import evaluate


# # Dataset path
# path = "data/raw/creditcard.csv"

# # Load data
# df = load_data(path)

# print("\nDataset Loaded Successfully")

# print(df.head())

# # Preprocessing
# X, y = preprocess_data(df)

# print("\nPreprocessing Completed")

# # Training
# model, X_test, y_test = train(X, y)

# print("\nModel Training Completed")

# # Evaluation
# evaluate(model, X_test, y_test)


import pandas as pd

from src.train_model import train
from src.evaluate_model import evaluate


# Dataset path
path = "data/raw/creditcard.csv"

# Load dataset
df = pd.read_csv(path)

print("\nDataset Loaded Successfully")

print(df.head())

# Train
model, preprocessor, X_test, y_test = train(df)

print("\nModel Training Completed")

# Transform test data
X_test_processed = preprocessor.transform(
    X_test
)

# Evaluate
feature_names = [

    'amount',
    'transaction_hour',
    'device_trust_score',
    'velocity_last_24h',
    'cardholder_age'

]

evaluate(

    model,
    X_test_processed,
    y_test,
    feature_names

)