import collections

# 사용자 정의 메서드 없이 일련의 속성을 갖는 클래스를 만들 때는 collections.namedtuple을 사용하면 간단하게 구현할 수 있다.
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    """
    A class to represent a deck of cards.
    """
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    # 해당 특별 메서드 선언으로 인해, 클래스에서 len()을 사용해 객체의 길이를 반환
    def __len__(self):
        return len(self._cards)

    # 해당 특별 메서드 선언으로 인해, 클래스에서 객체 슬라이싱 & 인덱싱 지원
    def __getitem__(self, position):
        return self._cards[position]


from random import choice

# print(choice(FrenchDeck()))

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(FrenchDeck(), key=spades_high):
    print(card)