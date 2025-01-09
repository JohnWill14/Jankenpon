from game.util.RandomUtils import get_random_cards


def get_cards(n):
    return get_random_cards(n)

handle = 5
class Cliente:
    def __init__(self, nome, chave, n = 20):
        self.nome = nome
        self.chave = chave
        self.deck = get_cards(n)
        self.top_deck = self.deck[:handle]
        self.deck = self.deck[handle:]

    def get_card(self):
        card = self.deck.pop()
        self.top_deck.append(card)
        return card

    def is_deck_And_handle_empty(self):
        return len(self.deck) == 0 and len(self.top_deck) == 0