import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set_style("whitegrid")
np.random.seed(1)

genres = ['Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi']
years = [2021, 2022, 2023, 2024]
ratings = np.random.uniform(5.5, 9.0, (len(genres), len(years)))

plt.figure(figsize=(7, 5))
sns.heatmap(ratings, annot=True, fmt=".1f", xticklabels=years, yticklabels=genres, cmap='YlOrRd')
plt.title("Average Rating by Genre & Year")
plt.tight_layout()
plt.show()
