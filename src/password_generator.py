import random
import string
from abc import ABC, abstractmethod
from typing import List, Optional

import nltk  # type: ignore

# Download the list of words from the NLTK corpus (only the first time this runs)
nltk.download("words")


class PasswordGenerator(ABC):
    """
    Abstract base class for all password generators.
    Defines a common interface that all subclasses must implement.
    """

    @abstractmethod
    def generator(self) -> str:
        """
        Generate a password.
        
        :return: The generated password as a string.
        """
        pass


class PinGeneratorPassword(PasswordGenerator):
    """
    Password generator for numeric PIN codes.
    Generates a string consisting only of digits.
    """

    def __init__(self, length: int) -> None:
        """
        Initialize the PIN generator with a specific length.

        :param length: Length of the PIN (number of digits).
        """
        self.length: int = length

    def generator(self) -> str:
        """
        Generate a numeric PIN of the specified length.

        :return: A string representing the numeric PIN.
        """
        # Randomly select digits to build the PIN
        return "".join(random.choice(string.digits) for _ in range(self.length))


class RandomPasswordGenerator(PasswordGenerator):
    """
    Password generator that creates random passwords with optional
    inclusion of numbers and/or symbols.
    """

    def __init__(
        self,
        length: int = 8,
        include_numbers: bool = False,
        include_symbols: bool = False,
    ) -> None:
        """
        Initialize the random password generator.

        :param length: Length of the password (minimum 1).
        :param include_numbers: Whether to include digits in the password.
        :param include_symbols: Whether to include punctuation/symbols in the password.
        """
        self.length: int = length
        self.include_numbers: bool = include_numbers
        self.include_symbols: bool = include_symbols

        # Start with alphabetic characters
        self.characters: str = string.ascii_letters

        # Add digits and symbols if requested
        if self.include_numbers:
            self.characters += string.digits
        if self.include_symbols:
            self.characters += string.punctuation

    def generator(self) -> str:
        """
        Generate a random password using the selected character sets.

        :return: A string representing the random password.
        """
        # Randomly select characters from the pool
        return "".join(random.choice(self.characters) for _ in range(self.length))


class MemorablePasswordGenerator(PasswordGenerator):
    """
    Password generator that creates more 'memorable' passwords
    by combining dictionary words instead of random characters.
    """

    def __init__(
        self,
        number_of_words: int = 4,
        separator: str = "-",
        capitalization: bool = False,
        vocabulary: Optional[List[str]] = None,
    ) -> None:
        """
        Initialize the memorable password generator.

        :param number_of_words: Number of words to include in the password.
        :param separator: Character(s) used to separate the words.
        :param capitalization: Whether to randomly capitalize words.
        :param vocabulary: Custom list of words. If None, NLTK's words corpus is used.
        """
        if vocabulary is None:
            vocabulary = nltk.corpus.words.words()

        self.number_of_words: int = number_of_words
        self.separator: str = separator
        self.capitalization: bool = capitalization
        self.vocabulary: List[str] = vocabulary

    def generator(self) -> str:
        """
        Generate a memorable password based on the specified criteria.

        :return: A string representing the memorable password.
        """
        # Randomly select words from the vocabulary
        password_words = [random.choice(self.vocabulary) for _ in range(self.number_of_words)]

        # Optionally randomize capitalization
        if self.capitalization:
            password_words = [
                word.upper() if random.choice([True, False]) else word.lower()
                for word in password_words
            ]

        # Join the words using the specified separator
        return self.separator.join(password_words)


if __name__ == "__main__":
    # Example usage of the password generators

    # Generate a numeric PIN of length 10
    p = PinGeneratorPassword(length=10)
    print("PIN:", p.generator())

    # Generate a random password with symbols and numbers
    r = RandomPasswordGenerator(length=12, include_numbers=True, include_symbols=True)
    print("Random Password:", r.generator())

    # Generate a memorable password with 4 words and capitalization
    m = MemorablePasswordGenerator(number_of_words=4, capitalization=True)
    print("Memorable Password:", m.generator())