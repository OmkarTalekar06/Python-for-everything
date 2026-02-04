import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.DataFrame({
    "Income" : [30000, 50000, 40000, 70000, 90000, 20000, 80000, 60000],
    "LoanAmount":[100000, 200000, 150000, 300000, 400000, 800000, 350000, 250000],
    "CreditScore" : [650, 720, 680, 750, 800, 600, 780, 710],
    "Approved":["No", "Yes", "No", "Yes", "Yes", "No", "Yes", "Yes"]
})

encoder = LabelEncoder()
df["Approved"] = encoder.fit_transform(df["Approved"])

x = df[["Income", "LoanAmount", "CreditScore"]]
y = df[["Approved"]].values.ravel()

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25, random_state=1
)

model = LogisticRegression(max_iter=500)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

new_applicant = pd.DataFrame({
    "Income" : [55000],
    "LoanAmount":[180000],
    "CreditScore":[700]
})

result = model.predict(new_applicant)
print("Loan Stauts", "Approved" if result[0] == 1 else "Rejected")
