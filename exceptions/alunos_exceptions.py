class AlunoJaAdicionadoException(Exception):
    def __init__(self):
        self.mensagem = "Esse aluno já faz parte dessa equipe"
        super().__init__(self.mensagem)

class AlunoNaoExisteException(Exception):
    def __init__(self):
        self.mensagem = "Esse aluno não existe"
        super().__init__(self.mensagem)

class AlunoNaoPertenceCursoException(Exception):
    def __init__(self):
        self.mensagem = "O aluno inserido não pertence ao curso da equipe"
        super().__init__(self.mensagem)

class AlunoNaoPertenceEquipeException(Exception):
    def __init__(self):
        self.mensagem = "O aluno inserido não pertence à equipe"
        super().__init__(self.mensagem)

class AlunoRepetidoException(Exception):
    def __init__(self):
        self.mensagem = "Não foi possível completar a ação pois esse aluno já está cadastrado"
        super().__init__(self.mensagem)