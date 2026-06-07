import pandas as pd

from analytics.value_engine import calculate_customer_value

from analytics.segment_engine import segment_customers

from analytics.insights_engine import (
    generate_insights,
    identify_outliers,
    assign_customer_category
)

df = pd.read_csv(
    "dataset/customers.csv"
)

df = calculate_customer_value(df)

df = segment_customers(df)

generate_insights(df)

df = identify_outliers(df)

df["customer_category"] = df["cvi"].apply(
    assign_customer_category
)

print("\nCUSTOMER CATEGORY DISTRIBUTION\n")

print(
    df["customer_category"].value_counts()
)

print("\nTOP 10 OUTLIERS\n")

print(
    df.sort_values(
        by="cvi_zscore",
        ascending=False
    )[
        [
            "customer_id",
            "cvi",
            "cvi_zscore",
            "customer_category"
        ]
    ].head(10)
)

top_customers = df.sort_values(
    by="cvi",
    ascending=False
)

print("\nTOP 20 MOST VALUABLE CUSTOMERS\n")

print(
    top_customers[
        [
            "customer_id",
            "customer_category",
            "cvi",
            "monthly_income",
            "credit_score",
            "late_payment_count"
        ]
    ].head(20)
)

df.to_csv(
    "customer_value_analysis.csv",
    index=False
)

print(
    "\ncustomer_value_analysis.csv exported successfully"
)