import streamlit as st
import pickle
import requests
from helper import r_similarity,m_similarity


# title
st.title("Movie Recommendation System")

# load movies
movies = pickle.load(open('movies.pkl', 'rb'))


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

# recommend v.1 (update for dynamic calculation of similarity in v.2)
def recommend(movie):
    index = int(movies[movies['title'] == movie].index[0])
    similarity = r_similarity(index)
    distances = similarity[0]
    movies_list = list(sorted(enumerate(distances), key=lambda x: x[1], reverse=True))[1:6]

    movie_recommendations = []
    poster_url = []
    for movie in movies_list:
        movie_id = movies.iloc[movie[0]]['movie_id']

        movie_recommendations.append(movies.iloc[movie[0]]['title'])
        poster_url.append(fetch_poster(movie_id))

    return movie_recommendations , poster_url

# recommend multiple v.2
def recommend_multple(selected_movies):
    similarities = m_similarity(selected_movies)
    movie_indices = similarities.argsort()[::-1][:20]

    recommendations = []
    poster_url = []
    for index in movie_indices:
        title = movies.iloc[index]['title']

        # remove already selected movies
        if title not in selected_movies:
            movie_id = movies.iloc[index]['movie_id']

            poster_url.append(fetch_poster(movie_id))
            recommendations.append(title)

        if len(recommendations) == 5:
            break
    return recommendations, poster_url

# movies list
total_movies = movies['title'].values.tolist()


st.write("Select up to 5 movies : ")
col1, col2 = st.columns([6,2])
# movies multi select box
with col1:
    movie = st.multiselect("Select up to 5 movies : ",total_movies, label_visibility="collapsed",max_selections=5)

with col2:
    recommend_btn = st.button("Recommend",use_container_width=True)

# button
if recommend_btn:
    if len(movie) == 0:
        st.warning("Please select at least one movie")
    elif len(movie) > 5:
        st.warning("You can select at most 5 movies")
    else:
        names, posters = recommend_multple(movie)

        st.write("Recommended Movies : ")
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

