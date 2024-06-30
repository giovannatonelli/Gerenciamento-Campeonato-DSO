class ArbitroRepetidoException(Exception):
    def __init__(self):
        self.mensagem = "Não foi possível completar a ação pois esse árbitro já está cadastrado"
        super().__init__(self.mensagem)