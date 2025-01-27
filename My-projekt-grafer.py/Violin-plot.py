import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


sns.set_theme(style="dark")
sns.set_palette("muted")

data = [np.random.normal(0, std, 100) for std in range(1, 4)]

sns.violinplot(data=data)
plt.title("Violin plot")
plt.xlabel("Category")
plt.ylabel("Values")
plt.show()