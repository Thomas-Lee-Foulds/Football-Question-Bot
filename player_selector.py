from random import sample

def get_unique_name():
    players = set(line.strip() for line in open('players.txt'))
    return sample(players,1)[0]