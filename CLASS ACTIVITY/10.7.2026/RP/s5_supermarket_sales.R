library(ggplot2)

set.seed(1)
months <- c('Jan','Feb','Mar','Apr')
categories <- c('Grocery','Electronics','Clothing')
branches <- c('Branch A','Branch B','Branch C')

df5 <- expand.grid(Month=months, Category=categories, Branch=branches)
df5$Sales <- sample(5000:20000, nrow(df5), replace=TRUE)

jan_data <- df5[df5$Month=='Jan', ]

ggplot(jan_data, aes(x=Category, y=Sales, fill=Branch)) +
  geom_col(position=position_dodge()) +
  labs(title="Product Category Sales by Branch (Jan)") +
  theme_minimal()
