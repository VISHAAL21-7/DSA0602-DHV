import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sns.set_style("whitegrid")
np.random.seed(1)

n = 60
dept = np.random.choice(['CSE', 'AI', 'IT', 'ECE'], n)
att = np.random.randint(50, 100, n)
marks = att * 0.7 + np.random.normal(0, 8, n)
df1 = pd.DataFrame({'Attendance': att, 'Marks': marks, 'Department': dept})

# bin attendance so trend per department is readable as a line
bins = [50, 60, 70, 80, 90, 100]
labels = ['50-59', '60-69', '70-79', '80-89', '90-99']
df1['AttBin'] = pd.cut(df1['Attendance'], bins=bins, labels=labels, right=False)
grouped = df1.groupby(['AttBin', 'Department'], observed=True)['Marks'].mean().reset_index()

plt.figure(figsize=(7, 5))
for d in grouped.Department.unique():
    sub = grouped[grouped.Department == d]
    plt.plot(sub.AttBin, sub.Marks, marker='o', label=d)

plt.title("Attendance vs Internal Marks by Department")
plt.xlabel("Attendance (%) Range")
plt.ylabel("Average Internal Marks")
plt.legend(title="Department")
plt.tight_layout()
plt.show()
