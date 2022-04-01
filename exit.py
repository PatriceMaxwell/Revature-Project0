from distutils.log import error
from Hangman import start

f = open("hangman_exit.txt", "r+")
file_name = f.read()
print(file_name)


f.close()

session = error
while session == error:
    try:
        session = int(input())
        if session != 0:
            print("please enter a number on the Menu :")
            session = error
        elif session == 0:
            start()
    except:
        print("please enter vaild number :")
        session = error
