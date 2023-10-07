from src.deck.deck import Deck


class Game:
    def __init__(self):
        self.players = []
        self.deck = Deck()

    def add_player(self, player):
        self.players.append(player)

    def start(self):
        # Game logic goes here
        pass

    def check_win_condition(self):
        # Check for win/loss conditions
        pass

    def handle_player_action(self, player, action):
        # Handle specific player actions
        pass
