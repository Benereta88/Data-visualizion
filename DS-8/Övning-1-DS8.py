import pandas as pd
import matplotlib.pyplot as plt

# Läs in data 
dataFrame = pd.read_csv("C:/Users/Book/OneDrive - TUC Sweden/Skrivbordet/DS-9/sales.csv")

print(dataFrame)

# Gruppera och summera försäljning per produkt
dataFrame["Sales"] = dataFrame["Price"] * dataFrame["Quantity"] 
print(dataFrame)

grouped_data = dataFrame.groupby("Product")["Sales"].sum()
print(grouped_data)

# Skapa ett stapeldiagram
plt.bar(grouped_data.index, grouped_data.values)
plt.title("Total försäljning per produkt")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()

#  # Gruppera och summera försäljning över tid
# time_series = dataFrame.groupby("Date").sum("Sales")
# plt.plot(time_series.index, time_series["Sales"])
# plt.title("Försäljning över tid")
# plt.xlabel("Date")
# plt.ylabel("Sales")
# plt.show()
