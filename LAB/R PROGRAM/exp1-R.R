library(ggplot2)
library(gridExtra)

# ---- Given dataset: Monthly Sales ----
months <- c('January','February','March','April','May')
sales <- c(15000, 18000, 22000, 20000, 23000)
df_sales <- data.frame(Month=factor(months, levels=months), Sales=sales)

# ---- Task 2 needs "top-selling products" - not in the given table,
#      so a small supplementary product dataset is assumed here ----
products <- c('Product A','Product B','Product C','Product D','Product E')
product_sales <- c(42000, 35000, 51000, 28000, 39000)
df_products <- data.frame(Product=factor(products, levels=products), Sales=product_sales)

# ---- Task 3 needs "advertising budget" - not in the given table,
#      so a plausible monthly budget series is assumed here ----
ad_budget <- c(2000, 2500, 3200, 2800, 3500)
df_ad <- data.frame(Budget=ad_budget, Sales=sales)

# 1. Line chart - monthly sales trend
p1 <- ggplot(df_sales, aes(x=Month, y=Sales, group=1)) +
  geom_line(color="steelblue", size=1) + geom_point(color="steelblue", size=2) +
  labs(title="Monthly Sales Trend", x="Month", y="Sales (in $)") +
  theme_minimal()
print(p1)

# 2. Bar chart - top-selling products for the year
p2 <- ggplot(df_products, aes(x=Product, y=Sales)) +
  geom_col(fill="darkorange") +
  labs(title="Top-Selling Products for the Year", x="Product", y="Annual Sales (in $)") +
  theme_minimal()
print(p2)

# 3. Scatter plot - advertising budget vs monthly sales
p3 <- ggplot(df_ad, aes(x=Budget, y=Sales)) +
  geom_point(color="firebrick", size=3) +
  labs(title="Advertising Budget vs Monthly Sales", x="Advertising Budget (in $)", y="Sales (in $)") +
  theme_minimal()
print(p3)
# Insight: sales rise as ad budget rises, suggesting a positive relationship
# between advertising spend and revenue (correlation, not proof of causation).

# 4. Combined dashboard - line chart + bar chart together
grid.arrange(p1, p2, ncol=2, top="Sales Dashboard: Monthly Trend + Top Products")
