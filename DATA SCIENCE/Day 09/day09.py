import requests
import matplotlib.pyplot as plt

API_KEY = "Your APi key"

movies = [
    "Fateh",     
    "Yodha",     
    "Crew",      
    "Maidaan",   
    "Metro",     
    "Champion",  
    "Sarfira",   
    "Stree 2",   
    "Emergency", 
    "Singham",   
    "Bhulaiyaa", 
    "Welcome"   
]


ratings = []
votes = []

for movie in movies:
    url=f"http://www.omdbapi.com/?t={movie}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data["Response"]=="True":
        ratings.append(float(data["imdbRating"]))
        votes.append(int(data["imdbVotes"].replace(",","")))

        print(movie, " Rating:", data["imdbRating"], "\nVotes:", data["imdbVotes"], "\n")

plt.bar(movies, ratings)
plt.title("IDMb ratings of movies")
plt.xlabel("Movies")
plt.ylabel("IMDb ratings")
plt.xticks(rotation=45)
plt.show()

plt.bar(movies, votes)
plt.title("Votes for movies")
plt.xlabel("Movies")
plt.ylabel("IMDb votes")
plt.xticks(rotation=45)
plt.show()

plt.scatter(votes, ratings)
plt.title("IDMb ratings vs IDMb votes")
plt.xlabel("Votes")
plt.ylabel("Ratings")
plt.xticks(rotation=45)
plt.show()
