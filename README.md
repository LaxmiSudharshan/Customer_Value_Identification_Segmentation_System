# Customer Value Identification & Segmentation System

## Overview

The Customer Value Identification & Segmentation System is a data analytics project designed to identify the most valuable and high-risk customers based on their financial behavior.

Instead of ranking customers using a single factor such as income or credit score, this project evaluates multiple financial indicators and creates a Customer Value Index (CVI) to measure overall customer value. Statistical techniques such as Z-score normalization, ratio analysis, and customer segmentation are used to compare customers fairly and identify exceptional customers and risk customers.

The results are presented through an interactive Power BI dashboard that provides business insights for customer management, lending decisions, customer retention, and premium customer targeting.

---

## Problem Statement

Financial institutions and businesses often have thousands of customers with different financial behaviors. Identifying which customers provide the highest value and which customers require attention can be challenging when relying on raw financial data.

This project aims to:

- Identify high-value customers (VIPs)
- Identify high-risk customers
- Compare customers using standardized metrics
- Detect statistically exceptional customers
- Support data-driven business decision making

---

## Objectives

- Build a Customer Value Index (CVI)
- Analyze customer financial behavior
- Perform statistical customer evaluation
- Detect outliers using Z-score analysis
- Segment customers into meaningful categories
- Create an interactive Power BI dashboard

---

## Dataset

The project uses a synthetic dataset containing **30,000 customer records**.

### Features

| Feature | Description |
|----------|-------------|
| customer_id | Unique customer identifier |
| age | Customer age |
| monthly_income | Monthly income |
| loan_amount | Total loan amount |
| emi_paid | EMI paid |
| emi_total | Total EMI amount |
| avg_account_balance | Average account balance |
| monthly_transactions | Monthly transaction count |
| years_with_company | Customer relationship duration |
| credit_score | Customer credit score |
| credit_utilization | Credit utilization percentage |
| late_payment_count | Number of late payments |
| savings_amount | Total savings amount |

---

## Methodology

### 1. Financial Ratio Analysis

Several financial ratios were calculated to evaluate customer behavior.

Examples include:

- Repayment Ratio
- Savings Ratio
- Balance Ratio
- Loyalty Ratio
- Risk Ratio

These ratios help standardize financial performance across customers.

---

### 2. Z-Score Normalization

To fairly compare customers with different financial profiles, Z-score normalization was applied.

Z-score formula:

\[
Z = \frac{X-\mu}{\sigma}
\]

Where:

- X = Customer value
- μ = Mean
- σ = Standard deviation

This allows customers to be compared relative to the overall population.

---

### 3. Customer Value Index (CVI)

A Customer Value Index (CVI) was developed by combining multiple financial indicators.

The CVI represents the overall value of a customer based on:

- Income
- Credit Score
- Savings
- Account Balance
- Transaction Activity
- Repayment Behavior
- Customer Loyalty

---

### 4. Customer Segmentation

Customers were segmented into categories:

| Category | Description |
|----------|-------------|
| VIP | Top-performing customers |
| High Value | Above-average customers |
| Average | Normal customers |
| Low Value | Below-average customers |
| Risk | High-risk customers |

---

### 5. Statistical Outlier Detection

Customers were analyzed using Z-scores to identify:

- Exceptional customers
- High-risk customers
- Statistical outliers

Outlier thresholds:

```text
Z-score > 3     → Exceptional Customer
Z-score < -3    → High Risk Customer
```

---

## Technologies Used

### Programming

- Python

### Libraries

- Pandas
- NumPy
- Scikit-Learn

### Visualization

- Power BI

---

## Project Structure

```text
Customer_Value_Identification_Segmentation_System
│
├── analytics/
│   ├── value_engine.py
│   ├── segment_engine.py
│   └── insights_engine.py
│
├── dataset/
│   └── customers.csv
│
├── customer_value_analysis.csv
├── dataset_generator.py
├── main.py
├── requirements.txt
├── CVI_Segmentation_System_Dashboard.pbix
└── README.md
```

---

## Dashboard Pages

### Page 1 — Executive Overview

Provides a high-level summary of:

- Total Customers
- VIP Customers
- Risk Customers
- Average CVI
- Highest CVI

---

### Page 2 — Customer Intelligence

Analyzes:

- Credit Score vs Customer Value
- Income vs Customer Value
- Savings Analysis
- Average Financial Metrics by Category

---

### Page 3 — Risk Analysis

Analyzes:

- Late Payment Behavior
- Credit Utilization
- Risk Customer Monitoring
- High-Risk Customer Watchlist

---

### Page 4 — VIP Customer Analysis

Analyzes:

- Top Customers
- VIP Customer Characteristics
- Income Patterns
- Savings Patterns
- Financial Performance Comparison

---

## Key Insights Generated

The system helps answer business questions such as:

- Who are the most valuable customers?
- Which customers should receive premium offers?
- Which customers are likely to become risky?
- How does financial behavior affect customer value?
- What characteristics define VIP customers?

---

## Business Applications

This solution can be used in:

- Banking
- Financial Services
- Lending Companies
- Insurance Companies
- Customer Relationship Management
- Customer Retention Programs

---

## Results

The project successfully:

- Generated customer value scores
- Identified VIP customers
- Detected high-risk customers
- Performed statistical customer analysis
- Segmented customers into meaningful groups
- Built an interactive Power BI dashboard

---

## Future Improvements

Possible future enhancements include:

- Real-world banking datasets
- Machine Learning based customer prediction
- Customer Lifetime Value (CLV) prediction
- Loan Default Prediction
- Automated dashboard deployment
- Real-time customer monitoring

---

## Author

Laxmi Sudharshan

Data Analytics | Statistics | Power BI | Python
