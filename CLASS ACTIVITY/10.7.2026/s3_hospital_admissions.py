import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_style("whitegrid")

depts = ['Cardiology', 'Orthopedics', 'Pediatrics', 'Neurology', 'ENT']
patients = [120, 95, 150, 60, 80]
cost = [45000, 32000, 18000, 52000, 15000]
df3 = pd.DataFrame({'Department': depts, 'Patients': patients, 'Cost': cost})

plt.figure(figsize=(7, 5))
ax = sns.barplot(data=df3, x='Department', y='Patients', hue='Department', palette='Set2', legend=False)
for i, c in enumerate(cost):
    ax.text(i, patients[i] + 2, f"₹{c}", ha='center', fontsize=9)
plt.title("Patient Admissions by Department (label=Avg Treatment Cost)")
plt.tight_layout()
plt.show()
