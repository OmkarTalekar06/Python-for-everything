import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


data = {
    "Temperature": [30, 25, 28, 35, 22, 20, 33, 27],
    "Humidity": [70, 80, 75, 60, 85, 90, 65, 78],
    "WindSpeed": [10, 12, 8, 15, 7, 6, 14, 9],
    "Weather": ["Sunny", "Rainy", "Sunny", "Sunny", "Rainy", "Rainy", "Sunny", "Rainy"]
}

df = pd.DataFrame(data)


df["Weather"] = df["Weather"].map({"Sunny": 1, "Rainy": 0})

X = df[["Temperature", "Humidity", "WindSpeed"]]
y = df["Weather"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=0
)


model = LogisticRegression()
model.fit(X_train, y_train)


pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, pred))

new_day = pd.DataFrame([[29, 72, 11]],
                       columns=["Temperature", "Humidity", "WindSpeed"])
result = model.predict(new_day)

print("Predicted Weather:", "Sunny" if result[0] == 1 else "Rainy")
