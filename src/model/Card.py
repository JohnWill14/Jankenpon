from src.model.Attack import Attack, relationship

class Result:
    def __init__(self, attack, tuple, victory):
        self.attack = attack
        self.tuple = tuple
        self.victory = victory

    def is_draw(self):
        return self.attack == None and self.tuple == None

    def is_victory(self):
        return self.victory

class Card:
    def __init__(self, type):
        if isinstance(type, Attack):
            self.attack = type
            self.magic = False

    def get_name(self):
        return self.attack.name.capitalize()

    def get_attack(self):
        return self.attack

    def attack_outher_card(self, card_attak_opponent):
        attak_opponent = card_attak_opponent.get_attack()
        if(self.attack == attak_opponent):
            return  Result(None, None, True)

        opponent = False
        tuple_selected = None
        for tuple in relationship[self.attack.value]:
            if tuple[1] == attak_opponent:
                tuple_selected = tuple
                opponent = True

        if opponent:
            return Result(self.attack, tuple_selected, True)
        else:
            for tuple in relationship[attak_opponent.value]:
                if tuple[1] == self.attack:
                    tuple_selected = tuple
                    return Result(attak_opponent, tuple_selected, False)

    def __str__(self):
        return str(self.attack)