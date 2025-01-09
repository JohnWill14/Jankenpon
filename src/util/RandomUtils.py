import random

from src.model.Attack import Attack
from src.model.Card import Card

def get_random_cards(n):
    cards = []

    for i in range(n):
         random_value = random.randint(0, len(Attack._member_map_.values()) - 1)
         cards.append(Card(Attack(random_value)))
    return cards