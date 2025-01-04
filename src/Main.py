from src.Client import Client, show_menu
from src.util.soUtil import clear
from src.util.RandomUtils import get_random_cards
from src.model.Magic import Magic
from src.model.Attack import Attack
import random


def get_cards():
    return get_random_cards(25)

# Função para criar cartas mágicas aleatórias
def generate_random_magic_cards(num_cards):
    all_attacks = list(Attack)  # Lista de todos os ataques
    magic_cards = []
    for _ in range(num_cards):
        attack_to_block = random.choice(all_attacks)  # Seleciona um ataque aleatório
        card_name = f"Anti-{attack_to_block.name.capitalize()}"  # Nome dinâmico
        magic_cards.append(Magic(card_name, [attack_to_block]))
    return magic_cards

# Criando cartas mágicas aleatórias para cada jogador
magic_cards = [
    generate_random_magic_cards(4),  # Jogador 1 (2 cartas mágicas)
    generate_random_magic_cards(4)   # Jogador 2 (2 cartas mágicas)
]


if __name__ == "__main__":
    clientes = []
    clientes.append(Client("cliente 1", 5, 5))
    clientes.append(Client("cliente 2", 5, 5))

    pts = [0, 0]

    user_actual = 0
    user_actual_oponnent = 1

    while(True):
        if clientes[user_actual].deck_And_handle_empty() or clientes[user_actual_oponnent].deck_And_handle_empty():
            break

        # Mostra o menu para o jogador atual
        print(f"Vez do jogador {clientes[user_actual].name}")
        print("Cartas mágicas disponíveis:")
        # Testando as cartas mágicas
        for i, player_cards in enumerate(magic_cards):
            print(f"\nJogador {i+1} - Cartas Mágicas:")
            for card in player_cards:
                print(f"{card.get_name()} bloqueia {', '.join([atk.name for atk in card.blocked_attacks])}")
        magia_op = int(input("> "))

        magia_selecionada = None
        if magia_op < len(magic_cards[user_actual]):
            magia_selecionada = magic_cards[user_actual].pop(magia_op)  # Remove a magia usada

        # Seleção do ataque
        card_Selected = show_menu(clientes[user_actual])
        if card_Selected is None:
            pts[user_actual_oponnent] += 1
            break

        card_Selected_oponente = show_menu(clientes[user_actual_oponnent])
        if card_Selected_oponente is None:
            pts[user_actual] += 1
            break

        # Verifica se a magia bloqueia o ataque do oponente
        if magia_selecionada and magia_selecionada.blocks(card_Selected_oponente.get_attack()):
            print(f"A magia {magia_selecionada.get_name()} bloqueou o ataque {card_Selected_oponente.get_name()}!")
            pts[user_actual] += 1  # Ganha ponto automático
        else:
            # Calcula o resultado normal
            result = card_Selected.attack_outher_card(card_Selected_oponente)
            if result.is_draw():
                print("EMPATE")
            elif result.is_victory():
                print(f"user {clientes[user_actual].name} ganhou.")
                pts[user_actual] += 1
            else:
                print(f"user {clientes[user_actual_oponnent].name} ganhou.")
                pts[user_actual_oponnent] += 1

        # Alterna os jogadores
        user_actual, user_actual_oponnent = user_actual_oponnent, user_actual

    # Resultado final
    print(f"Pontos finais - {clientes[0].name}: {pts[0]}, {clientes[1].name}: {pts[1]}")
