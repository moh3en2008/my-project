import streamlit as st
from password_generator import PinCodeGenerator, RandomPasswordGenerator, MemorablePasswordGenerator


st.image("./images/banner.jpeg", width=400)
st.title(":zap: Password Generator")

option = st.radio(
    "Select a password generator",
    ("Random Password", "Memorable Password", "Pin Code")
)


if option == 'Pin Code':
    length = st.slider("Select the length of the pin code", 4, 32)
    
    generator = PinCodeGenerator(length)

elif option == 'Random Password':
    length = st.slider("Select the length of the password", 8, 100)
    include_symbol = st.toggle("Include Symbols")
    include_number = st.toggle("Include Number")
    
    generator = RandomPasswordGenerator(length, include_number, include_symbol)

elif option == 'Memorable Password':
    num_of_words = st.slider("Select the number of the words: ", 2, 10)
    separator = st.text_input("Separator", value='-')
    capitalization = st.toggle("Capitalization")

    generator = MemorablePasswordGenerator(num_of_words, separator, capitalization)

password = generator.generate()
st.write(f"Your password is: `{password}` ")
