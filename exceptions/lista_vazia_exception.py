class ListaVaziaException(Exception):
    def __init__(self):
        self.mensagem = "Não foi possível listar pois a lista está vazia"
        super().__init__(self.mensagem)