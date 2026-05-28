# import pandas as pd
# from sklearn.preprocessing import StandardScaler
# from sklearn.preprocessing import LabelEncoder


# def load_data(path):

#     df = pd.read_csv(path)

#     return df


# def preprocess_data(df):

#     # Drop ID column
#     df = df.drop("transaction_id", axis=1)

#     # Scale numerical columns
#     scaler = StandardScaler()

#     numerical_cols = [
#         'amount',
#         'transaction_hour',
#         'device_trust_score',
#         'velocity_last_24h',
#         'cardholder_age'
#     ]

#     df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

#     # Encode categorical column
#     encoder = LabelEncoder()

#     df['merchant_category'] = encoder.fit_transform(
#         df['merchant_category']
#     )

#     # Features and target
#     X = df.drop("is_fraud", axis=1)

#     y = df["is_fraud"]

#     return X, y






import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder


def load_data(path):

    df = pd.read_csv(path)

    return df


def preprocess_data(df):

    # Remove ID column
    df = df.drop("transaction_id", axis=1)

    # Scale numerical columns
    scaler = StandardScaler()

    numerical_cols = [
        'amount',
        'transaction_hour',
        'device_trust_score',
        'velocity_last_24h',
        'cardholder_age'
    ]

    df[numerical_cols] = scaler.fit_transform(
        df[numerical_cols]
    )

    # Encode categorical columns
    encoder = LabelEncoder()

    df['merchant_category'] = encoder.fit_transform(
        df['merchant_category']
    )

    # Features and target
    X = df.drop("is_fraud", axis=1)

    y = df["is_fraud"]

    return X, y