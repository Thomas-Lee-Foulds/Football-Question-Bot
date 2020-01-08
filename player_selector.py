from random import choice

def get_unique_name(*args):
    first_name = 'n/a'
    for ar in args:
        first_name = ar
    while True:
        players = set(line.strip() for line in open('players.txt'))
        rand_name = choice(players)
        if (first_name != rand_name):
            break
    return rand_name