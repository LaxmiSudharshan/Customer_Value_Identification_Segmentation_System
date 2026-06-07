import pandas as pd
import numpy as np

np.random.seed(42)

n = 30000

data = {
    "customer_id": [f"C{i:04d}" for i in range(1, n + 1)],

    "age": np.random.randint(21, 65, n),

    "monthly_income": np.random.randint(25000, 250000, n),

    "loan_amount": np.random.randint(50000, 2000000, n),

    "emi_total": np.random.randint(12, 120, n),

    "years_with_company": np.random.randint(1, 15, n),

    "monthly_transactions": np.random.randint(5, 120, n),

    "credit_score": np.random.randint(550, 900, n),

    "credit_utilization": np.random.randint(10, 95, n),

    "late_payment_count": np.random.randint(0, 12, n),

    "savings_amount": np.random.randint(5000, 1000000, n),

    "avg_account_balance": np.random.randint(10000, 1500000, n)
}

df = pd.DataFrame(data)

df["emi_paid"] = [
    np.random.randint(
        max(1, total - 12),
        total + 1
    )
    for total in df["emi_total"]
]

df.to_csv(
    "dataset/customers.csv",
    index=False
)

print("Dataset created successfully")
print(df.head())
print("\nRows:", len(df))