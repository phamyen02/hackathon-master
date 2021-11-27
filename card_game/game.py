from card_game.deck import Deck
from card_game.player import Player

TABLE_STATE_SUFFER = 'suffer'
TABLE_STATE_SHOW_HAND = 'show_hand'
TABLE_STATE_INIT = 'init'


class PlayingTable(object):
    MAX_PLAYER = 4
    MIN_PLAYER = 2

    def __init__(self, players):
        self.players = players
        self.deck = None
        self.state = TABLE_STATE_INIT
        self.winner = None

    def print_players(self):
        for index, player in enumerate(self.players):
            print(f"{index + 1}  {player.name}")

    def total_players(self):
        return len(self.players)

    def can_add_player(self):
        return self.total_players() < self.MAX_PLAYER

    def add_player(self, player):
        if self.total_players() >= self.MAX_PLAYER:
            raise ValueError('Đã tối đa số người chơi')
        self.players.append(player)

    def remove_player(self, index):
        if self.total_players() <= self.MIN_PLAYER:
            raise ValueError('Không thể loại bỏ người chơi')
        del self.players[index - 1]

    def can_remove_player(self):
        return self.total_players() > self.MIN_PLAYER

    def suffer_deck(self):
        deck = Deck()
        deck.build()
        deck.shuffle_card()
        self.deck = deck

        for i in range(len(self.players)):
            for n in range(3):
                self.players[i].add_card(deck.deal_card())
        self.state = TABLE_STATE_SUFFER

    def show_hand(self):
        if self.state != TABLE_STATE_SUFFER:
            raise ValueError('Không thể lật bài khi chưa chia bài')

        winner = None  # type: Player
        for player in self.players:
            if not winner:
                winner = player
                continue
            if player.point > winner.point:
                winner = player
            elif player.point == winner.point:
                if player.biggest_card > winner.biggest_card:
                    winner = player
        self.winner = winner
        self.state = TABLE_STATE_SHOW_HAND

    def show_cards(self):
        self.show_hand()
        for player in self.players:
            print(player.flip_card())

        print("Người chiến thắng: %s" % self.winner.flip_card())


def init_table(players) -> PlayingTable:
    return PlayingTable(players)


def add_new_user() -> Player:
    name_player = input()
    return Player(name_player)
