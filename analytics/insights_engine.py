import pandas as pd


def generate_insights(df):

    print("\nCUSTOMER VALUE INSIGHTS\n")

    print("Mean CVI:", round(df["cvi"].mean(), 2))

    print("Median CVI:", round(df["cvi"].median(), 2))

    print("Mode CVI:", round(df["cvi"].mode()[0], 2))

    print("Standard Deviation:", round(df["cvi"].std(), 2))

    print("\n")

    top_1_percent = df["cvi"].quantile(0.99)

    bottom_1_percent = df["cvi"].quantile(0.01)

    print("Top 1% CVI Threshold:", round(top_1_percent, 2))

    print("Bottom 1% CVI Threshold:", round(bottom_1_percent, 2))

    vip_count = len(
        df[df["cvi"] >= top_1_percent]
    )

    risk_count = len(
        df[df["cvi"] <= bottom_1_percent]
    )

    print("\nVIP Customers:", vip_count)

    print("Risk Customers:", risk_count)


def identify_outliers(df):

    cvi_mean = df["cvi"].mean()

    cvi_std = df["cvi"].std()

    df["cvi_zscore"] = (
        df["cvi"] - cvi_mean
    ) / cvi_std

    vip_customers = df[
        df["cvi_zscore"] > 3
    ]

    risk_customers = df[
        df["cvi_zscore"] < -3
    ]

    print("\nSTATISTICAL OUTLIERS\n")

    print(
        "Exceptional Customers:",
        len(vip_customers)
    )

    print(
        "High Risk Customers:",
        len(risk_customers)
    )

    return df


def assign_customer_category(cvi):

    if cvi >= 6.76:
        return "VIP"

    elif cvi >= 3:
        return "High Value"

    elif cvi >= 0:
        return "Average"

    elif cvi >= -3:
        return "Low Value"

    return "Risk"