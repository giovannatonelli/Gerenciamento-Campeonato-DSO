class Campeonato:
    def __init__(self, equipes=None, partidas=None, nome_campeonato=""):
        self._equipes = equipes if equipes is not None else []
        self._partidas = partidas if partidas is not None else []
        self._nome_campeonato = nome_campeonato

    @property
    def equipes(self):
        return self._equipes

    @equipes.setter
    def equipes(self, equipes):
        self._equipes = equipes

    @property
    def partidas(self):
        return self._partidas

    @partidas.setter
    def partidas(self, partidas):
        self._partidas = partidas

    @property
    def nome_campeonato(self):
        return self._nome_campeonato

    @nome_campeonato.setter
    def nome_campeonato(self, nome_campeonato):
        self._nome_campeonato = nome_campeonato