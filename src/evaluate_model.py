# from sklearn.metrics import classification_report
# from sklearn.metrics import confusion_matrix


# def evaluate(model, X_test, y_test):

#     y_pred = model.predict(X_test)

#     print("\nClassification Report:\n")

#     print(classification_report(y_test, y_pred))

#     print("\nConfusion Matrix:\n")

#     print(confusion_matrix(y_test, y_pred))
















from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve

from src.cost_function import calculate_cost

import matplotlib.pyplot as plt


def evaluate(

    model,
    X_test,
    y_test,
    feature_names

):

    # Predictions
    y_pred = model.predict(X_test)

    # Probability scores
    y_prob = model.predict_proba(X_test)[:, 1]

    # Classification Report
    print("\nClassification Report:\n")

    print(classification_report(y_test, y_pred))

    # Confusion Matrix
    print("\nConfusion Matrix:\n")

    print(confusion_matrix(y_test, y_pred))

    # ROC AUC
    auc_score = roc_auc_score(y_test, y_prob)

    print("\nROC AUC Score:", auc_score)

    # Business Cost
    cost = calculate_cost(
        y_test.values,
        y_pred
    )

    print("\nBusiness Cost:", cost)

    # ROC Curve
    fpr, tpr, _ = roc_curve(
        y_test,
        y_prob
    )

    plt.figure(figsize=(8, 6))

    plt.plot(fpr, tpr)

    plt.xlabel("False Positive Rate")

    plt.ylabel("True Positive Rate")

    plt.title("ROC Curve")

    plt.show()

    # Feature Importance
    importance = model.feature_importances_

    plt.figure(figsize=(10, 6))

    plt.barh(feature_names, importance[:len(feature_names)])

    plt.xlabel("Importance")

    plt.title("Feature Importance")

    plt.show()