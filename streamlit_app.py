import streamlit

streamlit.title('My parents new healthy diner')

streamlit.header('Breakfast favourites')
streamlit.text('🥣Omega 3 & bluberry oatmeal')
streamlit.text('🥗🍞Kale, Spinach & Rocket Smoothie')
streamlit.text('🥑🐔Hard boiled free range Egg')
 
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
