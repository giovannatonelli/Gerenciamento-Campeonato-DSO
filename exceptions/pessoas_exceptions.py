class PessoaNCadastradaException(Exception):
    def __init__(self):
        self.mensagem = "Não foi possível completar a ação pois essa pessoa não está cadastrada"
        super().__init__(self.mensagem)

class CpfInvalidoException(Exception):
    def __init__(self):
        self.mensagem = "CPF inválido. Por favor, insira um CPF válido"
        super().__init__(self.mensagem)