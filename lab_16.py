import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
data = pd.read_csv("data.csv")

# Check if 'Months' is in the columns
if 'months' not in data.columns:
    raise KeyError("'months' column is not present in the DataFrame.")

# a. Line plot for total profit
plt.figure()
plt.plot(data["months"], data["total_profit"], color='blue', linestyle='dotted', linewidth=4, label="total_profit")
plt.title("a. Total profit of all months")
plt.xlabel("months")
plt.ylabel("sold units")
plt.legend(loc="lower right")

# b. Multiline plots for each product
plt.figure()
for product in data.columns[1:7]:
    plt.plot(data["months"], data[product], label=product)

plt.title("b. Number of units sold per month for each product")
plt.xlabel("months")
plt.ylabel("sold units")
plt.legend()

# c. Bar chart for chair and table product sales
plt.figure()
plt.bar(data["months"] - 0.2, data["chair"], 0.4, label="chair")
plt.bar(data["months"] + 0.2, data["table"], 0.4, label="table")
plt.title("c. chair and table product sales")
plt.xlabel("months")
plt.ylabel("Sold units")
plt.legend()

# d. Stack plot for all product sales data
plt.figure()
clmn = data.columns[1:7]  # Exclude "Months" and "Total profit" columns
plt.stackplot(data["months"], data[clmn].T, labels=clmn)
plt.title("d. All product sales data using stack plot")
plt.xlabel("months")
plt.ylabel("sold units")
plt.legend()

plt.show()
