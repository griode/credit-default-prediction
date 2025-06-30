import streamlit as st

from src.inputs import get_user_input
from src.shap_tools import explain_prediction
from src.utils import load_pipeline, make_prediction


st.set_page_config(page_title="Prédiction Défaut Crédit", page_icon="💳")
st.title("📉 Score de Risque de Défaut")

# Chargement du modèle
pipeline = load_pipeline()

# Données utilisateur (formulaire)
input_df = get_user_input()

# Prédiction
proba, prediction = make_prediction(pipeline, input_df)

st.write(f"Probabilité de défaut : **{proba:.2%}**")
st.write("Prédiction :", "❌ Risque élevé" if prediction else "✅ Risque faible")

# Interprétation
st.subheader("🔍 Interprétation du modèle")
explain_prediction(pipeline, input_df)
