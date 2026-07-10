import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sns.set_style("whitegrid")
np.random.seed(1)

states = ['TN', 'KA', 'MH', 'DL', 'UP', 'WB', 'KL', 'GJ']
active_cases = np.random.randint(500, 15000, len(states))
df9 = pd.DataFrame({'State': states, 'ActiveCases': active_cases}).sort_values('ActiveCases', ascending=False)

plt.figure(figsize=(8, 3))
sns.heatmap(df9[['ActiveCases']].T, annot=True, fmt="d", xticklabels=df9.State,
            yticklabels=['Active Cases'], cmap='Reds')
plt.title("State-wise Active COVID-19 Cases (Sequential Scale)")
plt.tight_layout()
plt.show()
