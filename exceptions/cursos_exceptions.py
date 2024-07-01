class CursoJaCadastradoException(Exception):
    def __init__(self):
        self.mensagem = "Não foi possível completar a ação pois esse curso já está cadastrado"
        super().__init__(self.mensagem)

class CursoNExisteException(Exception):
    def __init__(self):
        self.mensagem = "Por favor, cadastre o curso antes de adicionar um aluno"
        super().__init__(self.mensagem)

class CursoNCadastradoException(Exception):
     def __init__(self):
        self.mensagem = "Esse curso não existe"
        super().__init__(self.mensagem)