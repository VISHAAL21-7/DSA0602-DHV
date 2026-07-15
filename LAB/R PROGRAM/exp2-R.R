library(ggplot2)
library(wordcloud)
library(tm)
library(dplyr)

# ---- Given dataset: Customer Satisfaction ----
df <- data.frame(
  CustomerID = 1:5,
  Age = c(25, 30, 35, 28, 40),
  SatisfactionScore = c(4, 5, 3, 4, 5)
)

# ---- Task 4 needs open-ended feedback text - not in the given table,
#      so sample feedback strings are assumed here ----
feedback <- c(
  "great service fast delivery friendly staff",
  "product quality excellent will buy again",
  "delivery was late but support was helpful",
  "amazing experience highly recommend this store",
  "price a bit high but service is great"
)

# 1. Histogram - distribution of customer ages
hist(df$Age, breaks=5, col="steelblue", border="black",
     main="Distribution of Customer Ages", xlab="Age", ylab="Frequency")

# 2. Pie chart - distribution of satisfaction scores
score_counts <- table(df$SatisfactionScore)
pie(score_counts, labels=paste0("Score ", names(score_counts)),
    main="Distribution of Customer Satisfaction Scores",
    col=rainbow(length(score_counts)))

# 3. Stacked bar chart - satisfaction scores by age group
df$AgeGroup <- cut(df$Age, breaks=c(20,30,40,50), labels=c('21-30','31-40','41-50'))
stacked <- df %>% group_by(AgeGroup, SatisfactionScore) %>% summarise(Count=n(), .groups='drop')

p3 <- ggplot(stacked, aes(x=AgeGroup, y=Count, fill=factor(SatisfactionScore))) +
  geom_col() +
  labs(title="Satisfaction Scores by Age Group", x="Age Group", y="Number of Customers",
       fill="Satisfaction Score") +
  theme_minimal()
print(p3)

# 4. Word cloud - prevalent sentiments from open-ended feedback
corpus <- Corpus(VectorSource(feedback))
corpus <- tm_map(corpus, content_transformer(tolower))
tdm <- TermDocumentMatrix(corpus)
word_freq <- sort(rowSums(as.matrix(tdm)), decreasing=TRUE)
wordcloud(names(word_freq), word_freq, min.freq=1, colors=brewer.pal(8, "Dark2"))
title("Customer Feedback Word Cloud")
