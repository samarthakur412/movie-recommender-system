from src.data_preprocessing import *
from src.feature_engineering import *
from src.recommender import *
from src.utils import *

movies, credits = load_datasets(
    "data/raw/tmdb_5000_movies.csv",
    "data/raw/tmdb_5000_credits.csv"
)

movies = merge_datasets(movies, credits)

movies = select_features(movies)

movies = preprocess_columns(movies)

movies = remove_spaces(movies)

new_df = create_tags(movies)

new_df = apply_stemming(new_df)

vectors = create_vectors(new_df)

similarity = compute_similarity(vectors)

save_pickle(new_df.to_dict(), "data/processed/movies_dict.pkl")

save_pickle(similarity, "data/processed/similarity.pkl")