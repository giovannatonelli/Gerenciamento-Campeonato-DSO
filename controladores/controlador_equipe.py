from telas.tela_equipe import TelaEquipe
from entidades.equipe import Equipe
from exceptions.cursos_exceptions import CursoNCadastradoException
from exceptions.equipes_exceptions import EquipeRepetidaException
from exceptions.equipes_exceptions import EquipeNaoExisteException
from exceptions.lista_vazia_exception import ListaVaziaException
from exceptions.alunos_exceptions import AlunoNaoPertenceCursoException
from exceptions.alunos_exceptions import AlunoJaAdicionadoException
from exceptions.alunos_exceptions import AlunoNaoPertenceEquipeException
from exceptions.alunos_exceptions import AlunoNaoExisteException
from DAOS.equipe_dao import EquipeDAO
class ControladorEquipe:
    def __init__(self, controlador_sistema):
        self.__equipe_DAO = EquipeDAO()
        #self.__equipes = []
        self.__tela_equipe = TelaEquipe()
        self.__controlador_sistema = controlador_sistema

    def inclui_equipe(self):
        dados_equipe = self.__tela_equipe.solicita_dados_equipe()
        try: 
            curso_obj = self.__controlador_sistema.valida_curso(dados_equipe["curso"])
            if curso_obj is None:
                raise CursoNCadastradoException
        except CursoNCadastradoException as e:
            self.__tela_equipe.mostrar_mensagem(e)
            self.abre_tela_equipe()
        try:
            nova_equipe = Equipe(dados_equipe["nome"],
                            dados_equipe["curso"])
            if isinstance(nova_equipe, Equipe):
                for equipe in self.__equipe_DAO.get_all():
                    if nova_equipe.nome == equipe.nome:
                        raise EquipeRepetidaException()
                self.__equipe_DAO.add(nova_equipe)
                self.__tela_equipe.mostrar_mensagem("Equipe adicionada com sucesso!")
                return nova_equipe
        except EquipeRepetidaException as e:
            self.__tela_equipe.mostrar_mensagem(e)

    def altera_dados_equipe(self):
        nome = self.__tela_equipe.solicita_equipe()
        equipe = self.pega_equipe_por_nome(nome)
        try:
            if equipe:
                novos_dados_equipe = self.__tela_equipe.solicita_dados_equipe()
                equipe.nome = novos_dados_equipe["nome"]
                equipe.curso = novos_dados_equipe["curso"]
                self.__tela_equipe.mostrar_mensagem("Dados da equipe alterados com sucesso!")
            else:
                raise EquipeNaoExisteException
        except EquipeNaoExisteException as e:
                self.__tela_equipe.mostrar_mensagem(e)

    def exclui_equipe(self):
        nome = self.__tela_equipe.solicita_equipe()
        equipe = self.pega_equipe_por_nome(nome)
        try:
            if equipe:
                self.__equipe_DAO.remove(equipe.nome)
                self.__tela_equipe.mostrar_mensagem("Equipe removida com sucesso!")
            else:
                raise EquipeNaoExisteException
        except EquipeNaoExisteException as e:
            self.__tela_equipe.mostrar_mensagem(e)

    def pega_equipe_por_nome(self, nome):
        for equipe in self.__equipe_DAO.get_all():
            if equipe.nome == nome:
                return equipe
        return None

    def listar_equipes(self):
        try:
            if not self.__equipe_DAO:
                raise ListaVaziaException()
            
            todos_dados_equipes = ""
            for equipe in self.__equipe_DAO.get_all():
                dados_equipe = f"Nome: {equipe.nome}\n\nAlunos:\n" + \
                            '\n'.join([f"  - {aluno.nome}" for aluno in equipe.alunos]) + "\n\n"
                todos_dados_equipes += dados_equipe
            
            self.__tela_equipe.mostra_dados_equipes(todos_dados_equipes)
        
        except ListaVaziaException as e:
            self.__tela_equipe.mostrar_mensagem(e)
    
    def adicionar_aluno_equipe(self):
        nome = self.__tela_equipe.solicita_equipe()
        equipe = self.pega_equipe_por_nome(nome)
        try:
            if equipe:
                matricula_aluno = self.__tela_equipe.solicita_matricula_aluno()
                aluno = self.__controlador_sistema.pega_aluno_por_matricula(matricula_aluno)
                try:
                    for al in equipe.alunos:
                        if aluno.matricula == al.matricula:
                            raise AlunoJaAdicionadoException
                    try:
                        if aluno.curso == equipe.curso:
                            equipe.alunos.append(aluno)
                            self.__tela_equipe.mostrar_mensagem("Aluno adicionado à equipe!")
                        else:
                            raise AlunoNaoPertenceCursoException
                    except AlunoNaoPertenceCursoException as e:
                        self.__tela_equipe.mostrar_mensagem(e)
                except AlunoJaAdicionadoException as e:
                    self.__tela_equipe.mostrar_mensagem(e)
            else:
                raise EquipeNaoExisteException
        except EquipeNaoExisteException as e:
                self.__tela_equipe.mostrar_mensagem(e)

    def remover_aluno_equipe(self):
        nome = self.__tela_equipe.solicita_equipe()
        equipe = self.pega_equipe_por_nome(nome)
        try: 
            if equipe:
                matricula_aluno = self.__tela_equipe.solicita_matricula_aluno()
                try:
                    aluno = self.__controlador_sistema.pega_aluno_por_matricula(matricula_aluno)
                    if aluno is None:
                        raise AlunoNaoExisteException
                except AlunoNaoExisteException as e:
                    self.__tela_equipe.mostrar_mensagem(e)
                    self.__tela_equipe.tela_opcoes_equipe()
                try:
                    for al in equipe.alunos:
                        if aluno.matricula == al.matricula:
                            equipe.alunos.remove(aluno)
                            self.__tela_equipe.mostrar_mensagem("Aluno removido da equipe!")
                        else:
                            raise AlunoNaoPertenceEquipeException
                except AlunoNaoPertenceEquipeException as e:
                    self.__tela_equipe.mostrar_mensagem(e)
            else:
                raise EquipeNaoExisteException
        except EquipeNaoExisteException as e:
            self.__tela_equipe.mostrar_mensagem(e)
            

    def abre_tela_equipe(self):
        while True:
            opcao = self.__tela_equipe.tela_opcoes_equipe()
            if opcao == 1:
                self.listar_equipes()
            elif opcao == 2:
                self.inclui_equipe()
            elif opcao == 3:
                self.exclui_equipe()
            elif opcao == 4:
                self.altera_dados_equipe()
            elif opcao == 5:
                self.adicionar_aluno_equipe()
            elif opcao == 6:
                self.remover_aluno_equipe()
            elif opcao == 0:
                return
            else:
                print("Opção inválida!")

    def retornar_incio(self):
        self.__controlador_sistema.abre_tela_equipe()