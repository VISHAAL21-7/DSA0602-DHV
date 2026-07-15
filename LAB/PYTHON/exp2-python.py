import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from wordcloud import WordCloud

# ---- Given dataset: Customer Satisfaction ----
df = pd.DataFrame({
    'CustomerID': [1, 2, 3, 4, 5],
    'Age': [25, 30, 35, 28, 40],
    'SatisfactionScore': [4, 5, 3, 4, 5]
})

# ---- Task 4 needs open-ended feedback text - not in the given table,
#      so sample feedback strings are assumed here ----
feedback = [
    "great service fast delivery friendly staff",
    "product quality excellent will buy again",
    "delivery was late but support was helpful",
    "amazing experience highly recommend this store",
    "price a bit high but service is great"
]

# 1. Histogram - distribution of customer ages
plt.figure(figsize=(7, 5))
plt.hist(df['Age'], bins=5, color='steelblue', edgecolor='black')
plt.title("Distribution of Customer Ages")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 2. Pie chart - distribution of satisfaction scores
score_counts = df['SatisfactionScore'].value_counts().sort_index()
plt.figure(figsize=(6, 6))
plt.pie(score_counts.values, labels=[f"Score {s}" for s in score_counts.index],
        autopct='%1.1f%%', startangle=90)
plt.title("Distribution of Customer Satisfaction Scores")
plt.tight_layout()
plt.show()

# 3. Stacked bar chart - satisfaction scores by age group
df['AgeGroup'] = pd.cut(df['Age'], bins=[20, 30, 40, 50], labels=['21-30', '31-40', '41-50'])
stacked = df.groupby(['AgeGroup', 'SatisfactionScore'], observed=True).size().unstack(fill_value=0)
stacked.plot(kind='bar', stacked=True, figsize=(7, 5), colormap='viridis')
plt.title("Satisfaction Scores by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Number of Customers")
plt.legend(title="Satisfaction Score")
plt.tight_layout()
plt.show()

# 4. Word cloud - prevalent sentiments from open-ended feedback
text = " ".join(feedback)
wc = WordCloud(width=800, height=400, background_color='white').generate(text)
plt.figure(figsize=(9, 5))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.title("Customer Feedback Word Cloud")
plt.tight_layout()
plt.show()
