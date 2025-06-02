import random
import string
from abc import ABC, abstractmethod

from wordfreq import top_n_list


class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass


class PinGenerator(PasswordGenerator):
    def __init__(self, length):
        self.length = length
        
    def generate(self):
        return ''.join([random.choice(string.digits) for _ in range(self.length)])   


class RandomPasswordGenerator(PasswordGenerator):
    def __init__(self, length: int = 8, include_numbers: bool = False, include_symbols: bool = False):
        self.length = length
        self.characters = string.ascii_letters
        if include_numbers:
            self.characters += string.digits
        if include_symbols:
            self.characters += string.punctuation

    def generate(self):
        return ''.join([random.choice(self.characters) for _ in range(self.length)])


common_words = top_n_list('en', 1000)

class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(
        self,
        number_of_words: int = 4,
        separator: str = '_', 
        capitalization: bool = False, 
        vocabulary: list = common_words[0:1000]
    ):
    
        self.num_of_words = number_of_words
        self.capitalize = capitalization
        self.separator = separator
        self.vocabulary = vocabulary

    def generate(self):
        password_words = [random.choice(self.vocabulary) for _ in range(self.num_of_words)]
        if self.capitalize:
            password_words = [word.upper() if random.choice([True, False]) else word.lower() for word in password_words]
        
        return self.separator.join(password_words)


def test_random_password_generator():
    random_gen = RandomPasswordGenerator(length=10, include_numbers=True, include_symbols=True)
    password = random_gen.generate()
    print(password)
    assert len(password) == 10
    assert any(char in string.ascii_uppercase for char in password)
    assert any(char in string.digits for char in password)


def test_memorable_password_generator():
    memorable_gen = MemorablePasswordGenerator(
        number_of_words=4,
        separator="-",
        capitalization=True,
        vocabulary=common_words[0:1000],
    )
    password = memorable_gen.generate()
    print(password)
    assert len(password.split('-')) == 4


def test_pincode_generator():
    pin_gen = PinGenerator(length=4)
    pin = pin_gen.generate()
    print(pin)
    assert len(pin) == 4
    assert all(char in string.digits for char in pin)


def main():
    print("Testing RandomPasswordGenerator:")
    test_random_password_generator()
    print("Testing MemorablePasswordGenerator:")
    test_memorable_password_generator()
    print("Testing PinCodeGenerator:")
    test_pincode_generator()


if __name__ == "__main__":
    main()