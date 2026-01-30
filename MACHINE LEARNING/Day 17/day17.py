import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score


df = pd.DataFrame({
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Marks": [35, 40, 45, 55, 60, 65, 70, 78, 85, 92]
})

X = df[["Hours"]]
y = df["Marks"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1
)


model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)

print("MAE:", round(mean_absolute_error(y_test, y_pred), 2))
print("R2 Score:", round(r2_score(y_test, y_pred), 2))


test_hours = pd.DataFrame({"Hours": [2.5, 5.5, 9]})
predicted_marks = model.predict(test_hours)

for h, m in zip(test_hours["Hours"], predicted_marks):
    print(f"Study Hours: {h} -> Predicted Marks: {round(m,2)}")


plt.scatter(X, y)
plt.plot(X, model.predict(X))
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Student Marks Prediction using Linear Regression")
plt.show()
