import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# movie dataset
movies = pd.DataFrame({
    "title": [
        "Inception",
        "Interstellar",
        "The Dark Knight",
        "Avengers",
        "Titanic",
        "Notebook"
    ],
    "genre": [
        "sci-fi thriller",
        "sci-fi space drama",
        "action crime thriller",
        "action superhero sci-fi",
        "romance drama",
        "romance love drama"
    ]
})

vectorizer = CountVectorizer()
genre_matrix = vectorizer.fit_transform(movies["genre"])


similarity = cosine_similarity(genre_matrix)


def recommend(movie_name):
    index = movies[movies["title"] == movie_name].index[0]
    scores = list(enumerate(similarity[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print("Recommended movies:")
    for i in scores[1:4]:
        print(movies.iloc[i[0]]["title"])

# test recommendation
recommend("Inception")
