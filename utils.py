from distutils.log import error


def menu_validation(x: int):

    user_input_keyword = error
    while user_input_keyword == error:
        try:
            user_input_keyword = int(input())
            if user_input_keyword > x or user_input_keyword < 0:
                print("please enter a number on the Menu: ")
                user_input_keyword = error
        except:
            print("please enter a valid number: ")
            user_input_keyword = error

    return user_input_keyword
