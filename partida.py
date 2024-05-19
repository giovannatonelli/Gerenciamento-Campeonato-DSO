from arbitro import Arbitro

class Partida():
    def __init__(self, id_partida: int, equipe_1: str, equipe_2: str,
                arbitro: Arbitro, data_partida: any, num_gols_eq1: int, 
                num_gols_eq2: int):
        self._id_partida = id_partida
        self._equipe_1 = equipe_1
        self._equipe_2 = equipe_2
        self._arbitro = arbitro
        self._data_partida = data_partida
        self._num_gols_eq1 = num_gols_eq1
        self._num_gols_eq2 = num_gols_eq2

    @property
    def id_partida(self):
        return self._id_partida

    @id_partida.setter
    def id_partida(self, id_partida):
        self._id_partida = id_partida
    
    @property
    def equipe_1(self):
        return self._equipe_1

    @equipe_1.setter
    def equipe_1(self, equipe_1):
        self._equipe_1 = equipe_1
    
    @property
    def equipe_2(self):
        return self._equipe_2

    @equipe_2.setter
    def equipe_2(self, equipe_2):
        self._equipe_2 = equipe_2

    @property
    def data_partida(self):
        return self._data_partida

    @data_partida.setter
    def data_partida(self, data_partida):
        self._data_partida = data_partida

    @property
    def num_gols_eq1(self):
        return self._num_gols_eq1

    @num_gols_eq1.setter
    def num_gols_eq1(self, num_gols_eq1):
        self._num_gols_eq1 = num_gols_eq1

    @property
    def num_gols_eq2(self):
        return self._num_gols_eq2

    @num_gols_eq2.setter
    def num_gols_eq2(self, num_gols_eq2):
        self._num_gols_eq2 = num_gols_eq2

    @property
    def arbitro(self):
        return self.__arbitro

    @arbitro.setter
    def arbitro(self, arbitro):
        if isinstance(arbitro, Arbitro):
            self.__arbitro = arbitro