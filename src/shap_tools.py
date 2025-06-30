import shap
from streamlit.components.v1 import html

def explain_prediction(pipeline, input_df):
    model = pipeline.named_steps["classifier"]
    preprocessor = pipeline.named_steps["preprocessor"]
    X_transformed = preprocessor.transform(input_df)

    try:
        feature_names = preprocessor.get_feature_names_out()
    except AttributeError:
        feature_names = input_df.columns

    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_transformed)

    instance = X_transformed[0]
    if hasattr(instance, "toarray"):
        instance = instance.toarray().flatten()

    force_plot = shap.force_plot(
        explainer.expected_value, shap_values[0], instance, feature_names=feature_names
    )
    shap_html = f"<head>{shap.getjs()}</head><body>{force_plot.html()}</body>"
    html(shap_html, height=200)
