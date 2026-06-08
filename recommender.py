import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity 
# Load the dataset
df = pd.read_csv('tmdb_5000_movies.csv')

# Let's see what we have
print("Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nFirst 2 movies:")
print(df.head(2))
# Keep only the columns we need
df = df[['title', 'overview', 'genres', 'keywords']]

# Check for missing values
print("Missing values:")
print(df.isnull().sum())
df.dropna(inplace=True)
print("Shape after cleaning:", df.shape)
import ast

def extract_names(text):
    try:
        items = ast.literal_eval(text)
        return ' '.join([i['name'] for i in items])
    except:
        return ''

df['genres'] = df['genres'].apply(extract_names)
df['keywords'] = df['keywords'].apply(extract_names)

print("\nCleaned genres example:")
print(df['genres'][0])
# Combine everything into one text column
df['tags'] = df['overview'] + ' ' + df['genres'] + ' ' + df['keywords']

print("\nExample tags for first movie:")
print(df['tags'][0])
# Turn tags into numbers
tfidf = TfidfVectorizer(stop_words='english')
matrix = tfidf.fit_transform(df['tags'])

# Calculate similarity between all movies
similarity = cosine_similarity(matrix)

# The recommendation function
def recommend(movie_title):
    try:
        idx = df[df['title'] == movie_title].index[0]
        scores = list(enumerate(similarity[idx]))
        scores = sorted(scores, key=lambda x: x[1], reverse=True)
        scores = scores[1:6]
        print(f"\nMovies similar to {movie_title}:")
        for i, score in scores:
            print(f"- {df['title'][i]}")
    except:
        print("Movie not found!")

# Test it!
recommend("Avatar")
recommend("The Dark Knight")