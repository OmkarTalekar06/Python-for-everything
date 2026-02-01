import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# load dataset
data = load_diabetes()
X = pd.DataFrame(data.data, columns=data.feature_names)


y = (data.target > data.target.mean()).astype(int)


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1
)

# train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# test model
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# predict for new patient (sample values)
new_patient = pd.DataFrame([X.mean()], columns=X.columns)
result = model.predict(new_patient)

print("Prediction:", "Diabetic" if result[0] == 1 else "Not Diabetic")
