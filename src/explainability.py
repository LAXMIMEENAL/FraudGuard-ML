import shap
import joblib

model = joblib.load("models/fraud_model.pkl")


def explain_model(X_sample):

    explainer = shap.Explainer(model)

    shap_values = explainer(X_sample)

    shap.plots.waterfall(shap_values[0])