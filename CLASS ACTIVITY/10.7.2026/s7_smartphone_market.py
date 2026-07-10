import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sns.set_style("whitegrid")
np.random.seed(1)

n = 50
brand = np.random.choice(['Samsung', 'Apple', 'OnePlus', 'Xiaomi'], n)
ram = np.random.choice([4, 6, 8, 12, 16], n)
storage = np.random.choice([64, 128, 256, 512], n)
speed = np.random.uniform(2.0, 3.5, n)
price = ram * 3000 + storage * 10 + speed * 5000 + np.random.normal(0, 3000, n)
df7 = pd.DataFrame({'Brand': brand, 'RAM': ram, 'Storage': storage, 'Speed': speed, 'Price': price})

grouped = df7.groupby(['RAM', 'Brand'], observed=True).agg(
    AvgPrice=('Price', 'mean'),
    AvgSpeed=('Speed', 'mean')
).reset_index()

plt.figure(figsize=(9, 6))
ax = sns.barplot(data=grouped, x='RAM', y='AvgPrice', hue='Brand', palette='viridis')

# annotate average processor speed on each bar (stands in for old color-gradient channel)
for container, brand_name in zip(ax.containers, grouped.Brand.unique()):
    sub_speed = grouped[grouped.Brand == brand_name]['AvgSpeed'].values
    ax.bar_label(container, labels=[f"{s:.1f}GHz" for s in sub_speed], fontsize=8, padding=2)

plt.title("RAM vs Avg Price by Brand (labels = Avg Processor Speed)")
plt.xlabel("RAM (GB)")
plt.ylabel("Average Price")
plt.tight_layout()
plt.show()
