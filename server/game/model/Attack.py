import enum


class Attack(enum.Enum):
    PEDRA: int = 0
    PAPEL: int = 1
    TESOURA: int = 2
    LAGARTO: int = 3
    SPOCK: int = 4

    def __str__(self):
        if self.value == 0:
            return "PEDRA"
        elif self.value == 1:
            return "PAPEL"
        elif self.value == 2:
            return "TESOURA"
        elif self.value == 3:
            return "LAGARTO"
        elif self.value == 4:
            return "SPOCK"

relationship = {
    Attack.PEDRA.value: [("quebra", Attack.TESOURA), ("esmaga", Attack.LAGARTO)],
    Attack.PAPEL.value: [("cobre", Attack.PEDRA), ("refuta", Attack.SPOCK)],
    Attack.TESOURA.value: [("corta", Attack.PAPEL), ("decapita", Attack.LAGARTO)],
    Attack.LAGARTO.value: [("come", Attack.PAPEL), ("envenena", Attack.SPOCK)],
    Attack.SPOCK.value: [("vaporiza", Attack.PEDRA), ("quebra", Attack.TESOURA)]
}


