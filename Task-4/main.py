import json

class MovieRecommendationSystem:
    def __init__(self, movies_dataset, user_ratings):
        self.movies_dataset = movies_dataset
        self.user_ratings = user_ratings

    def get_top_rated_movie_genre(self, user_id):
        user_ratings = next((user['ratings'] for user in self.user_ratings if user['user'] == user_id), None)
        if user_ratings is None:
            return None

        # Find the highest-rated movie and its genre
        top_rated_movie = max(user_ratings, key=user_ratings.get)
        top_rated_genre = next((movie['genre'] for movie in self.movies_dataset if movie['title'] == top_rated_movie), None)

        return top_rated_genre

    def suggest_movies(self, user_id):
        user_top_genre = self.get_top_rated_movie_genre(user_id)

        if user_top_genre is None:
            return "No recommendations available for the user."

        # Find movies from the dataset with the same genre
        recommended_movies = [movie['title'] for movie in self.movies_dataset if movie['genre'] == user_top_genre]

        if not recommended_movies:
            return "No similar movies found in the same genre."

        return f"We recommend the following movies in the genre '{user_top_genre}': {', '.join(recommended_movies)}."

# Load movies dataset
with open('movies_dataset.json', 'r') as movies_file:
    movies_dataset = json.load(movies_file)

# Load user ratings dataset
with open('user_ratings.json', 'r') as user_ratings_file:
    user_ratings_data = json.load(user_ratings_file)

# Create an instance of the MovieRecommendationSystem
recommendation_system = MovieRecommendationSystem(movies_dataset, user_ratings_data)

# Specify the user for whom you want to make a recommendation
user_to_recommend = 'User1'

# Get movie recommendations for the specified user
recommendations = recommendation_system.suggest_movies(user_to_recommend)

print(recommendations)
