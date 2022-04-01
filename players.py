from tempfile import NamedTemporaryFile
from xml.dom.minidom import Identified
from Hangman import user_col, hangdb
import json


class player:
    def __init__(self, name, email, play_points):
        self.name = name
        self.email = email
        self.play_points = play_points


def new_player_sign_up():
    print("New player sign up! ")
    ##check for correct input
    x, y = 0, 0
    while x == 0:
        x = input("\tWhat would you like USER NAME to be? (max 20 char) : ")
        if len(x) > 20:
            print("Too many charaters!")
            x = 0

    y = input("\tWhat email address would you like to use? : ")

    ## Create new player
    new_user = player(x, y, 100)

    ##Add new player to dictionary
    dict = {"userName": x, "email": y, "playPTS": 100}

    hangdb.user_col.insert_one(dict)

    return new_user.name, new_user.play_points, new_user.email


def sign(player_name, player_email):
    result = hangdb.user_col.find_one({"userName": player_name, "email": player_email})
    if result == None:
        signed = "unsigned"
        return signed
    return "signed"


def returning_player_sign_in(player_name, player_email):
    # db.check login and playpoint status

    result = hangdb.user_col.find_one({"userName": player_name, "email": player_email})

    # check if list is empty or not?
    # if it is not empty, then proceed.
    play_points = result["playPTS"]
    return player_name, play_points, player_email
    # for x in range(len(db_x)):
    #     if db_x[x] == player_name:
    #         if db_y[x] == player_email:
    #             return db_x[x] ,db_pp[x]
    #         else:
    #             print("You have entered the wrong email, please try again")
    #             return "unsigned"1
