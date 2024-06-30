from entidades.arbitro import Arbitro
from entidades.equipe import Equipe

class Partida():
    def __init__(self, equipe_1: Equipe, equipe_2: Equipe,
                arbitro: Arbitro, data_partida: any):
        self.__equipe_1 = equipe_1
        self.__equipe_2 = equipe_2
        self.__arbitro = arbitro
        self.__data_partida = data_partida
        self.__num_gols_eq1 = 0
        self.__num_gols_eq2 =  0
    
    @property
    def equipe_1(self):
        return self.__equipe_1

    @equipe_1.setter
    def equipe_1(self, equipe_1):
        if isinstance(equipe_1, Equipe):
            self.__equipe_1 = equipe_1
    
    @property
    def equipe_2(self):
        return self.__equipe_2

    @equipe_2.setter
    def equipe_2(self, equipe_2):
        if isinstance(equipe_2, Equipe):
            self.__equipe_2 = equipe_2

    @property
    def data_partida(self):
        return self.__data_partida

    @data_partida.setter
    def data_partida(self, data_partida):
        self.__data_partida = data_partida

    @property
    def num_gols_eq1(self):
        return self.__num_gols_eq1

    @num_gols_eq1.setter
    def num_gols_eq1(self, num_gols_eq1):
        self.__num_gols_eq1 = num_gols_eq1

    @property
    def num_gols_eq2(self):
        return self.__num_gols_eq2

    @num_gols_eq2.setter
    def num_gols_eq2(self, num_gols_eq2):
        self.__num_gols_eq2 = num_gols_eq2

    @property
    def arbitro(self):
        return self.__arbitro

    @arbitro.setter
    def arbitro(self, arbitro):
        if isinstance(arbitro, Arbitro):
            self.__arbitro = arbitro