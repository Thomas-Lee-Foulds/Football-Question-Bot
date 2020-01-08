from random import sample

def get_unique_name():
    players = set(line.strip() for line in open('players.txt'))
    rand_name = sample(players,1)
    return rand_name