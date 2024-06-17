from curso import Curso
from aluno import Aluno


class Equipe:
    def __init__(self, nome, curso: Curso):
        self.__nome = nome
        self.__curso = curso  
        self.__alunos = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def curso(self):
        return self.__curso
    
    @curso.setter
    def curso(self, curso):
        if isinstance(curso, Curso):
            self.__curso = curso

    @property
    def alunos(self):
        return self.__alunos
    
    def adc_alunos(self, aluno: Aluno):
        self.__alunos.append(aluno)
    
    def remove_alunos(self, nome:str):
        for aluno in self.__alunos:
            if aluno.nome == nome:
                self.__alunos.remove(aluno)