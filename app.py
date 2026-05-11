import streamlit as st
import pickle
import requests


# title
st.title("Movie Recommendation System")

# load movies
movies = pickle.load(open('movies.pkl', 'rb'))

#load similarity vector
similarity = pickle.load(open('similarity.pkl', 'rb'))

# reusable session
session = requests.Session()
# fetch poster
def fetch_poster(movie_id):
    key = st.secrets["TMDB_API_KEY"]

    headers = {
        "accept": "application/json",
        "Authorization": key
    }
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"

    try:
        response = session.get(url, headers=headers, timeout=20)
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path is None:
            return "https://via.placeholder.com/500x750?text=Image+Not+Available"
        return "https://image.tmdb.org/t/p/w500/" + poster_path

    except requests.exceptions.RequestException:
        # fallback image instead of crashing
        return "https://via.placeholder.com/500x750?text=Connection+Error"

# recommend
def recommend(movie):
    index = int(movies[movies['title'] == movie].index[0])
    distances = similarity[index]
    movies_list = list(sorted(enumerate(distances), key=lambda x: x[1], reverse=True))[1:6]

    movie_recommendations = []
    poster_url = []
    for movie in movies_list:
        movie_id = movies.iloc[movie[0]]['movie_id']

        movie_recommendations.append(movies.iloc[movie[0]]['title'])
        poster_url.append(fetch_poster(movie_id))

    return movie_recommendations , poster_url

# movies list
total_movies = movies['title'].values.tolist()

# movies select box
movie  = st.selectbox("Select Movie", total_movies)

# button
if st.button("recommend"):
    names,posters = recommend(movie)

    # show movie and poster
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])

