import streamlit
import pandas
import requests

streamlit.title('My Parents New Health Diner') 
streamlit.header('Breakfast Menu') 
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal') 
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie') 
streamlit.text('🐔 Hard-Boiled Free-Range Egg') 
streamlit.text('🥑🍞 Avocado Toast')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
#Let's put a pick list here so they can pick the fruit they want to include
fruits_selected=streamlit.multiselect("Pick some fruit: ",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
#display the table on the page
streamlit.dataframe(my_fruit_list)

streamlit.header('Fruityvice Fruit Advice')
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi")

# It creates a table for the json format
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# creates a dataframe
streamlit.dataframe(fruityvice_normalized)


