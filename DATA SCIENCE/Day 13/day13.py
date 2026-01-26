import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Area_sqft" : [400, 600, 800, 1000, 1200, 1500, 1800, 2200],
    "Price_Lakhs" : [90, 140, 190, 260, 340, 460, 620, 820]
}

df = pd.DataFrame(data)

df.index = range(1, len(df) + 1)
print("Mumbai House price dataset \n")
print(df)

mean_price = df["Price_Lakhs"].mean()
median_price = df["Price_Lakhs"].median()

print("\nAverage Price (Lakhs):", round(mean_price, 2))
print("Median Price (Lakhs):", median_price)

plt.figure()
plt.plot(df["Area_sqft"], df["Price_Lakhs"], marker='o')
plt.xlabel("Area (sqft)")
plt.ylabel("Price (Lakhs)")
plt.title("Mumbai House Price Analysis")
plt.grid(True)
plt.show()
