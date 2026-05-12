from sklearn.metrics.pairwise import cosine_similarity
import pickle
import numpy as np

vectors = pickle.load(open('vectors.pkl', 'rb'))
movies = pickle.load(open('movies.pkl', 'rb'))

# similarity
def r_similarity(index):
    movie_vector = vectors[index]
    similarity = cosine_similarity([movie_vector],vectors)
    return similarity

# for multiple movies
def m_similarity(selected_movies):
    movies_vectors = []
    for movie in selected_movies:
        index = movies[movies['title'] == movie].index[0]
        movies_vectors.append(vectors[index])

    user_vector = np.mean(movies_vectors, axis=0)
    similarities = cosine_similarity([user_vector],vectors)[0]

    return similarities