# 实现一副牌 展示特殊方法__getitem__和__len__的功能

import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])
class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.ranks
                                        for rank in self.suits]
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards(position)
    

deck = FrenchDeck()
choice(deck)
    