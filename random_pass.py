import random



def rand_pass():
    low_case = "abcdefghijklmnopqrstuvwxy"
    up_case = "ABCDEFGHIJKLMNOPQSTUVWXYZ"

    number = "0123456789"
    symbols = "@#$%&!"
    make_pass = low_case + up_case + number + symbols

    length_pass = 8

    password = "".join(random.sample(make_pass, length_pass))
    return password