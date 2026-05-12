## Movie Recommendation System

A content-based Movie Recommendation System built using Python, Machine Learning, and Streamlit.

The application recommends similar movies using vectorization and cosine similarity. It also supports multiple movie preference input to generate more personalized recommendations. Movie posters and metadata are fetched dynamically using the TMDB API.

### Live Demo
https://movie-recommendation-2511.streamlit.app/


## Features

- Content-based movie recommendation system
- Cosine similarity based recommendation engine
- Multiple movie preference recommendation
- Dynamic similarity computation
- Interactive Streamlit UI
- TMDB API integration
- Dynamic movie posters and movie details
- Error handling for unavailable posters/API failures


## Tech Stack

- Python
- Pandas
- NumPy
- Pandas
- Scikit-learn
- Streamlit
- TMDB API


## Project Structure

```bash
movie-recommendation-system/
│
├── .github/
├── .streamlit/
│   └── secrets.toml
│
├── data/
│
├── app.py
├── helper.py
├── movies.pkl
├── vectors.pkl
├── preprocessing.ipynb
├── requirements.txt
├── .gitignore
├── .gitattributes
└── README.md

```