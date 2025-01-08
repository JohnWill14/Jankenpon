from src.model.Attack import Attack

class Magic:
    def __init__(self, name, blocked_attacks):
        """
        Inicializa uma carta mágica.

        :param name: Nome da carta mágica.
        :param blocked_attacks: Lista de ataques bloqueados.
        """
        self.name = name
        self.blocked_attacks = blocked_attacks

    def get_name(self):
        """
        Retorna o nome da carta mágica formatado.
        """
        return self.name.capitalize()

    def blocks(self, attack):
        """
        Verifica se esta carta bloqueia o ataque especificado.
        
        :param attack: Instância do ataque a ser verificado.
        :return: True se bloqueia, False caso contrário.
        """
        return attack in self.blocked_attacks
