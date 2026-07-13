library(ggplot2)
library(dplyr)

set.seed(1)
n <- 40
battery <- runif(n, 30, 100)
mfr <- sample(c('Tesla','Tata','BYD','Hyundai'), n, replace=TRUE)
price <- battery*800 + rnorm(n, 0, 3000)
range_km <- battery*4 + rnorm(n, 0, 20)
df2 <- data.frame(Battery=battery, Price=price, Range=range_km, Manufacturer=mfr)

df2$BatteryBin <- cut(df2$Battery, breaks=c(30,50,70,90,100),
                       labels=c('30-49','50-69','70-89','90-100'), include.lowest=TRUE)

grouped <- df2 %>% group_by(BatteryBin, Manufacturer) %>%
  summarise(AvgPrice=mean(Price), AvgRange=mean(Range), .groups='drop')

ggplot(grouped, aes(x=BatteryBin, y=AvgPrice, fill=Manufacturer)) +
  geom_col(position=position_dodge()) +
  geom_text(aes(label=paste0(round(AvgRange),"km")),
            position=position_dodge(width=0.9), vjust=-0.3, size=3) +
  labs(title="Avg Price by Battery Capacity & Manufacturer (labels = Avg Range)",
       x="Battery Capacity (kWh)", y="Average Price") +
  theme_minimal()
