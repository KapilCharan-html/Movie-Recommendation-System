import streamlit as st
import pickle
import requests

# Load data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# TMDb API Key
API_KEY = 'bef8dbf1a67fb3a503efabb8dbb3f54a'

# Cached poster fetch
@st.cache_data(show_spinner=False)
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return "https://via.placeholder.com/500x750.png?text=No+Poster"
    except requests.exceptions.RequestException as e:
        print("Poster fetch error:", e)
        return "https://via.placeholder.com/500x750.png?text=Connection+Error"

# Recommend function (returns exactly 5 valid posters)
def recommend(movie):
    movie = movie.lower()
    if movie not in movies['title'].str.lower().values:
        st.error("❌ Movie not found in the database.")
        return [], []

    idx = movies[movies['title'].str.lower() == movie].index[0]
    distances = similarity[idx]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:20]  # top 20 similar

    recommended_movies = []
    recommended_posters = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        title = movies.iloc[i[0]].title
        poster = fetch_poster(movie_id)

        if "placeholder.com" in poster:
            continue  # Skip broken poster

        recommended_movies.append(title)
        recommended_posters.append(poster)

        if len(recommended_movies) == 5:
            break

    return recommended_movies, recommended_posters

# Streamlit UI setup
st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")
st.title("🎬 Movie Recommendation System")
st.markdown("#### Select a movie and get 5 similar movie recommendations with posters")

# Dropdown movie selector
movie_list = movies['title'].values
selected_movie_name = st.selectbox("Choose a movie", sorted(movie_list))

# On button click, show recommendations
if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    # Display results in 5 columns
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            title = names[i] if i < len(names) else "Not Available"
            poster = posters[i] if i < len(posters) else "https://via.placeholder.com/500x750.png?text=No+Poster"
            st.text(title)
            st.image(poster)
