# Movie Recommendation System 🎬

A content-based movie recommender that suggests 5 similar movies 
based on genre, story, and keywords.

## How It Works
Each movie is converted into a "tag" combining its overview, 
genres and keywords. Cosine similarity is then used to find 
the most similar movies.

## Example Results
Avatar → Mission to Mars, Aliens, Moonraker...
The Dark Knight → The Dark Knight Rises, Batman Begins...

## Technologies Used
- Python
- Pandas
- Scikit-learn (TF-IDF, Cosine Similarity)

## Dataset
TMDB 5000 Movies Dataset (Kaggle)
