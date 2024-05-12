from pessoa import Pessoa
from arbitro import Arbitro
from aluno import Aluno
from tela_pessoa import TelaPessoa 


class ControladorPessoa():
    def __init__(self):
    self.__alunos = []
    self.__arbitro = []
    self.__tela_pessoa = TelaPessoa()

def inclui_aluno(self):
    dados_aluno = self.__tela_aluno.pega_dados_aluno()
    aluno = Aluno(dados_aluno["nome"], dados_amigo["cpf"], dados_amigo["data_nascimento", dados_amigo["matricula"])