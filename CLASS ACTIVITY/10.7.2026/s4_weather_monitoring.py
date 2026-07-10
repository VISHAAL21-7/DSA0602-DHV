import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.random.seed(1)

days = pd.date_range("2026-06-01", periods=30)
cities = ['Chennai', 'Delhi', 'Mumbai']
styles = ['-', '--', '-.']

plt.figure(figsize=(8, 5))
for city, style in zip(cities, styles):
    base = {'Chennai': 33, 'Delhi': 38, 'Mumbai': 30}[city]
    temp = base + np.random.normal(0, 1.5, 30).cumsum() * 0.1
    plt.plot(days, temp, linestyle=style, label=city)

plt.title("Daily Temperature Trend by City")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
