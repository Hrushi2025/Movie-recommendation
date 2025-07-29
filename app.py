import streamlit as st
import pickle as pkl
import pandas as pd
import requests


def fetch_poster(movie_id):
    try:
        url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=87196f196bf9be6f2d96f4f550ed740a'
        response = requests.get(url)
        print(f"Fetching poster for ID: {movie_id}, Status Code: {response.status_code}")
        data = response.json()
        print(data)
        poster_path = data.get('poster_path')
        if poster_path:
            return f'https://image.tmdb.org/t/p/w500{poster_path}'
        else:
            return "https://via.placeholder.com/500x750?text=No+Poster"
    except Exception as e:
        print(f"Error for movie ID {movie_id}: {e}")
        return "https://via.placeholder.com/500x750?text=Error"


# 🎥 Recommend similar movies
def recommd(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]]['movie_id']
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_poster


# 📦 Load data
with open('movie_dict.pkl', 'rb') as f:
    movies_dict = pkl.load(f)

with open('similarity.pkl', 'rb') as f:
    similarity = pkl.load(f)

movies = pd.DataFrame(movies_dict)

# 🖼 Streamlit UI
st.title('Movie Recommendation System')

selectMoviesName = st.selectbox('Select a movie:', movies['title'].values)

if st.button('Recommend'):
    names, posters = recommd(selectMoviesName)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])
