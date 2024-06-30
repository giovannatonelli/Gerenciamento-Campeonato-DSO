class ArbitroRepetidoException(Exception):
    def __init__(self):
        self.mensagem = "Não foi possível completar a ação pois esse árbitro já está cadastrado"
        super().__init__(self.mensagem)

class ArbitroNCadastradoException(Exception):
    def __init__(self):
        self.mensagem = "Cadastre árbitros antes de continuar"
        super().__init__(self.mensagem)