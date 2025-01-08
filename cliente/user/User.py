class User:
    def __init__(self, name, chave):
       self.name = name
       self.chave = chave

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

def show_menu(user):
    pegou_card = False
    desistiu = False
    while(True):
        print(f"USER {user.name}")
        print("1- ver mao")
        print("2- pegar carta do deck")
        print("3- desistir")
        item = int(input("> "))

        if item == 1:
            user.show_top_deck()
            print(len(user.top_deck), '- sair')

            op = int(input("> "))

            if op == len(user.top_deck):
                continue

            card = user.top_deck[op]
            del user.top_deck[op]
            return card
        elif item == 2:
            if pegou_card == False and len(user.deck) > 0:
                card = user.get_card()
                print(f"pegou o card {card.get_name()}")
                pegou_card = True
            else:
                print("nao pode pegar mais =(")
        elif item == 3:
            print("desistiu")
            break
    return None