from pessoa import Pessoa


class Arbitro(Pessoa):
    def __init__(self, nome: str, cpf: str, data_nascimento):
        super().__init__(nome, cpf, data_nascimento)
        self.__num_partidas = 0

    @property
    def num_partidas(self):
        return self.__num_partidas

    @num_partidas.setter
    def num_partidas(self, num_partidas):
        self.__num_partidas += num_partidas
