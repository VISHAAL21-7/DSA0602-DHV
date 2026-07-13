library(ggplot2)
library(dplyr)

set.seed(1)
states <- c('TN','KA','MH','DL','UP','WB','KL','GJ')
active_cases <- sample(500:15000, length(states))
df9 <- data.frame(State=states, ActiveCases=active_cases) %>%
  arrange(desc(ActiveCases))
df9$State <- factor(df9$State, levels=df9$State)

ggplot(df9, aes(x=State, y=1, fill=ActiveCases)) +
  geom_tile(color="white") +
  geom_text(aes(label=ActiveCases), size=3.3) +
  scale_fill_gradient(low="white", high="darkred") +
  labs(title="State-wise Active COVID-19 Cases (Sequential Scale)") +
  theme_minimal() +
  theme(axis.title.y=element_blank(), axis.text.y=element_blank())
