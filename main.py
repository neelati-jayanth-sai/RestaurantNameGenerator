import streamlit as st
from langchain_helper import generate_restaurant_name_and_menu_items

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a cuisine", (
"Italian", "French", "Chinese", "Japanese", "Indian", "Mexican", "Thai", "Mediterranean", "Greek", "Middle Eastern"))

# def generate_restauratnt_name_and_menu(cuisine):
#     return {
#         'restaurant_name':"gsdfgdf",
#         "menu_items":"gsdfgsdf, dfafasfsa"
#     }

if cuisine:
    response = generate_restaurant_name_and_menu_items(cuisine)
    st.header(response["restaurant_name"])
    menu_items = response["menu_items"]
    st.write("Menu Items")
    st.write(menu_items)
