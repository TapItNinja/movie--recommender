import pickle
import pandas as pd
import streamlit as st


# def fetch_poster(movie_id):
#     response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
#     data=response.json()
#     print(data)
#     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['original_title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    # recommended_movies_posters=[]
    for i in movies_list:
        movie_id = i[0]
        #fetch poster from api


        recommended_movies.append(movies.iloc[i[0]].original_title)
        # recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies

    # for i in movie_list:
    #     print(new_df.iloc[i[0]].original_title)

movies_dict=pickle.load(open('movie_dict.pkl', 'rb'))
movies=pd.DataFrame(movies_dict)


similarity = pickle.load(open('similarity.pkl', 'rb'))


st.title('Movie Recommender System')

option = st.selectbox(
'How would you like to be contacted?',
movies['original_title'].values)

# if st.button( 'Recommend'):
#     names, posters=recommend(option)

if st.button('Recommend'):
    recommendations = recommend(option)
    for i in recommendations:
        st.write(i)

    # col1, col2, col3, col4, col5 = st.beta_columns(3)
    # with col1:
    #     st.header("A cat")
    #     st.image("https://static.streamlit.io/examples/cat.jpg")
    # with col2:
    #     st.header("A cat")
    #     st.image("https://static.streamlit.io/examples/cat.jpg")
    # with col3:
    #     st.header("A cat")
    #     st.image("https://static.streamlit.io/examples/cat.jpg")
    # with col4:
    #     st.header("A cat")
    #     st.image("https://static.streamlit.io/examples/cat.jpg")
    # with col5:
    #     st.header("A cat")
    #     st.image("https://static.streamlit.io/examples/cat.jpg")