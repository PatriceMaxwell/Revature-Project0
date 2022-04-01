from distutils.log import error
import time
import sys
from unicodedata import name
from utils import menu_validation
import utils

from black import err


def scroll_text1(text):
    for char in str(text):
        sys.stdout.write(char)
        time.sleep(0.1)
        sys.stdout.flush()


f = open("C:\\Users\\patri\\Codex\\Revature\\Project0\\hangman0.txt", "r+")
file_name = f.read()
print(file_name)

f.close()

scroll_text1("Welcome to Hangman!")

session = menu_validation(3)
