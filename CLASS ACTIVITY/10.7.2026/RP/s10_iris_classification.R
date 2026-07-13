library(ggplot2)
library(gridExtra)

data(iris)

p1 <- ggplot(iris, aes(x=Species, y=Sepal.Length, fill=Species)) +
  geom_boxplot() +
  labs(title="Sepal Length by Species") +
  theme_minimal() + theme(legend.position="none")

p2 <- ggplot(iris, aes(x=Species, y=Petal.Length, fill=Species)) +
  geom_boxplot() +
  labs(title="Petal Length by Species") +
  theme_minimal() + theme(legend.position="none")

grid.arrange(p1, p2, ncol=2, top="Species Separation via Sepal/Petal Length (Box Plots)")
