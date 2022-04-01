from cmath import e
from itertools import count
from pymongo import MongoClient
import random

myclient = MongoClient("mongodb://localhost:27017")


dictionay = myclient["Hangman_db"]
words_col = dictionay["Dictionary_col"]


def point_value(char_count: int) -> int:
    if char_count > 3:
        j = char_count / 3
        j = j * 20
        return j
    else:
        return 10


def getWord():
    rand = random.randint(0, 36)
    y = 0
    letters = []
    for x in words_col.find():
        y = y + 1

        if y == rand:
            word = x["word"]
            char_count = int(x["char_count"])
            phrase = x["definition"]
            ptvalue = int(point_value(char_count))

            for char in word:
                letters.append(char)

            return word, char_count, ptvalue, phrase, letters


def makeLett(word: str) -> list:
    letters = []

    for char in word:
        letters.append(char)
    return letters
