import streamlit

streamlit.title('My parents new healthy diner')

streamlit.header('Breakfast favourites')
streamlit.text('🥣Omega 3 & bluberry oatmeal')
streamlit.text('🥗🍞Kale, Spinach & Rocket Smoothie')
streamlit.text('🥑🐔Hard boiled free range Egg')
 
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")


# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_selected)
