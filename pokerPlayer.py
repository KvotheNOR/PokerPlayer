class Table:

    def __init__(self, big_blind, player_count, button):
        self.big_blind = big_blind
        self.small_bind = int(big_blind / 2)
        self.player_count =  player_count
        self.button = button

class Player:

    def __init__(self, chips, position):
        self.chips = chips
        self.position = position



table = Table(200, 6, 1)

players_list = {"player1": 4000, "player2": 5000, "player3": 5000, "player4": 5000, "player5": 5000, "player6": 6000}
players_list_name = []

#creates player1 player2......
for i in range(table.player_count):
    players_list_name.append("player"+ str(i+1))

print(players_list_name)
