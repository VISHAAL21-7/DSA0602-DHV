library(ggplot2)
library(dplyr)

set.seed(1)
n <- 50
brand <- sample(c('Samsung','Apple','OnePlus','Xiaomi'), n, replace=TRUE)
ram <- sample(c(4,6,8,12,16), n, replace=TRUE)
storage <- sample(c(64,128,256,512), n, replace=TRUE)
speed <- runif(n, 2.0, 3.5)
price <- ram*3000 + storage*10 + speed*5000 + rnorm(n, 0, 3000)
df7 <- data.frame(Brand=brand, RAM=ram, Storage=storage, Speed=speed, Price=price)

grouped <- df7 %>% group_by(RAM, Brand) %>%
  summarise(AvgPrice=mean(Price), AvgSpeed=mean(Speed), .groups='drop')

ggplot(grouped, aes(x=factor(RAM), y=AvgPrice, fill=Brand)) +
  geom_col(position=position_dodge()) +
  geom_text(aes(label=paste0(round(AvgSpeed,1),"GHz")),
            position=position_dodge(width=0.9), vjust=-0.3, size=3) +
  labs(title="RAM vs Avg Price by Brand (labels = Avg Processor Speed)",
       x="RAM (GB)", y="Average Price") +
  theme_minimal()
