import random

TIME_LIMIT = 17

this_side = [2, 1, 5, 10]
that_side = []

def send_2_across():
    pass

def add_highest_time():
    pass

def send_1_back():
    pass

def add_time():
    pass

def all_across():
    return False

def over_time_limit():
    return False

while not all_across() and not over_time_limit():

    send_2_across()
    add_highest_time()
    send_1_back()
    add_time()
    send_2_across()
    add_highest_time()
    send_1_back()
    add_time()
    send_2_across()
    add_highest_time()

    print("Test") # debug
