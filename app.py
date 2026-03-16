import streamlit as st
import pickle
import pandas as pd
import requests
from config import config

API_KEY = config['api_key']
NUM_RECOMMENDATIONS = config['num_recommendations']

st.set_page_config(
    page_title="AI Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# -------------------- CSS STYLE --------------------

st.markdown("""
<style>

.main {
    background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
}

.title {
    text-align:center;
    font-size:60px;
    font-weight:bold;
    color:white;
}

.subtitle{
    text-align:center;
    color:#d1d1d1;
    font-size:20px;
}

.card {
    background: rgba(255,255,255,0.08);
    border-radius:20px;
    padding:15px;
    backdrop-filter: blur(10px);
    transition:0.3s;
}

.card:hover{
    transform: scale(1.05);
}

.rating{
    color:#FFD700;
    font-size:18px;
}

</style>
""", unsafe_allow_html=True)

# -------------------- LOAD DATA --------------------

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))



# -------------------- API FUNCTIONS --------------------

def fetch_movie_details(movie_id):

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"

    data = requests.get(url).json()

    poster = "https://image.tmdb.org/t/p/w500/" + data['poster_path']

    rating = data['vote_average']

    overview = data['overview']

    return poster, rating, overview


def fetch_trailer(movie_id):

    url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={API_KEY}"

    data = requests.get(url).json()

    for video in data['results']:
        if video['type'] == "Trailer":
            return "https://www.youtube.com/watch?v=" + video['key']

    return None


# -------------------- RECOMMENDER --------------------

def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(list(enumerate(distances)),
                         reverse=True,
                         key=lambda x: x[1])[1:6]

    rec_movies = []

    for i in movies_list:

        movie_id = movies.iloc[i[0]].movie_id

        title = movies.iloc[i[0]].title

        poster, rating, overview = fetch_movie_details(movie_id)

        trailer = fetch_trailer(movie_id)

        rec_movies.append({
            "title":title,
            "poster":poster,
            "rating":rating,
            "overview":overview,
            "trailer":trailer
        })

    return rec_movies


# -------------------- TRENDING MOVIES --------------------

def get_trending():

    url = f"https://api.themoviedb.org/3/trending/movie/day?api_key={API_KEY}"

    data = requests.get(url).json()

    trending = []

    for movie in data['results'][:5]:

        poster = "https://image.tmdb.org/t/p/w500/" + movie['poster_path']

        trending.append((movie['title'],poster))

    return trending


# -------------------- HEADER --------------------

st.markdown('<p class="title">🎬 AI Movie Recommender</p>', unsafe_allow_html=True)

st.markdown('<p class="subtitle">Discover movies using Machine Learning</p>', unsafe_allow_html=True)

st.write("")

# -------------------- TRENDING --------------------

st.subheader("🔥 Trending Movies")

trending = get_trending()

cols = st.columns(5)

for i in range(5):
    with cols[i]:
        st.image(trending[i][1])
        st.write(trending[i][0])

st.write("---")


# -------------------- SEARCH MOVIE --------------------

selected_movie_name = st.selectbox(
    "🔍 Search your favourite movie",
    movies['title'].values
)


# -------------------- RECOMMEND --------------------

if st.button("✨ Show Recommendations"):

    with st.spinner("Finding perfect movies for you... 🍿"):

        recommendations = recommend(selected_movie_name)

    st.subheader("🎯 Recommended For You")

    cols = st.columns(5)

    for i in range(5):

        with cols[i]:

            movie = recommendations[i]

            st.image(movie["poster"])

            st.markdown(f"**{movie['title']}**")

            st.markdown(f"<p class='rating'>⭐ {movie['rating']}</p>",unsafe_allow_html=True)

            st.caption(movie["overview"][:120] + "...")

            if movie["trailer"]:
                st.link_button("▶ Watch Trailer", movie["trailer"])


# -------------------- FOOTER --------------------

st.markdown("---")

st.markdown(
"""
<center>

Built with ❤️ using  
**Machine Learning • Streamlit • TMDB API**

</center>
""",
unsafe_allow_html=True
)