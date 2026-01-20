import matplotlib.pyplot as plt


players = ["Virat", "Rohit", "Dhoni", "Rahul", "Pant"]
runs = [6200, 5800, 5000, 4200, 3800]
matches = [230, 240, 250, 210, 190]
balls_faced = [4700, 4600, 4200, 3500, 3000]


averages = []
strike_rates = []

for i in range(len(players)):
    averages.append(round(runs[i] / matches[i], 2))
    strike_rates.append(round((runs[i] / balls_faced[i]) * 100, 2))


plt.figure(figsize=(12, 8))


plt.subplot(2, 2, 1)
plt.bar(players, runs)
plt.title("Total Runs")
plt.ylabel("Runs")
plt.ylim(0, 7000)


plt.subplot(2, 2, 2)
plt.bar(players, strike_rates)
plt.title("Strike Rate")
plt.ylabel("Strike Rate")
plt.ylim(0, max(strike_rates) + 20)


plt.subplot(2, 1, 2)
plt.plot(players, averages, marker='o')
plt.title("Batting Average")
plt.xlabel("Players")
plt.ylabel("Average")
plt.ylim(0, max(averages) + 10)

for i in range(len(players)):
    plt.text(players[i], averages[i] + 0.5, averages[i], ha='center')

plt.tight_layout()
plt.show()
