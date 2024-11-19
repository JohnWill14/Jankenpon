from src.util.RandomUtils import get_random_cards


def get_cards(n):
    return get_random_cards(n)

class Client:
    def __init__(self, name, n, handle):
       self.name = name
       self.deck = get_cards(n)
       self.top_deck = self.deck[:handle]
       self.deck = self.deck[handle:]

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

def show_menu(cliente):
    pegou_card = False
    desistiu = False
    while(True):
        print(f"USER {cliente.name}")
        print("1- ver mao")
        print("2- pegar carta do deck")
        print("3- desistir")
        item = int(input("> "))

        if item == 1:
            cliente.show_top_deck()
            print(len(cliente.top_deck), '- sair')

            op = int(input("> "))

            if op == len(cliente.top_deck):
                continue

            card = cliente.top_deck[op]
            del cliente.top_deck[op]
            return card
        elif item == 2:
            if pegou_card == False and len(cliente.deck) > 0:
                card = cliente.get_card()
                print(f"pegou o card {card.get_name()}")
                pegou_card = True
            else:
                print("nao pode pegar mais =(")
        elif item == 3:
            print("desistiu")
            break
    return None