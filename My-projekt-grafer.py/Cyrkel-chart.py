import matplotlib.pyplot as plt

labels = ["Category A", "Category B", "Category C"]
sizes = [10, 65, 25 ]
explode = (0.5, 0.5, 0.5)
print(len)


plt.pie(sizes, labels=labels, autopct= "%1.1f%%")
plt.title("Pie chart")
plt.show()