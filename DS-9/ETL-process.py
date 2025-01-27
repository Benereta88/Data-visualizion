import pandas as pd
import matplotlib.pyplot as plt

sales_data = pd.read_csv("sales_2025.csv")
costumer_data = pd.read_csv("customers.csv")

sales_data["Price"].fillna(sales_data["Price"].mean(), inplace=True)
sales_data["Quantity"].fillna(0, inplace=True)
sales_data["Total_Sales"] = sales_data["Price"] * sales_data["Quantity"]

combined_data = pd.merge(sales_data, costumer_data, on="CostumerID, how="inner")
north_sales = combined_data[combined_data["Region"] == "North"]

north_sales.to_csv("north_sales.csv", index=False)
print("Pipline färdig! Data sparad i 'north_sales.csv'")
