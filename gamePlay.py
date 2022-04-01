from pickle import GLOBAL
from utils import menu_validation
from Menu_2 import player_2_signin, player_2_return
from Hangman import myclient, user_col, hangdb
from dictSort import getWord, makeLett


correct = []
incorrect = []


def pvc(p1_name, p1_pts, p1_email):
    word, length, point_val, phrase, letters = getWord()
    word_completed = []
    print(
        f"Hey {p1_name} , Your word is {length} charaters long!(worth {point_val} points)\n  Here is the definition : {phrase}"
    )
    stat = "playing"
    chance_left = 7
    correct = [None] * len(letters)
    while stat == "playing":
        guess = input("guess away : ")

        ##Cleaning: Could make this require single char input
        if guess in word_completed:
            guess = input("Already in your correct answer ! Guess again : ")

        stat, correct, incorrect, chance_left, letters, flash, word_completed = playing(
            guess, letters, chance_left, correct, word_completed
        )

        print(flash)
        ### Working haulted here :=>

        print(correct, "Tried Incorrect Letters: ", incorrect)

    if stat == "winner":
        print(flash)
        ppoint = p1_pts + point_val
        result = hangdb.user_col.find_one({"userName": p1_name, "email": p1_email})
        hangdb.user_col.update_one(
            {"userName": p1_name, "email": p1_email}, {"$set": {"playPTS": ppoint}}
        )

    if stat == "lost":
        print(flash)
        import exit


def pvp(p1_name, p1_pts, p1_email, p2_name, p2_pts, p2_email):
    chance_left = 7
    word_completed = []
    print(
        f"Hey {p1_name} , you will be player 1! \n \t You have {p1_pts},"
    )  # Cleaning :Could points< wager madatory
    wager = int(input("How many would you like to wager? :"))
    word = input("What  word do you want to give them : ")
    definition = input("Now give the definition or a helpful hint")
    letter = makeLett(word)
    stat = "playing"

    print(
        f"Hey {p2_name} , you will be player 2. Your word is {len(word)} charaters long! (worth {wager} points!)\n Here is your clue pharse : {definition}"
    )

    correct = [None] * len(word)
    while stat == "playing":
        guess = input("guess away : ")

        if guess in word_completed:
            guess = input("Already in your correct answer ! Guess again : ")

        stat, correct, incorrect, chance_left, letter, flash, word_completed = playing(
            guess, letter, chance_left, correct, word_completed
        )
        print(flash)
        print(correct, "Tried Incorrect Letters: ", incorrect)

    if stat == "winner":
        print(flash)
        ppoint = p1_pts - wager
        ppoint2 = p2_pts + wager
        hangdb.user_col.update_one(
            {"userName": p1_name, "email": p1_email}, {"$set": {"playPTS": ppoint}}
        )
        hangdb.user_col.update_one(
            {"userName": p2_name, "email": p2_email}, {"$set": {"playPTS": ppoint2}}
        )

    if stat == "lost":
        print(flash)
        ppoint = p1_pts + wager

        hangdb.user_col.update_one(
            {"userName": p1_name, "email": p1_email}, {"$set": {"playPTS": ppoint}}
        )


def playing(guess: chr, letters: list, chance_left, correct, word_completed):

    flash = "Incorrect Guess"

    for x in range(len(letters)):
        if letters[x] == guess:
            correct[x] = guess
            stat = "playing"
            flash = "Correct Guess"
            word_completed.append(guess)

        if letters[x] != guess:
            stat = "playing"
            if correct[x] == None:
                correct[x] = "_"

            if correct[x] == "_":
                next

    if flash == "Incorrect Guess":
        chance_left -= 1
        incorrect.append(guess)

    if len(word_completed) == len(correct):
        stat = "winner"
        flash = " You Win Congratulations"

    if chance_left <= 0:
        stat = "lost"
        flash = "Sorry you lost"

    return stat, correct, incorrect, chance_left, letters, flash, word_completed


def player_mode(x, p1_name, p1_pts, p1_email, p2_name=None, p2_pts=None, p2_email=None):
    if x == 1:
        pvc(p1_name, p1_pts, p1_email)

    else:
        choice = input(
            "Is Player 2 a \n\t 1: New Player \n\t\t or \n\t 2: Returning Player "
        )
        other_choice = menu_validation(2)
        if other_choice == 1:

            plyer2_name, plyer2_ppts, p2_email = player_2_signin()
            pvp(p1_name, p1_pts, p1_email, plyer2_name, plyer2_ppts, p2_email)
        else:
            plyer2_name, plyer2_ppts, p2_email = player_2_return()
            pvp(p1_name, p1_pts, p1_email, plyer2_name, plyer2_ppts, p2_email)
