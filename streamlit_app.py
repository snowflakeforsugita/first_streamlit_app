import streamlit
import pandas
streamlit.title("This is a demo page")
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some Fruits :", list(my_fruit_list.index),['Avocado','Grapes']) 
