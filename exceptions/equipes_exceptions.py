class EquipeNaoExisteException(Exception):
     def __init__(self):
        self.mensagem = "Essa equipe não existe"
        super().__init__(self.mensagem)

class EquipeRepetidaException(Exception):
    def __init__(self):
        self.mensagem = "Não foi possível completar a ação pois essa equipe já está cadastrada"
        super().__init__(self.mensagem)