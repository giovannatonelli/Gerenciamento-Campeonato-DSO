from entidades.aluno import Aluno
from telas.tela_aluno import TelaAluno
from exceptions.alunos_exceptions import AlunoRepetidoException
from exceptions.cursos_exceptions import CursoNExisteException
from exceptions.pessoas_exceptions import PessoaNCadastradaException
from exceptions.lista_vazia_exception import ListaVaziaException


class ControladorAluno():
    def __init__(self, controlador_sistema):
        self.__alunos = []
        self.__tela_aluno = TelaAluno()
        self.__controlador_sistema = controlador_sistema

    def pega_aluno_por_matricula(self, matricula: str):
        for aluno in self.__alunos:
            if(aluno.matricula == matricula):
                return aluno
            else:
                return None
            


    def inclui_aluno(self):
        dados_aluno = self.__tela_aluno.solicita_dados_aluno()
        try:
            curso_obj = self.__controlador_sistema.valida_curso(dados_aluno["curso"])
            if curso_obj is None:
                raise CursoNExisteException
        except CursoNExisteException as e:
                self.__tela_aluno.mostrar_mensagem(e)
                return None
        try:
            novo_aluno = Aluno(dados_aluno["nome"], 
                        dados_aluno["cpf"], 
                        dados_aluno["data_nascimento"], 
                        dados_aluno["matricula"], 
                        dados_aluno["curso"])
            if not self.__controlador_sistema.valida_cpf(dados_aluno['cpf']):
                raise ValueError("CPF inválido. Por favor, digite um cpf válido")
            elif isinstance(novo_aluno, Aluno):
                try:
                    for aluno in self.__alunos:
                        if novo_aluno.matricula == aluno.matricula:
                            raise AlunoRepetidoException()
                    self.__alunos.append(novo_aluno)
                    self.__tela_aluno.mostrar_mensagem("Aluno adicionado com sucesso!")
                    return novo_aluno
                except AlunoRepetidoException as e:
                    self.__tela_aluno.mostrar_mensagem(e)
        except ValueError as e:
            self.__tela_aluno.mostrar_mensagem(e)

    def listar_alunos(self):
        try:
            for aluno in self.__alunos:
                self.__tela_aluno.mostra_dados_aluno({"nome": aluno.nome,
                                                      "cpf": aluno.cpf, 
                                                      "data_nascimento": aluno.data_nascimento, 
                                                      "matricula": aluno.matricula, 
                                                      "curso": aluno.curso})
            if len(self.__alunos) == 0:
                raise ListaVaziaException()
        except ListaVaziaException as e:
            self.__tela_aluno.mostrar_mensagem(e)

    def altera_aluno(self):
        matricula_aluno = self.__tela_aluno.seleciona_aluno()
        aluno = self.pega_aluno_por_matricula(matricula_aluno)

        if(aluno is not None):
            novos_dados_aluno = self.__tela_aluno.solicita_dados_aluno()
            aluno.nome = novos_dados_aluno["nome"]
            aluno.cpf = novos_dados_aluno["cpf"]
            aluno.data_nascimento = novos_dados_aluno["data_nascimento"]
            aluno.matricula =  novos_dados_aluno["matricula"]
            aluno.curso = novos_dados_aluno["curso"]
            self.__tela_aluno.mostrar_mensagem("Dados Alterados com sucesso")
            self.__tela_aluno.mostra_dados_aluno(novos_dados_aluno)

    def exclui_aluno(self):
        matricula_aluno = self.__tela_aluno.seleciona_aluno()
        aluno = self.pega_aluno_por_matricula(matricula_aluno)
        try:
            if(aluno is not None):
                self.__alunos.remove(aluno)
                self.__tela_aluno.mostrar_mensagem("Aluno removido com sucesso")
                self.listar_alunos()
            else:
                raise PessoaNCadastradaException()
        except PessoaNCadastradaException as e:
            self.__tela_aluno.mostrar_mensagem(e)

    def retornar_incio(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela_aluno(self):
        lista_opcoes = {1: self.listar_alunos,
                        2: self.inclui_aluno, 
                        3: self.exclui_aluno, 
                        4: self.altera_aluno, 
                        0: self.retornar_incio}

        executando = True 
        while executando:
            lista_opcoes[self.__tela_aluno.tela_opcoes_aluno()]()