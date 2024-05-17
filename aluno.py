from pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self, nome: str, cpf: str, data_nascimento, matricula: str):
        super().__init__(nome, cpf, data_nascimento)
        self.__matricula = matricula

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula
