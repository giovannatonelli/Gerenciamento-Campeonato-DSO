class Equipe:
    def __init__(self, nome, curso=None, alunos=None, num_pontos=0):
        self.nome = nome
        self.curso = curso  
        self.alunos = alunos if alunos else []
        self.num_pontos = num_pontos

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_alunos(self):
        return self.alunos

    def set_alunos(self, alunos):
        self.alunos = alunos

    def get_num_pontos(self):
        return self.num_pontos

    def set_num_pontos(self, num_pontos):
        self.num_pontos = num_pontos