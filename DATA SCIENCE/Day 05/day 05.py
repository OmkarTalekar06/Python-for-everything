import matplotlib.pyplot as plt

days = ["Day 01", "Day 02", "Day 03", "Day 04", "Day 05", "Day 06", "Day 07"]

confirmed = [120, 150, 180, 210, 260, 300, 350]
recovered = [20, 35, 50, 60, 90, 100, 120]
deaths = [2, 3, 5, 7, 8, 10, 12]

plt.figure(figsize=(9, 5))

plt.plot(days, confirmed, marker='o', label="Confirmed Cases")
plt.plot(days, recovered, marker='o', label="Recovered Cases")
plt.plot(days, deaths, marker='o', label="Deaths")

plt.xlabel("Days")
plt.ylabel("Number of Cases")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
