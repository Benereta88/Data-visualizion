import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [30, 20, 30, 20, 30]
y2 = [25, 10, 25, 10, 25]

plt.fill_between(x, y1, y2, color="skyblue", alpha=1)
plt.title("Area chart")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

