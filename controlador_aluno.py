from aluno import Aluno
from tela_aluno import TelaAluno


class ControladorAluno():
    def __init__(self):
        self.__alunos = []
        self.__tela_aluno = TelaAluno()

    def pega_aluno_por_matricula(self, matricula: str):
        for aluno in self.__alunos:
            if(aluno.matricula == matricula):
                return aluno

    def inclui_aluno(self):
        dados_aluno = self.__tela_aluno.solicita_dados_aluno()
        novo_aluno = Aluno (dados_aluno["nome"], dados_aluno["cpf"], dados_aluno["data_nascimento"], dados_aluno["matricula"])
        if isinstance(novo_aluno, Aluno):
            for aluno in self.__alunos:
                if novo_aluno.matricula == aluno.matricula:
                    return None
            self.__alunos.append(novo_aluno)
            return novo_aluno

    def listar_alunos(self):
        for aluno in self.__alunos:
            self.__tela_aluno.mostra_dados_aluno({"nome": aluno.nome, "cpf": aluno.cpf, "data_nascimento": aluno.data_nascimento, "matricula": aluno.matricula})
        if len(self.__alunos) == 0:
            self.__tela_aluno.mostrar_mensagem("A lista está vazia")

    def altera_aluno(self):
        self.listar_alunos()
        matricula_aluno = self.__tela_aluno.seleciona_aluno()
        aluno = self.pega_aluno_por_matricula(matricula_aluno)

        if(aluno is not None):
            novos_dados_aluno = self.__tela_aluno.solicita_dados_aluno()
            aluno.nome = novos_dados_aluno["nome"]
            aluno.cpf = novos_dados_aluno["cpf"]
            aluno.data_nascimento = novos_dados_aluno["data_nascimento"]
            aluno.matricula =  novos_dados_aluno["matricula"]
            self.__tela_aluno.mostrar_mensagem("Dados Alterados com sucesso")
            self.__tela_aluno.mostra_dados_aluno()

    def exclui_aluno(self):
        self.listar_alunos()
        matricula_aluno = self.__tela_aluno.seleciona_aluno()
        aluno = self.pega_aluno_por_matricula(matricula_aluno)

        if(aluno is not None):
            self.__alunos.remove(aluno)
            self.__tela_aluno.mostrar_mensagem("Aluno removido com sucesso")
            #avaliar possibilidade de colocar uma opcao "deseja listar os alunos?"
            self.listar_alunos()
        else:
            self.__tela_aluno.mostrar_mensagem("Esse aluno não existe")

    def retornar_incio(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.listar_alunos, 2: self.inclui_aluno, 3: self.exclui_aluno, 4: self.altera_aluno, 5: self.retornar_incio}

        executando = True 
        while executando:
            lista_opcoes[self.__tela_aluno.tela_opcoes_aluno()]()