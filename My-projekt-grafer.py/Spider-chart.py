import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


labels = np.array([ "A", "B", "C", "D", "E", "F"])
data = np.array([4, 5, 2, 5, 3, 5])


sns.set_theme(style="dark")
sns.set_palette("muted")

angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)
data = np.concatenate((data, [data[0]]))
angles = np.concatenate((angles, [angles[0]]))

plt.polar(angles, data, marker="o")
plt.fill(angles, data, alpha=0.25)
plt.title("Spider chart")
plt.show()