
# from sklearn.model_selection import train_test_split
# from xgboost import XGBClassifier
# from imblearn.over_sampling import SMOTE
# import joblib
# import os


# def train(X, y):

#     X_train, X_test, y_train, y_test = train_test_split(
#         X,
#         y,
#         test_size=0.2,
#         random_state=42
#     )

#     # Handle imbalance
#     smote = SMOTE(random_state=42)

#     X_train, y_train = smote.fit_resample(
#         X_train,
#         y_train
#     )

#     # XGBoost model
#     model = XGBClassifier(
#         n_estimators=200,
#         max_depth=6,
#         learning_rate=0.1,
#         scale_pos_weight=10,
#         eval_metric='logloss'
#     )

#     model.fit(X_train, y_train)

#     os.makedirs("models", exist_ok=True)

#     joblib.dump(
#         model,
#         "models/fraud_model.pkl"
#     )

#     return model, X_test, y_test


from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder

from xgboost import XGBClassifier
from imblearn.over_sampling import SMOTE

import pandas as pd
import joblib
import os


def train(df):

    # Features and target
    X = df.drop(
        ["transaction_id", "is_fraud"],
        axis=1
    )

    y = df["is_fraud"]

    # Column groups
    numeric_features = [
        'amount',
        'transaction_hour',
        'device_trust_score',
        'velocity_last_24h',
        'cardholder_age'
    ]

    categorical_features = [
        'merchant_category',
        'foreign_transaction',
        'location_mismatch'
    ]

    # Preprocessing
    preprocessor = ColumnTransformer(

        transformers=[

            (
                'num',
                StandardScaler(),
                numeric_features
            ),

            (
                'cat',
                OneHotEncoder(
                    handle_unknown='ignore'
                ),
                categorical_features
            )

        ]

    )

    # Model
    model = XGBClassifier(

        n_estimators=200,
        max_depth=6,
        learning_rate=0.1,
        scale_pos_weight=10,
        eval_metric='logloss'
    )

    # Full pipeline
    pipeline = Pipeline([

        ('preprocessor', preprocessor),

        ('classifier', model)

    ])

    # Split
    X_train, X_test, y_train, y_test = train_test_split(

        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Apply preprocessing first
    X_train_processed = preprocessor.fit_transform(
        X_train
    )

    X_test_processed = preprocessor.transform(
        X_test
    )

    # SMOTE
    smote = SMOTE(random_state=42)

    X_train_smote, y_train_smote = smote.fit_resample(
        X_train_processed,
        y_train
    )

    # Train model
    model.fit(
        X_train_smote,
        y_train_smote
    )

    # Save both
    os.makedirs("models", exist_ok=True)

    joblib.dump(
        preprocessor,
        "models/preprocessor.pkl"
    )

    joblib.dump(
        model,
        "models/fraud_model.pkl"
    )

    return (
        model,
        preprocessor,
        X_test,
        y_test
    )