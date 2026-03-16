import pandas as pd


def load_datasets(movies_path, credits_path):
    movies = pd.read_csv(movies_path)
    credits = pd.read_csv(credits_path)
    return movies, credits


def merge_datasets(movies, credits):
    movies = movies.merge(credits, on='title')
    return movies


def select_features(movies):

    movies = movies[['movie_id',
                     'title',
                     'overview',
                     'genres',
                     'keywords',
                     'cast',
                     'crew']]

    movies.dropna(inplace=True)

    return movies