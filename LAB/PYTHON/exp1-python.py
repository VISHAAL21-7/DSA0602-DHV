import matplotlib.pyplot as plt
import numpy as np

# ---- Given dataset: Monthly Sales ----
months = ['January', 'February', 'March', 'April', 'May']
sales = [15000, 18000, 22000, 20000, 23000]

# ---- Task 2 needs "top-selling products" - not in the given table,
#      so a small supplementary product dataset is assumed here ----
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
product_sales = [42000, 35000, 51000, 28000, 39000]

# ---- Task 3 needs "advertising budget" - not in the given table,
#      so a plausible monthly budget series is assumed here ----
ad_budget = [2000, 2500, 3200, 2800, 3500]

# 1. Line chart - monthly sales trend
plt.figure(figsize=(7, 5))
plt.plot(months, sales, marker='o', color='steelblue')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales (in $)")
plt.tight_layout()
plt.show()

# 2. Bar chart - top-selling products for the year
plt.figure(figsize=(7, 5))
plt.bar(products, product_sales, color='darkorange')
plt.title("Top-Selling Products for the Year")
plt.xlabel("Product")
plt.ylabel("Annual Sales (in $)")
plt.tight_layout()
plt.show()

# 3. Scatter plot - advertising budget vs monthly sales
plt.figure(figsize=(7, 5))
plt.scatter(ad_budget, sales, color='crimson', s=80)
plt.title("Advertising Budget vs Monthly Sales")
plt.xlabel("Advertising Budget (in $)")
plt.ylabel("Sales (in $)")
plt.tight_layout()
plt.show()
# Insight: sales rise as ad budget rises, suggesting a positive relationship
# between advertising spend and revenue (correlation, not proof of causation).

# 4. Combined dashboard - line chart + bar chart together
fig, axes = plt.subplots(1, 2, figsize=(13, 5))
axes[0].plot(months, sales, marker='o', color='steelblue')
axes[0].set_title("Monthly Sales Trend")
axes[0].set_xlabel("Month"); axes[0].set_ylabel("Sales (in $)")

axes[1].bar(products, product_sales, color='darkorange')
axes[1].set_title("Top-Selling Products")
axes[1].set_xlabel("Product"); axes[1].set_ylabel("Annual Sales (in $)")

plt.suptitle("Sales Dashboard: Monthly Trend + Top Products")
plt.tight_layout()
plt.show()
