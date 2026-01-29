import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

# dataset
df = pd.DataFrame({
    "Area": [500, 650, 800, 950, 1100, 1300, 1500, 1700, 1900, 2100],
    "Price": [10, 13, 16, 19, 22, 26, 30, 34, 38, 42]  # price in lakhs
})

X = df[["Area"]]
y = df["Price"]

# split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1
)

# train
model = LinearRegression()
model.fit(X_train, y_train)

# test
y_pred = model.predict(X_test)

print("MAE:", round(mean_absolute_error(y_test, y_pred), 2), "Lakhs")
print("R2 Score:", round(r2_score(y_test, y_pred), 2))

# real predictions
test_houses = pd.DataFrame({"Area": [900, 1400, 2000]})
prices = model.predict(test_houses)

for a, p in zip(test_houses["Area"], prices):
    print(f"Area {a} sq ft -> Price {round(p,2)} Lakhs")

# graph (same structure)
plt.scatter(X, y)
plt.plot(X, model.predict(X))
plt.xlabel("Area (sq ft)")
plt.ylabel("House Price (Lakhs)")
plt.title("House Price Prediction using Linear Regression")
plt.show()
