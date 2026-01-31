import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix


data = {
    "message": [
        "Win a free iPhone now",
        "Limited offer click here",
        "Congratulations you won a prize",
        "Meeting at 10 am tomorrow",
        "Project submission deadline extended",
        "Let's have lunch today",
        "Earn money from home easily",
        "Exclusive deal just for you"
    ],
    "label": ["spam", "spam", "spam", "ham", "ham", "ham", "spam", "spam"]
}

df = pd.DataFrame(data)

X = df["message"]
y = df["label"]

vectorizer = CountVectorizer()
X_vector = vectorizer.fit_transform(X)

# split data
X_train, X_test, y_train, y_test = train_test_split(
    X_vector, y, test_size=0.25, random_state=1
)

# train model
model = MultinomialNB()
model.fit(X_train, y_train)

# test model
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# real prediction
emails = [
    "Free cashback offer waiting",
    "Can we reschedule the meeting"
]

emails_vector = vectorizer.transform(emails)
results = model.predict(emails_vector)

for e, r in zip(emails, results):
    print(f"Email: '{e}' -> {r.upper()}")
