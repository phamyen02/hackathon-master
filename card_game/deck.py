
import random
from card_game.card import Card
ENUM_SUIT = {
    1: '♠',
    2: '♣',
    3: '♦',
    4: '♥'
}
ENUM_STATE_INIT = 'INIT'
ENUM_STATE = {
    ENUM_STATE_INIT: 'init'
}
class Deck:
    cards = []

    def __init__(self):
        self.state = ENUM_STATE_INIT

    def build(self):
        self.cards = []
        for s in ENUM_SUIT.keys():
            for r in range(1, 10):  # 1 - 9
                self.cards.append(Card(s, r))
        assert len(self.cards) == 36

    def shuffle_card(self):
        random.shuffle(self.cards)

    def deal_card(self) -> Card:
        if len(self.cards) == 0:
            raise ValueError('Đã hết card trong bài')
        return self.cards.pop()

