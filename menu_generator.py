import requests
import streamlit as st

# Replace with your own Spoonacular API Key
API_KEY = "8f2cc897811c77dac235cb512a98c5b7dfd9f4bc"

def generate_menu(grocery_items):
    endpoint = "https://api.spoonacular.com/recipes/findByIngredients"
    
    params = {
        "apiKey": API_KEY,
        "ingredients": ",".join(grocery_items),
        "number": 5,  # Number of recipes to fetch
    }
    
    response = requests.get(endpoint, params=params)
    
    if response.status_code == 200:
        recipes = response.json()
        return recipes
    else:
        return None

# Create a Streamlit app
st.title("Menu Generator based on Grocery Items")

# Input box for users to list their available grocery items
user_input = st.text_area("Enter the grocery items you have available (comma-separated):")

# Convert user input into a list of items
grocery_items = [item.strip() for item in user_input.split(',') if item.strip()]

if grocery_items:
    # Generate a menu based on the user's grocery items
    recipes = generate_menu(grocery_items)

    if recipes:
        st.header("Generated Menu:")
        for recipe in recipes:
            st.write(f"- {recipe['title']}")
    else:
        st.warning("Unable to fetch menu. Please check your API key or try again later.")
else:
    st.warning("Please enter some grocery items in the input box above.")
  
