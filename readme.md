# 🎬 AI Movie Recommendation System

An intelligent **content-based movie recommendation system** built using **Machine Learning, NLP, and Streamlit** that suggests movies similar to the one a user selects.

The system analyzes movie **genres, cast, keywords, director, and overview** to compute similarity between movies and recommend the most relevant ones.

---

# 📌 Project Overview

Recommendation systems power platforms like  **Netflix, Amazon Prime, and Spotify** .
This project demonstrates how such systems can be built using  **Natural Language Processing and cosine similarity** .

The model analyzes movie metadata and finds **semantic similarity** between movies to generate recommendations.

Example:

If you select  **Avatar** , the system may recommend:

* Guardians of the Galaxy
* John Carter
* Star Trek
* Jupiter Ascending
* The Fifth Element

---

# 🧠 How It Works

The recommendation pipeline follows these steps:

1️⃣ Load movie datasets
2️⃣ Merge movie and credit datasets
3️⃣ Extract important features
4️⃣ Perform text preprocessing
5️⃣ Generate movie tags
6️⃣ Convert text to vectors using **CountVectorizer**
7️⃣ Compute similarity using **Cosine Similarity**
8️⃣ Recommend top similar movies

---

# 🏗 Project Architecture

```
User selects movie
        │
        ▼
Load processed movie dataset
        │
        ▼
Find movie index
        │
        ▼
Compute similarity scores
        │
        ▼
Sort movies by similarity
        │
        ▼
Return Top 5 Recommendations
        │
        ▼
Fetch posters & trailers using TMDB API
        │
        ▼
Display results in Streamlit UI
```

---

# 📂 Project Structure

```
movie-recommender-system
│
├── app.py                     # Streamlit application
├── train_model.py             # Model training pipeline
├── requirements.txt
├── README.md
│
├── data
│   ├── raw
│   │   ├── tmdb_5000_movies.csv
│   │   └── tmdb_5000_credits.csv
│   │
│   └── processed
│       ├── movies_dict.pkl
│       └── similarity.pkl
│
├── notebooks
│   └── movie_recommendation_system.ipynb
│
├── src
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── recommender.py
│   └── utils.py
│
└── assets
    └── screenshots
```

---

# 📊 Dataset

Dataset used: **TMDB 5000 Movie Dataset**

Contains:

* Movie titles
* Genres
* Keywords
* Cast
* Crew
* Overview
* Popularity metrics

Source:
[https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

---

# ⚙️ Tech Stack

**Programming**

* Python

**Machine Learning**

* Scikit-learn
* Cosine Similarity
* CountVectorizer

**Data Processing**

* Pandas
* NumPy
* NLP preprocessing

**Frontend**

* Streamlit

**API Integration**

* TMDB API (for posters & trailers)

---

# 🎥 Features

✔ Content-based movie recommendation
✔ Modern **Streamlit UI**
✔ Movie posters fetched from TMDB API
✔ Movie overview and ratings
✔ Trailer links
✔ Trending movies section
✔ Fast similarity search

---

# 📸 Application Preview

Example:

<img width="959" height="539" alt="movei-rec" src="https://github.com/user-attachments/assets/cf564676-0cb1-4c6d-bb52-20dab2b30559" />

<img width="959" height="539" alt="movie-rec2" src="https://github.com/user-attachments/assets/ddda3e9a-05b7-4a32-b285-342238672551" />


---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/samarthakur412/movie-recommender-system.git
cd movie-recommender-system
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

# 🧪 Model Training

To retrain the model:

```bash
python train_model.py
```

This will generate:

```
movies_dict.pkl
similarity.pkl
```

---

# 📈 Future Improvements

* Collaborative filtering recommendations
* Deep learning recommender system
* User login & watchlist
* Genre-based filtering
* Personalized recommendations
* Netflix-style UI

---

# 💡 Learning Outcomes

Through this project I learned:

* Building recommendation systems
* Natural Language Processing for feature engineering
* Cosine similarity and vector space models
* Building interactive ML apps with Streamlit
* API integration in ML projects
* Structuring production-ready ML repositories

---

# 👨‍💻 Author

**Sammy**

Machine Learning & AI Enthusiast

GitHub: https://github.com/samarthakur412
LinkedIn: https://www.linkedin.com/in/samarjeet-singh-1908551b7

---

# ⭐ Support

If you like this project, please consider **starring the repository** ⭐
It helps others discover the project and motivates further development.

---
