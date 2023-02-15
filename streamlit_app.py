import streamlit
import pandas
streamlit.title("This is a demo page")
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Let's put a pick list here so they can pick the fruit they want to include 
# Display the table on the page.
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avacado'])

fruits_to_show = my_fruit_list.loc[fruits_selected]
#streamlit.dataframe(my_fruit_list)
