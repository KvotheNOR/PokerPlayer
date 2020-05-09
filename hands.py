cards = ['1C', '1S', '1D', '1H', '1C', '1S', '1D', '1H', '1C', '1S', '1D', '1H', '1C', '1S', '1D', '1H', '2C', '2S', '2D', '2H', '2C', '2S', '2D', '2H', '2C', '2S', '2D', '2H', '2C', '2S', '2D', '2H', '3C', '3S', '3D', '3H', '3C', '3S', '3D', '3H', '3C', '3S', '3D', '3H', '3C', '3S', '3D', '3H', '4C', '4S', '4D', '4H', '4C', '4S', '4D', '4H', '4C', '4S', '4D', '4H', '4C', '4S', '4D', '4H', '5C', '5S', '5D', '5H', '5C', '5S', '5D', '5H', '5C', '5S', '5D', '5H', '5C', '5S', '5D', '5H', '6C', '6S', '6D', '6H', '6C', '6S', '6D', '6H', '6C', '6S', '6D', '6H', '6C', '6S', '6D', '6H', '7C', '7S', '7D', '7H', '7C', '7S', '7D', '7H', '7C', '7S', '7D', '7H', '7C', '7S', '7D', '7H', '8C', '8S', '8D', '8H', '8C', '8S', '8D', '8H', '8C', '8S', '8D', '8H', '8C', '8S', '8D', '8H', '9C', '9S', '9D', '9H', '9C', '9S', '9D', '9H', '9C', '9S', '9D', '9H', '9C', '9S', '9D', '9H', '10C', '10S', '10D', '10H', '10C', '10S', '10D', '10H', '10C', '10S', '10D', '10H', '10C', '10S', '10D', '10H', '11C', '11S', '11D', '11H', '11C', '11S', '11D', '11H', '11C', '11S', '11D', '11H', '11C', '11S', '11D', '11H', '12C', '12S', '12D', '12H', '12C', '12S', '12D', '12H', '12C', '12S', '12D', '12H', '12C', '12S', '12D', '12H', '13C', '13S', '13D', '13H', '13C', '13S', '13D', '13H', '13C', '13S', '13D', '13H', '13C', '13S', '13D', '13H']

hand_value = {
    "high_card":1,
    "pair":2,
    "two_pairs":3,
    "threes":4,
    "straight":5,
    "flush":6,
    "full_house":7,
    "foures":8,
    "straight_flush":9
}


class Table_info:

    def __init__(self, big_blind, player_count, button):
        self.big_blind = big_blind
        self.small_bind = int(big_blind / 2)
        self.player_count =  player_count
        self.button = button


"""class Hand_value(your_cards, board, position, players):
    pass"""





table = Table_info(200, 6, 1)

print(table.big_blind)
