from pessoa import Pessoa
from curso import Curso



class Aluno(Pessoa):
    def __init__(self, nome: str, cpf: str, data_nascimento, matricula: str, curso: Curso):
        super().__init__(nome, cpf, data_nascimento)
        self.__matricula = matricula
        self.__curso = curso

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def curso(self):
        return self.__curso

    @curso.setter
    def curso(self, curso):
        if isinstance (curso, Curso):
            self.__curso = curso