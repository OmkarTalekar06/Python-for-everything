import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# sample salary dataset
data = {
    "Experience": [1, 2, 3, 4, 5, 6, 7, 8],
    "Salary": [30000, 35000, 40000, 50000, 60000, 70000, 80000, 90000]
}

df = pd.DataFrame(data)


X = df[["Experience"]]
y = df["Salary"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)


model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)
print("R2 Score:", r2_score(y_test, y_pred))


new_exp = [[10]]
predicted_salary = model.predict(new_exp)

print("Predicted Salary:", int(predicted_salary[0]))
