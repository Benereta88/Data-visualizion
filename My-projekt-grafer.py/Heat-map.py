import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(10, 10)

sns.heatmap(data, annot=True)
plt.title("Heat map")
plt.show()
