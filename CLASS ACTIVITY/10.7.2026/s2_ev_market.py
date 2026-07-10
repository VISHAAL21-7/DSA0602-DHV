import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sns.set_style("whitegrid")
np.random.seed(1)

n = 40
battery = np.random.uniform(30, 100, n)
mfr = np.random.choice(['Tesla', 'Tata', 'BYD', 'Hyundai'], n)
price = battery * 800 + np.random.normal(0, 3000, n)
range_km = battery * 4 + np.random.normal(0, 20, n)
df2 = pd.DataFrame({'Battery': battery, 'Price': price, 'Range': range_km, 'Manufacturer': mfr})

# bin battery capacity into ranges for a grouped bar chart
bins = [30, 50, 70, 90, 100]
labels = ['30-49', '50-69', '70-89', '90-100']
df2['BatteryBin'] = pd.cut(df2['Battery'], bins=bins, labels=labels, include_lowest=True)

grouped = df2.groupby(['BatteryBin', 'Manufacturer'], observed=True).agg(
    AvgPrice=('Price', 'mean'),
    AvgRange=('Range', 'mean')
).reset_index()

plt.figure(figsize=(9, 5))
ax = sns.barplot(data=grouped, x='BatteryBin', y='AvgPrice', hue='Manufacturer')

# annotate average driving range on each bar (stands in for the old bubble "size")
for container, mfr_name in zip(ax.containers, grouped.Manufacturer.unique()):
    sub_ranges = grouped[grouped.Manufacturer == mfr_name]['AvgRange'].values
    ax.bar_label(container, labels=[f"{r:.0f}km" for r in sub_ranges], fontsize=8, padding=2)

plt.title("Avg Price by Battery Capacity & Manufacturer (labels = Avg Range)")
plt.xlabel("Battery Capacity (kWh)")
plt.ylabel("Average Price")
plt.tight_layout()
plt.show()
