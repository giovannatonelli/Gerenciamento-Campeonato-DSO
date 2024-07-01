class CampeonatoNaoExisteException(Exception):
    def __init__(self):
        self.mensagem = "Campeonato não existe. Por favor, adicione um antes de continuar"
        super().__init__(self.mensagem)

class EquipesInsuficientesException(Exception):
    def __init__(self):
        self.mensagem = "Equipes insuficientes"
        super().__init__(self.mensagem)

class CadastreEquipeException(Exception):
    def __init__(self):
        self.mensagem = "Cadastre equipes antes de continuar"
        super().__init__(self.mensagem)