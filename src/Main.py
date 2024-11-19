from src.Client import Client, show_menu
from src.util.soUtil import clear
from src.util.RandomUtils import get_next_atak, get_random_cards


def get_cards():
    return get_random_cards(25)

if __name__ == "__main__":
    clientes = []
    clientes.append(Client("cliente 1", 5, 5))
    clientes.append(Client("cliente 2", 5, 5))

    pts = [0,0]

    user_actual = 0
    user_actual_oponnent = 1

    while(True):
        if clientes[user_actual].deck_And_handle_empty() or clientes[user_actual_oponnent].deck_And_handle_empty():
            break

        card_Selected = show_menu(clientes[user_actual])

        if card_Selected == None:
            pts[user_actual_oponnent] = pts[user_actual_oponnent] + 1
            break


        card_Selected_oponente = show_menu(clientes[user_actual_oponnent])

        if card_Selected_oponente == None:
            pts[user_actual] = pts[user_actual] + 1
            break

        result = card_Selected.attack_outher_card(card_Selected_oponente)

        if result.is_draw():
            print("EMPATE")
            print("digite qualquer valor para sair")
            _ = input()
            clear()
            continue

        print(result.attack.name.capitalize(), result.tuple[0],result.tuple[1].name.capitalize())

        if result.is_victory():
            print(f"user {clientes[user_actual].name} ganhou.")
            pts[user_actual] = pts[user_actual] + 1
        else:
            print(f"user {clientes[user_actual_oponnent].name} ganhou.")
            pts[user_actual_oponnent] = pts[user_actual_oponnent] + 1

        if user_actual == 1:
            user_actual = 0
            user_actual_oponnent = 1
        else:
            user_actual = 1
            user_actual_oponnent = 0


    print(f"ponto user 1 {pts[0]} e 2 {pts[1]}")