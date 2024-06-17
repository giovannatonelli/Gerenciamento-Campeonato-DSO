class Campeonato:
    def __init__(self, nome_campeonato: str):
        self.__equipes = []
        self.__partidas =  []
        self.__nome_campeonato = nome_campeonato
        self.__pontuacao = {}

    @property
    def equipes(self):
        return self.__equipes

    def adc_equipe(self, equipe):
        self.__equipes.append(equipe)

    @property
    def partidas(self):
        return self.__partidas

    def adc_partida(self, partida):
        self.__partidas.append(partida)

    @property
    def nome_campeonato(self):
        return self.__nome_campeonato

    @nome_campeonato.setter
    def nome_campeonato(self, nome_campeonato):
        self._nome_campeonato = nome_campeonato
    
    @property
    def pontuacao(self):
        return self.__pontuacao