import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity 
import streamlit as st
import ast

# Load and prepare data
df = pd.read_csv('tmdb_5000_movies.csv')
df = df[['title', 'overview', 'genres', 'keywords']]
df.dropna(inplace=True)

def extract_names(text):
    try:
        items = ast.literal_eval(text)
        return ' '.join([i['name'] for i in items])
    except:
        return ''

df['genres'] = df['genres'].apply(extract_names)
df['keywords'] = df['keywords'].apply(extract_names)
df['tags'] = df['overview'] + ' ' + df['genres'] + ' ' + df['keywords']
tfidf = TfidfVectorizer(stop_words='english')
matrix = tfidf.fit_transform(df['tags'])
similarity = cosine_similarity(matrix)

movie = st.selectbox("Pick a movie:", df['title'].values)

if st.button("Recommend"):
    idx = df[df['title'] == movie].index[0]
    scores = sorted(list(enumerate(similarity[idx])), key=lambda x: x[1], reverse=True)[1:6]
    st.subheader("You might also like:")
    for i, _ in scores:
        st.write("🎥 " + df['title'][i])