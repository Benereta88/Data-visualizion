import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

categories = ["A", "B", "C", "D"]
values = [25, 40, 30, 20]

sns.set_theme(style="dark")
sns.set_palette("muted")

plt.bar(categories, values)
plt.title("Bar chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()