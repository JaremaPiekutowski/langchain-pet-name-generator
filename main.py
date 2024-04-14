import langchain_helper as lch
import streamlit as st

# Set the title of the web app
st.title("Pet Name Generator 🐈")

# Create a sidebar with two select boxes
# The first select box will have the animal type
animal_type = st.sidebar.selectbox(
    "What is your pet?",
    ("Cat", "Dog", "Hamster", "Mouse", "Fish", "Snake", "Spider", "Parrot"),
)

# The second select box will have the color of the pet
pet_color = st.sidebar.selectbox(
    "What is the color of your pet?",
    (
        "Black",
        "White",
        "Brown",
        "Ginger",
        "Green",
        "Gray",
        "Patchy",
        "Blue",
        "Purple",
        "Orange",
        "Pink",
        "Grey",
        "Gold",
        "Silver",
        "Rainbow",
    ),
)

# Create a button to generate the pet names
if st.button("Generate Names"):
    # Get the pet names from the langchain_helper
    response = lch.generate_pet_names(animal_type, pet_color)
    # Display the pet names
    st.text(response["pet_names"])
