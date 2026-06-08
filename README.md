🎬 Movie Recommendation System
A content-based movie recommender system that suggests similar movies based on genre, plot, and keywords using TF-IDF vectorization and cosine similarity.
📌 Project Overview
This project recommends movies by analyzing textual features such as:
Movie overview
Genres
Keywords
These features are combined into a single text representation, then converted into numerical vectors using TF-IDF, and compared using cosine similarity to find the most similar movies.
⚙️ How It Works
Clean and preprocess movie dataset
Extract meaningful text features (genres, keywords, overview)
Combine features into a single “tag”
Apply TF-IDF vectorization
Compute cosine similarity between all movies
Recommend top 5 most similar movies
🎯 Example Output
Avatar → Aliens, Moonraker, Mission to Mars...
The Dark Knight → Batman Begins, The Dark Knight Rises...
🛠️ Technologies Used
Python 🐍
Pandas
NumPy
Scikit-learn
TF-IDF Vectorizer
Cosine Similarity
Streamlit (for web app interface)
📊 Dataset
TMDB 5000 Movies Dataset (Kaggle) containing:
Titles
Genres
Overviews
Keywords
🚀 How to Run
1. Clone repository
git clone https://github.com/raghidaq/movie-recommender.git
cd movie-recommender
2. Install dependencies
pip install -r requirements.txt
3. Run the app
streamlit run app.py
💡 Key Features
Simple interactive UI
Fast movie recommendations
Content-based filtering approach
Easy to extend with new features
📈 Future Improvements
Add movie posters using TMDB API
Improve similarity using word embeddings (Word2Vec / BERT)
Deploy live version using Streamlit Cloud
Add search autocomplete
👩‍💻 Author
Built as a personal machine learning project exploring recommender systems and NLP techniques.
