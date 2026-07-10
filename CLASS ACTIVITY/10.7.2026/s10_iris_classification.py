import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

sns.set_style("whitegrid")

iris = load_iris(as_frame=True)
df10 = iris.frame
df10['species'] = df10['target'].map(dict(enumerate(iris.target_names)))

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.boxplot(data=df10, x='species', y='sepal length (cm)', hue='species',
            palette='Set2', legend=False, ax=axes[0])
axes[0].set_title("Sepal Length by Species")

sns.boxplot(data=df10, x='species', y='petal length (cm)', hue='species',
            palette='Set2', legend=False, ax=axes[1])
axes[1].set_title("Petal Length by Species")

plt.suptitle("Species Separation via Sepal/Petal Length (Box Plots)")
plt.tight_layout()
plt.show()
