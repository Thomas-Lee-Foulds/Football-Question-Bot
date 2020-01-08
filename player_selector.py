from random import sample

def get_unique_name(first_name):
    while True:
        players = set(line.strip() for line in open('players.txt'))
        rand_name = sample(players,1)[0]
        if (first_name != rand_name):
            break
    return rand_name