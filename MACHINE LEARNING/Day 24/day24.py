import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

data = {
    "Amount": [100, 2500, 300, 5000, 120, 7000, 200, 9000],
    "Transactions_Per_Day": [2, 15, 3, 20, 1, 25, 2, 30],
    "Is_Fraud": [0, 1, 0, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

X = df[["Amount", "Transactions_Per_Day"]]
y = df["Is_Fraud"].values.ravel()


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

new_transaction = pd.DataFrame([[6000, 22]],
                                columns=["Amount", "Transactions_Per_Day"])

result = model.predict(new_transaction)
print("Transaction Status:", "Fraud" if result[0] == 1 else "Legitimate")
