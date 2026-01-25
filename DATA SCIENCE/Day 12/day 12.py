import matplotlib.pyplot as plt
import requests

states = [
    "Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh",
    "Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand",
    "Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur",
    "Meghalaya","Mizoram","Nagaland","Odisha","Punjab",
    "Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura",
    "Uttar Pradesh","Uttarakhand","West Bengal"
]

state_share = [
    0.041,0.001,0.026,0.085,0.021,
    0.001,0.051,0.021,0.006,0.027,
    0.051,0.026,0.061,0.093,0.002,
    0.003,0.001,0.002,0.035,0.022,
    0.059,0.001,0.058,0.028,0.003,
    0.166,0.008,0.075
]

url = "https://api.worldbank.org/v2/country/IND/indicator/SP.POP.TOTL?format=json"
response = requests.get(url)
data = response.json()

india_population = int(data[1][0]["value"])
print("India Total Population : ", india_population)

male_ratio = 0.511
female_ratio = 0.489
child_ratio=0.267

male = []
female = []
children = []

for share in state_share:
    state_population = india_population * share
    male.append(state_population * male_ratio)
    female.append(state_population * female_ratio)
    children.append(state_population * child_ratio)

#Male & Female Graph
plt.figure(figsize=(12, 6))
plt.bar(states, male, label="Male")
plt.bar(states, female, bottom=male, label="Females")
plt.xticks(rotation=90)
plt.ylabel("Population")
plt.title("State-Wise Distritubtion of Male and Female Population in India")
plt.legend()
plt.tight_layout()
plt.show()

#Children Graph
plt.figure(figsize=(12, 6))
plt.bar(states, children)
plt.xticks(rotation=90)
plt.ylabel("Population")
plt.title("State-Wise Population of Children (0-14 years)")
plt.tight_layout()
plt.show()
