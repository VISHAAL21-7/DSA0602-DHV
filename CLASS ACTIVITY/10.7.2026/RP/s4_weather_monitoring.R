library(ggplot2)
library(dplyr)

set.seed(1)
days <- seq(as.Date("2026-06-01"), by="day", length.out=30)
cities <- c('Chennai','Delhi','Mumbai')
base_temp <- c(Chennai=33, Delhi=38, Mumbai=30)

df4 <- data.frame()
for (city in cities) {
  temp <- base_temp[[city]] + cumsum(rnorm(30, 0, 1.5))*0.1
  df4 <- rbind(df4, data.frame(Date=days, Temperature=temp, City=city))
}

ggplot(df4, aes(x=Date, y=Temperature, color=City, linetype=City)) +
  geom_line(size=1) +
  labs(title="Daily Temperature Trend by City", y="Temperature (C)") +
  theme_minimal() +
  theme(axis.text.x=element_text(angle=45, hjust=1))
