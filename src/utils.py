import joblib
import numpy as np

def load_pipeline(path="model/xgboost_pipeline.pkl"):
    return joblib.load(path)

def make_prediction(pipeline, X):
    proba = pipeline.predict_proba(X)[0, 1]
    pred = int(proba >= 0.5)
    return proba, pred
