library(ggplot2)

set.seed(1)
genres <- c('Action','Comedy','Drama','Horror','Sci-Fi')
years <- c(2021,2022,2023,2024)

df8 <- expand.grid(Genre=genres, Year=years)
df8$Rating <- runif(nrow(df8), 5.5, 9.0)

ggplot(df8, aes(x=factor(Year), y=Genre, fill=Rating)) +
  geom_tile(color="white") +
  geom_text(aes(label=round(Rating,1)), size=3.3) +
  scale_fill_gradient(low="yellow", high="red") +
  labs(title="Average Rating by Genre & Year", x="Year", y="Genre") +
  theme_minimal()
