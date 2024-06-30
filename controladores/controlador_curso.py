from telas.tela_curso import TelaCurso
from entidades.curso import Curso
from exceptions.cursos_exceptions import CursoJaCadastradoException
from exceptions.cursos_exceptions import CursoNCadastradoException
from exceptions.lista_vazia_exception import ListaVaziaException


class ControladorCurso:
    def __init__(self, controlador_sistema):
        self.__cursos = []
        self.__tela_curso = TelaCurso()
        self.__controlador_sistema = controlador_sistema

    def inclui_curso(self):
        codigo, nome = self.__tela_curso.solicita_dados_curso()
        try:
            novo_curso = Curso(codigo, nome)
            if isinstance(novo_curso, Curso):
                for c in self.__cursos:
                    if c.codigo_curso == novo_curso.codigo_curso:
                        raise CursoJaCadastradoException()
                self.__cursos.append(novo_curso)
                self.__tela_curso.mostrar_mensagem("Curso adicionado com sucesso!")
                return novo_curso
        except CursoJaCadastradoException as e:
            self.__tela_curso.mostrar_mensagem(e)

    def altera_dados_curso(self):
        codigo = self.__tela_curso.seleciona_curso()
        curso = self.pega_curso_por_codigo(codigo)
        try:
            if curso:
                novo_codigo, novo_nome = self.__tela_curso.solicita_dados_curso()
                curso.codigo_curso = novo_codigo
                curso.nome_curso = novo_nome
                self.__tela_curso.mostrar_mensagem("Dados do curso alterados com sucesso!")
            else:
                raise CursoNCadastradoException
        except CursoNCadastradoException as e:
            self.__tela_curso.mostrar_mensagem(e)

    def exclui_curso(self):
        codigo = self.__tela_curso.seleciona_curso()
        curso = self.pega_curso_por_codigo(codigo)
        try:
            if curso:
                self.__cursos.remove(curso)
                self.__tela_curso.mostrar_mensagem("Curso excluído com sucesso!")
            else:
                raise CursoNCadastradoException
        except CursoNCadastradoException as e:
            self.__tela_curso.mostrar_mensagem(e)

    def valida_curso(self, nome):
        for curso in self.__cursos:
            if curso.nome_curso == nome:
                return curso
        return None

    def pega_curso_por_codigo(self, codigo):
        for curso in self.__cursos:
            if curso.codigo_curso == codigo:
                return curso
        return None

    def listar_cursos(self):
        try:
            if self.__cursos:
                for curso in self.__cursos:
                    self.__tela_curso.mostra_dados_curso(curso)
            else:
                raise ListaVaziaException
        except ListaVaziaException as e:
            self.__tela_curso.mostrar_mensagem(e)

    def abre_tela_curso(self):
        while True:
            opcao = self.__tela_curso.tela_opcoes_curso()
            if opcao == 1:
                self.listar_cursos()
            elif opcao == 2:
                self.inclui_curso()
            elif opcao == 3:
                self.exclui_curso()
            elif opcao == 4:
                self.altera_dados_curso()
            elif opcao == 0:
                return
            else:
                print("Opção inválida!")

    def retornar_incio(self):
        self.__controlador_sistema.abre_tela()