import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


data = {
    "tenure": [1, 3, 6, 9, 12, 18, 24, 30, 36, 48],
    "monthly_charges": [80, 75, 70, 65, 60, 55, 50, 45, 40, 35],
    "total_charges": [80, 225, 420, 585, 720, 990, 1200, 1350, 1440, 1680],
    "churn": [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
}

df = pd.DataFrame(data)


X = df.drop("churn", axis=1)
y = df["churn"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1
)


model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))


new_customer = [[10, 68, 680]]
result = model.predict(new_customer)

if result[0] == 1:
    print("Customer will CHURN")
else:
    print("Customer will NOT churn")
