import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1)

salary = np.random.normal(60000, 15000, 300)

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].hist(salary, bins=10, color='steelblue')
axes[0].set_title("Bins=10")
axes[1].hist(salary, bins=40, color='darkorange')
axes[1].set_title("Bins=40")
plt.suptitle("Salary Distribution: Bin Size Comparison")
plt.tight_layout()
plt.show()
