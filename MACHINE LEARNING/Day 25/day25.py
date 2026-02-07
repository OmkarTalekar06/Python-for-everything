from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from PIL import Image
import numpy as np


digits = load_digits()
X = digits.data
y = digits.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)


model = LogisticRegression(max_iter=5000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

img = Image.open("Day 25/digit.png").convert("L") 
img = img.resize((8, 8))

img_array = np.array(img)
img_array = 16 - (img_array / 16)           
img_flat = img_array.reshape(1, -1)

prediction = model.predict(img_flat)
print("Predicted Digit:", prediction[0])
