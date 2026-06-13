import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# =========================
# CREATE OUTPUT DIRECTORY
# =========================

os.makedirs("output", exist_ok=True)

# =========================
# LOAD DATASET
# =========================

df = pd.read_csv(
    "data/shopping_trends_updated.csv"
)

print("\n===== DATASET INFORMATION =====")

print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

# =========================
# SUMMARY REPORT
# =========================

summary = pd.DataFrame({
    "Metric": [
        "Total Customers",
        "Total Revenue",
        "Average Purchase Amount"
    ],
    "Value": [
        len(df),
        df["Purchase Amount (USD)"].sum(),
        round(df["Purchase Amount (USD)"].mean(), 2)
    ]
})

summary.to_csv(
    "output/dashboard_summary.csv",
    index=False
)

print(summary)

# =========================
# CHART 1
# CATEGORY SALES
# =========================

category_sales = (
    df.groupby("Category")
    ["Purchase Amount (USD)"]
    .sum()
    .sort_values(
        ascending=False
    )
)

plt.figure(figsize=(10,5))

category_sales.plot(
    kind="bar"
)

plt.title(
    "Revenue by Product Category"
)

plt.ylabel(
    "Revenue (USD)"
)

plt.tight_layout()

plt.savefig(
    "output/category_sales_bar_chart.png"
)

plt.show()

# =========================
# CHART 2
# GENDER DISTRIBUTION
# =========================

gender_distribution = (
    df["Gender"]
    .value_counts()
)

plt.figure(figsize=(6,6))

gender_distribution.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title(
    "Gender Distribution"
)

plt.ylabel("")

plt.savefig(
    "output/gender_distribution_pie_chart.png"
)

plt.show()

# =========================
# CHART 3
# SEASONAL SALES
# =========================

season_sales = (
    df.groupby("Season")
    ["Purchase Amount (USD)"]
    .sum()
)

plt.figure(figsize=(8,5))

season_sales.plot(
    kind="line",
    marker="o"
)

plt.title(
    "Seasonal Revenue Trend"
)

plt.ylabel(
    "Revenue"
)

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "output/seasonal_sales_line_chart.png"
)

plt.show()

# =========================
# CHART 4
# PURCHASE AMOUNT HISTOGRAM
# =========================

plt.figure(figsize=(8,5))

plt.hist(
    df["Purchase Amount (USD)"],
    bins=20
)

plt.title(
    "Purchase Amount Distribution"
)

plt.xlabel(
    "Purchase Amount"
)

plt.ylabel(
    "Frequency"
)

plt.tight_layout()

plt.savefig(
    "output/purchase_amount_histogram.png"
)

plt.show()

# =========================
# CHART 5
# PURCHASE AMOUNT BOXPLOT
# =========================

plt.figure(figsize=(6,5))

plt.boxplot(
    df["Purchase Amount (USD)"]
)

plt.title(
    "Purchase Amount Box Plot"
)

plt.tight_layout()

plt.savefig(
    "output/purchase_amount_boxplot.png"
)

plt.show()

# =========================
# CHART 6
# TOP PRODUCTS
# =========================

top_products = (
    df["Item Purchased"]
    .value_counts()
    .head(10)
)

plt.figure(figsize=(10,5))

top_products.plot(
    kind="bar"
)

plt.title(
    "Top 10 Purchased Products"
)

plt.ylabel(
    "Purchase Count"
)

plt.tight_layout()

plt.savefig(
    "output/top_products_chart.png"
)

plt.show()

# =========================
# CHART 7
# AGE GROUP ANALYSIS
# =========================

df["Age Group"] = pd.cut(
    df["Age"],
    bins=[0,20,30,40,50,60,100],
    labels=[
        "0-20",
        "21-30",
        "31-40",
        "41-50",
        "51-60",
        "60+"
    ]
)

age_group_count = (
    df["Age Group"]
    .value_counts()
    .sort_index()
)

plt.figure(figsize=(8,5))

age_group_count.plot(
    kind="bar"
)

plt.title(
    "Customer Distribution by Age Group"
)

plt.ylabel(
    "Number of Customers"
)

plt.tight_layout()

plt.savefig(
    "output/age_group_chart.png"
)

plt.show()

# =========================
# CHART 8
# PAYMENT METHODS
# =========================

payment_methods = (
    df["Payment Method"]
    .value_counts()
)

plt.figure(figsize=(8,5))

payment_methods.plot(
    kind="bar"
)

plt.title(
    "Payment Method Usage"
)

plt.ylabel(
    "Number of Transactions"
)

plt.tight_layout()

plt.savefig(
    "output/payment_method_chart.png"
)

plt.show()

# =========================
# CHART 9
# SUBSCRIPTION STATUS
# =========================

subscription = (
    df["Subscription Status"]
    .value_counts()
)

plt.figure(figsize=(6,6))

subscription.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title(
    "Subscription Status"
)

plt.ylabel("")

plt.savefig(
    "output/subscription_status_chart.png"
)

plt.show()

# =========================
# SAVE REPORTS
# =========================

category_sales.to_csv(
    "output/category_sales.csv"
)

season_sales.to_csv(
    "output/season_sales.csv"
)

top_products.to_csv(
    "output/top_products.csv"
)

payment_methods.to_csv(
    "output/payment_methods.csv"
)

# =========================
# FINAL SUMMARY
# =========================

print("\n===== VISUALIZATION SUMMARY =====")

print(
    f"Total Revenue: ${df['Purchase Amount (USD)'].sum()}"
)

print(
    f"Average Purchase: ${round(df['Purchase Amount (USD)'].mean(),2)}"
)

print(
    f"Most Popular Product: {top_products.index[0]}"
)

print(
    f"Highest Revenue Category: {category_sales.index[0]}"
)

print(
    f"Most Used Payment Method: {payment_methods.index[0]}"
)

print("\nProject Completed Successfully!")