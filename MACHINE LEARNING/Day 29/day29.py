import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


data = {
    "text": [
        "Government passes new education reform bill",
        "Scientists discover new planet in solar system",
        "Celebrity adopts alien baby from Mars",
        "Secret medicine cures all diseases overnight",
        "Stock market hits record high this year",
        "Man claims he can live without food for 5 years",
        "New technology improves battery life",
        "Politician caught in corruption scandal"
    ],
    "label": [1, 1, 0, 0, 1, 0, 1, 1]   # 1 = Real, 0 = Fake
}

df = pd.DataFrame(data)


X = df["text"]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)


vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)


model = LogisticRegression()
model.fit(X_train_vec, y_train)


y_pred = model.predict(X_test_vec)
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)


news = ["Scientists say chocolate increases lifespan"]

news_vec = vectorizer.transform(news)
prediction = model.predict(news_vec)

if prediction[0] == 1:
    print("Prediction: Real News")
else:
    print("Prediction: Fake News")
