from distutils.log import error
import imp
from unicodedata import name
from black import err
from Open import session
from gamePlay import player_mode

# session = 2
from utils import menu_validation
from players import new_player_sign_up, returning_player_sign_in, sign


def new_player():
    plyer1_name, plyer1_ppts, plyer_email = new_player_sign_up()
    print("How would you like to play? \n \t 1: Vs Computer \n \t 2: Player Vs Player ")
    game_play = menu_validation(2)
    player_mode(game_play, plyer1_name, plyer1_ppts, plyer_email)


def returning_player():

    # sign in
    print("Sign-in!")
    signed = "unsigned"

    while signed == "unsigned":
        uname = input("\tPlease enter your USER NAME :")
        uemail = input("\tPlease enter your email :")
        signed = sign(uname, uemail)

    plyer1_name, plyer1_ppts, plyer1_email = returning_player_sign_in(uname, uemail)

    # how would you like to play
    print("How would you like to play? \n \t 1: Vs Computer \n \t 2: Player Vs Player ")
    game_play = menu_validation(2)
    player_mode(game_play, plyer1_name, plyer1_ppts, plyer1_email)


def player_2_signin():
    plyer2_name, plyer2_ppts, plyer2_email = new_player_sign_up()
    return plyer2_name, plyer2_ppts, plyer2_email


def player_2_return():

    # sign in
    print("Sign-in!")
    signed = "unsigned"

    while signed == "unsigned":
        uname = input("\tPlease enter your USER NAME :")
        uemail = input("\tPlease enter your email :")
        signed = sign(uname, uemail)
        plyer2_name, plyer2_ppts, plyer2_email = returning_player_sign_in(uname, uemail)

    return plyer2_name, plyer2_ppts, plyer2_email


def rules():

    f = open("rules.txt", "r+")
    file_read = f.read()
    print(file_read)

    f.close()
    import Hangman


def exit():
    import exit


# menu_dict = {0: exit(), 1: new_player(), 2: returning_player(), 3: rules()}

# choice = menu_dict[session]
# print(choice)

if session == 1:
    new_player()
elif session == 2:
    returning_player()
elif session == 3:
    rules()
# elif session == 4:
#     player_2_signin()
# elif session == 5:
#     player_2_return()
else:
    exit()
