from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem.porter import PorterStemmer


ps = PorterStemmer()


def stem(text):
    y = []

    for i in text.split():
        y.append(ps.stem(i))

    return " ".join(y)


def apply_stemming(df):
    df['tags'] = df['tags'].apply(stem)
    return df


def create_vectors(df):

    cv = CountVectorizer(max_features=5000, stop_words='english')

    vectors = cv.fit_transform(df['tags']).toarray()

    return vectors


def compute_similarity(vectors):

    similarity = cosine_similarity(vectors)

    return similarity


def recommend(movie, df, similarity):

    movie_index = df[df['title'] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended = []

    for i in movies_list:
        recommended.append(df.iloc[i[0]].title)

    return recommended