import streamlit as st
import pandas as pd

features = [
    "RevolvingUtilizationOfUnsecuredLines",
    "age",
    "DebtRatio",
    "MonthlyIncome",
    "NumberOfOpenCreditLinesAndLoans",
    "NumberRealEstateLoansOrLines",
    "NumberOfDependents",
    "NumberOfTime30-59DaysPastDueNotWorse",
    "NumberOfTime60-89DaysPastDueNotWorse",
    "NumberOfTimes90DaysLate"
]

def get_user_input():
    st.sidebar.header("🖊️ Saisir les données du client")
    data = {feature: st.sidebar.number_input(feature, min_value=0.0, value=0.0) for feature in features}
    df = pd.DataFrame([data])
    df["Unnamed: 0"] = 0
    df["TotalLatePayments"] = (
        df["NumberOfTime30-59DaysPastDueNotWorse"] +
        df["NumberOfTime60-89DaysPastDueNotWorse"] +
        df["NumberOfTimes90DaysLate"]
    )
    return df
