class User:
    def __init__(self, name, chave):
       self.name = name
       self.chave = chave
       self.cartas = 0

    def show_top_deck(self):
        for i, item in enumerate(self.top_deck):
            item_name = item.get_name()
            item_name = item_name.capitalize()
            print(i,'-', item_name)

    def get_card(self):
        card = self.deck.pop()
        self.top_deck.append(card)
        return card

    def deck_And_handle_empty(self):
        return len(self.deck) == 0 and len(self.top_deck) == 0

