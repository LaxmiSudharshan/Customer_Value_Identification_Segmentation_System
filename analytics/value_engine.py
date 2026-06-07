import pandas as pd


def z_score(series):

    return (
        series - series.mean()
    ) / series.std()


def calculate_customer_value(df):

    df["repayment_ratio"] = (
        df["emi_paid"] /
        df["emi_total"]
    )

    positive_features = [
        "monthly_income",
        "credit_score",
        "avg_account_balance",
        "savings_amount",
        "repayment_ratio",
        "years_with_company",
        "monthly_transactions"
    ]

    negative_features = [
        "late_payment_count",
        "credit_utilization"
    ]

    for col in positive_features:
        df[f"{col}_z"] = z_score(df[col])

    for col in negative_features:
        df[f"{col}_z"] = z_score(df[col])

    df["cvi"] = (

        df["monthly_income_z"] +

        df["credit_score_z"] +

        df["avg_account_balance_z"] +

        df["savings_amount_z"] +

        df["repayment_ratio_z"] +

        df["years_with_company_z"] +

        df["monthly_transactions_z"]

        -

        df["late_payment_count_z"]

        -

        df["credit_utilization_z"]

    )

    return df