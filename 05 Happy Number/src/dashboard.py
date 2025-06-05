import streamlit as st 
from src.main import is_happy


# Display the image
st.image('images/image_1.png', width=300)

# Set the title
st.title("😊 Find Your Number’s Happiness")

# Explanation
st.caption("A happy number eventually reaches 1 by summing the squares of its digits repeatedly.")

# Number input
number = int(st.number_input("Insert a number", min_value=1, step=1))

# Button
click = st.button("Check", type="primary")

# Result
if click:
    if is_happy(number):
        st.success("🎉 Your number is happy!")
    else:
        st.error("😢 Oh! Your number is not happy.")
