import streamlit as st
from src.password_generator import PinGeneratorPassword, RandomPasswordGenerator, MemorablePasswordGenerator

st.image("/Users/mahnaz/students_work/streamlit_password_generator/src/images/banner.jpeg")
st.title(":zap: Password Generator")

option = st.radio("Select a password generator",
                ("Random Password", "Memorable Password", "Pin Code"))

if option == "Pin Code":
    length = st.slider("Select the length of the Pin Code", 4, 32)
    generator = PinGeneratorPassword(length)
elif option == "Random Password":
    length = st.slider("Select the length of the password", 8, 100)
    include_number = st.toggle("Include Numbers")
    include_symbol = st.toggle("Include symbols")
    generator = RandomPasswordGenerator(length, include_number, include_symbol)
elif option == "Memorable Password":
    number_of_words = st.slider("Select number of words:", 2, 10)
    separator = st.text_input("Separator", value = "_")
    capitalization = st.toggle("Capitalization")
    generator = MemorablePasswordGenerator(number_of_words, separator, capitalization)

password = generator.generator()
st.write(f"Your password is : ``` {password}``` ")