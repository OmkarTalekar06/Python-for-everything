import pandas as pd 
import matplotlib.pyplot as plt

data = {
    "Age" : [18, 22, 25, 30, 40, 45, 50, 55, 60, 65],
    "Spending" : [500, 1200, 1800, 2500, 3200, 3800, 4200, 4500, 4300, 3500]
}

df = pd.DataFrame(data)
df.index = range(1 , len(df) + 1)

print("Customer Age vs Spending Dataset\n")
print(df)

avg_spending = df["Spending"].mean()
print("\nAverage Spending:", round(avg_spending, 2))

plt.figure()
plt.plot(df["Age"], df["Spending"], marker = 'o')
plt.xlabel("Customer Age")
plt.ylabel("spending Amount")
plt.title("Customer Age VS spending analysis")
plt.grid(True)
plt.show()
