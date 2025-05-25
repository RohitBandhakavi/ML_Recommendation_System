import streamlit as st
import pickle
import requests

def fetch_posters(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movie_list[movie_list['title'] == movie].index[0]  # fetch index of the given movie
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1]) # similarity scores with all other movies


    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movie_list.iloc[i[0]].id

        recommended_movie_names.append(movie_list.iloc[i[0]].title)  # get title using index
        # fetching poster from API.
        recommended_movie_posters.append(fetch_posters(movie_id))
    return recommended_movie_names, recommended_movie_posters


st.header("Movie Recommender")
movie_list = pickle.load(open('movie.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_title = movie_list['title'].values



st.title('Movie Recommender System')
selected_movie = st.selectbox(
    'Type or Select Movie',
    movie_title
 )
if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])




