# Password Generator Streamlit App

This project provides a Streamlit application for generating various types of passwords. It allows users to select from different password generation strategies, including PIN codes, random passwords, and memorable passwords. The app utilizes the `password_generator` module to generate passwords based on user input.

## Project Structure
password_generator_streamline/
|
|– src/
|   |– images/
|   |   |– banner.jpeg     # Banner image for the Streamlit app
|   |– password_generator.py  # The module with password generation classes
|   |– dashboard.py       # The Streamlit app script
|
|– README.md              # This file

## Requirements

- Python 3.7 or higher
- NLTK library (Natural Language Toolkit)
- Streamlit library

You can install the required libraries using:

```bash
pip install nltk streamlit
```

## How to Run
1.	Navigate to the project directory:
```
cd path/to/password_generator_streamline
```
2.	Run the Streamlit app:
```
streamlit run src/dashboard.py
```
3.	Open your browser and go to the URL provided by Streamlit to interact with the app.

## Features

1. Pin Generator

Generates numeric PINs of a specified length.
```
generator = PinGeneratorPassword(length=10)
print(generator.generator())  # Outputs a 10-digit PIN
```
•	Constructor Parameters:
•	length (int): The length of the numeric PIN.

2. Random Password Generator

Generates random passwords with optional inclusion of numbers and symbols.

. Usage
```
generator = RandomPasswordGenerator(length=12, include_numbers=True, include_symbols=True)
print(generator.generator())  # Outputs a random password of length 12 with numbers and symbols
```
•	Constructor Parameters:
•	include_numbers (bool): Whether to include numbers in the password.
•	include_symbols (bool): Whether to include symbols in the password.
•	length (int): The length of the password.

3. Memorable Password Generator

Generates memorable passwords using a list of words.

. Usage
```
generator = MemorablePasswordGenerator(number_of_words=4, separator='-', capitalization=True)
print(generator.generator())  # Outputs a memorable password with 4 words, separated by hyphens, with random capitalization
```

•	Constructor Parameters:
•	number_of_words (int): Number of words to include in the password.
•	separator (str): Separator between words.
•	capitalization (bool): Whether to randomly capitalize words.
•	vocabulary (list): List of words to use for generating the password. Uses NLTK words by default.

Example

The app interface allows you to:

•	Select the type of password generator from a radio button.
•	Adjust the settings for the selected generator (e.g., length, inclusion of symbols, etc.).
•	Generate and display the password based on your selections.