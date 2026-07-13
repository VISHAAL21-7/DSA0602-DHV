library(ggplot2)
library(dplyr)

set.seed(1)
n <- 60
dept <- sample(c('CSE','AI','IT','ECE'), n, replace=TRUE)
att <- sample(50:99, n, replace=TRUE)
marks <- att*0.7 + rnorm(n, 0, 8)
df1 <- data.frame(Attendance=att, Marks=marks, Department=dept)

df1$AttBin <- cut(df1$Attendance, breaks=c(50,60,70,80,90,100),
                   labels=c('50-59','60-69','70-79','80-89','90-99'), right=FALSE)

grouped <- df1 %>% group_by(AttBin, Department) %>% summarise(Marks=mean(Marks), .groups='drop')

ggplot(grouped, aes(x=AttBin, y=Marks, color=Department, group=Department)) +
  geom_line(size=1) + geom_point(size=2) +
  labs(title="Attendance vs Internal Marks by Department",
       x="Attendance (%) Range", y="Average Internal Marks") +
  theme_minimal()
