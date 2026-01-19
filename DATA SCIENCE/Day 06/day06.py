import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul","Aug", "Sep", "Oct", "Nov", "Dec"]
sales = [12000, 15000, 10000, 18000, 20000, 17000, 15000, 17000, 19000, 25000, 22000, 23000]

print("Months:", months)
print("Sales:", sales)

plt.plot(months, sales, marker='o')
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Sales Data Trends Analysis")
plt.ylim(0, 27000)
plt.grid(True)

plt.show()
