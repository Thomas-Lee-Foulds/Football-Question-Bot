import random

def get_names():
    while True:  
        chosen = random.randint(1,5)
        if chosen == 1:
            players = set(line.strip() for line in open('Attackers.txt'))
            players_chosen = random.sample(players,2)
            break
        elif chosen == 2:
            players = set(line.strip() for line in open('Midfielders.txt'))
            players_chosen = random.sample(players,2)
            break
        elif chosen == 3:
            players = set(line.strip() for line in open('Defenders.txt'))
            players_chosen = random.sample(players,2)
            break
        elif chosen == 4:
            players = set(line.strip() for line in open('Goalkeepers.txt'))
            players_chosen = random.sample(players,2)
            break
                
    return players_chosen