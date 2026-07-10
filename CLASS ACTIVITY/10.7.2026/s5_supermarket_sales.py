import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sns.set_style("whitegrid")
np.random.seed(1)

months = ['Jan', 'Feb', 'Mar', 'Apr']
categories = ['Grocery', 'Electronics', 'Clothing']
branches = ['Branch A', 'Branch B', 'Branch C']

rows = []
for m in months:
    for c in categories:
        for b in branches:
            rows.append([m, c, b, np.random.randint(5000, 20000)])
df5 = pd.DataFrame(rows, columns=['Month', 'Category', 'Branch', 'Sales'])

plt.figure(figsize=(9, 5))
sns.barplot(data=df5[df5.Month == 'Jan'], x='Category', y='Sales', hue='Branch')
plt.title("Product Category Sales by Branch (Jan)")
plt.tight_layout()
plt.show()
