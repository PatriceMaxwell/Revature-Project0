from players import returning_player_sign_in, new_player_sign_up, sign


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
