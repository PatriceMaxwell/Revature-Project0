from pymongo import MongoClient
import Open
import Menu

myclient = MongoClient("mongodb://localhost:27017")

hangdb = myclient["Hangman_db"]
user_col = hangdb["players"]


def start():
    Open
    Menu


start()
