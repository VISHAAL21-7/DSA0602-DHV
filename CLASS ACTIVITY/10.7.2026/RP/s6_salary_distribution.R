library(ggplot2)
library(gridExtra)

set.seed(1)
salary <- rnorm(300, 60000, 15000)
df6 <- data.frame(Salary=salary)

p1 <- ggplot(df6, aes(x=Salary)) +
  geom_histogram(bins=10, fill="steelblue") +
  labs(title="Bins=10") + theme_minimal()

p2 <- ggplot(df6, aes(x=Salary)) +
  geom_histogram(bins=40, fill="darkorange") +
  labs(title="Bins=40") + theme_minimal()

grid.arrange(p1, p2, ncol=2, top="Salary Distribution: Bin Size Comparison")
