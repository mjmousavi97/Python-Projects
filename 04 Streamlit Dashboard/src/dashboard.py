import streamlit as st 
from src.password_generator import MemorablePasswordGenerator, PinGenerator, RandomPasswordGenerator


st.image("/mnt/e/Project-based-python/Codes/Python-Projects/04 Streamlit Dashboard/images/user-access.png", width=300)
st.title(":zap: Password Generator")

option = st.radio(
    "Select a password generator",
    ("Random Password", "Memorable Password", "Pin code")
)

if option == "Pin code":
    length = st.slider("Select the length of the pin code: ", 4, 32)
    generator = PinGenerator(length)
    
elif option == "Random Password":
    length = st.slider("Select the length of the password: ", 4, 100)
    include_symbols = st.toggle("include Symbols")
    include_number = st.toggle("include Number")
    generator = RandomPasswordGenerator(length=length, include_numbers=include_number, include_symbols=include_symbols)

elif option == "Memorable Password":
    length = st.slider("Select number of words: ", 2, 10)
    separator = st.text_input("Seoerator", value="-")
    capitalization = st.toggle("Capitalization")
    generator = MemorablePasswordGenerator(number_of_words=length, separator=separator, capitalization=capitalization)

password = generator.generate()
st.write(f"Your password is: `{password}`") 