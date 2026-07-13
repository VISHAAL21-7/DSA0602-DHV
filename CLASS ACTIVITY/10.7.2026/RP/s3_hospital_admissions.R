library(ggplot2)

depts <- c('Cardiology','Orthopedics','Pediatrics','Neurology','ENT')
patients <- c(120,95,150,60,80)
cost <- c(45000,32000,18000,52000,15000)
df3 <- data.frame(Department=depts, Patients=patients, Cost=cost)

ggplot(df3, aes(x=Department, y=Patients, fill=Department)) +
  geom_col() +
  geom_text(aes(label=paste0("Rs.", Cost)), vjust=-0.4, size=3.3) +
  labs(title="Patient Admissions by Department (label=Avg Treatment Cost)",
       y="Number of Patients") +
  theme_minimal() +
  theme(legend.position="none")
