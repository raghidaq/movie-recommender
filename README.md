# 🎬 Movie Recommendation System

A **content-based movie recommender system** that suggests similar movies based on genre, plot, and keywords using **TF-IDF vectorization and cosine similarity**.
<img width="1064" height="558" alt="Screenshot 2026-06-09 at 04 00 34" src="https://github.com/user-attachments/assets/be014798-c7fb-400b-9564-16eee5222f0c" />

---

## 📌 Project Overview

This project recommends movies by analyzing textual features such as:

* Movie overview
* Genres
* Keywords

These features are combined into a single text representation, then converted into numerical vectors using **TF-IDF**, and compared using **cosine similarity** to find the most similar movies.

---

## ⚙️ How It Works

1. Clean and preprocess movie dataset
2. Extract meaningful text features (genres, keywords, overview)
3. Combine features into a single “tag”
4. Apply TF-IDF vectorization
5. Compute cosine similarity between all movies
6. Recommend top 5 most similar movies

---

## 🎯 Example Output

* Avatar → *Aliens, Moonraker, Mission to Mars...*
* The Dark Knight → *Batman Begins, The Dark Knight Rises...*

---

## 🛠️ Technologies Used

* Python 🐍
* Pandas
* NumPy
* Scikit-learn

  * TF-IDF Vectorizer
  * Cosine Similarity
* Streamlit (for web app interface)

---

## 📊 Dataset

TMDB 5000 Movies Dataset (Kaggle) containing:

* Titles
* Genres
* Overviews
* Keywords

---

## 🚀 How to Run

### 1. Clone repository

```bash
git clone https://github.com/raghidaq/movie-recommender.git
cd movie-recommender
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

---

## 💡 Key Features

* Simple interactive UI
* Fast movie recommendations
* Content-based filtering approach
* Easy to extend with new features

---

## 📈 Future Improvements

* Add movie posters using TMDB API
* Improve similarity using word embeddings (Word2Vec / BERT)
* Deploy live version using Streamlit Cloud
* Add search autocomplete

---

## 👩‍💻 Author

Built as a personal machine learning project exploring recommender systems and NLP techniques.

