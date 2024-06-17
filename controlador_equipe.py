from tela_equipe import TelaEquipe
from equipe import Equipe
from aluno import Aluno
from curso import Curso


class ControladorEquipe:
    def __init__(self, controlador_sistema):
        self.__equipes = []
        self.__tela_equipe = TelaEquipe()
        self.__controlador_sistema = controlador_sistema

    def inclui_equipe(self):
        curso = self.__controlador_sistema.valida_curso(self.__tela_equipe.solicita_curso())
        if isinstance(curso, Curso):
            nome = self.__tela_equipe.solicita_equipe()
            equipe = Equipe(nome, curso)
            self.__equipes.append(equipe)
            self.__tela_equipe.mostrar_mensagem("Equipe adicionada com sucesso!")
        else:
            self.__tela_equipe.mostrar_mensagem("Curso não existe")
            self.abre_tela_equipe()


    def inclui_pontos(self):
        nome_equipe = self.__tela_equipe.solicita_equipe()
        equipe = self.pega_equipe_por_nome(nome_equipe)
        if equipe:
            pontos = int(input("Digite o número de pontos a adicionar: "))
            equipe.set_num_pontos(equipe.get_num_pontos() + pontos)
            self.__tela_equipe.mostrar_pontos_equipe(equipe)
        else:
            self.__tela_equipe.mostrar_mensagem("Equipe não encontrada!")

    def altera_dados_equipe(self):
        nome_equipe = self.__tela_equipe.solicita_equipe()
        equipe = self.pega_equipe_por_nome(nome_equipe)
        if equipe:
            novo_nome = input("Digite o novo nome da equipe: ")
            equipe.set_nome(novo_nome)
            self.__tela_equipe.mostrar_mensagem("Dados da equipe alterados com sucesso!")
        else:
            self.__tela_equipe.mostrar_mensagem("Equipe não encontrada!")

    def exclui_equipe(self):
        nome_equipe = self.__tela_equipe.solicita_equipe()
        equipe = self.pega_equipe_por_nome(nome_equipe)
        if equipe:
            self.__equipes.remove(equipe)
            self.__tela_equipe.mostrar_mensagem("Equipe removida com sucesso!")
        else:
            self.__tela_equipe.mostrar_mensagem("Equipe não encontrada!")

    def pega_equipe_por_nome(self, nome):
        for equipe in self.__equipes:
            if equipe.nome == nome:
                return equipe
        return None

    def listar_equipes(self):
        if self.__equipes:
            for equipe in self.__equipes:
                self.__tela_equipe.mostra_dados_equipe(equipe)
        else:
            self.__tela_equipe.mostrar_mensagem("Nenhuma equipe cadastrada!")

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

    def equipe_mais_gols(self):
        # lógica para encontrar a equipe com mais gols
        equipe_mais_gols = None
        return equipe_mais_gols

    def equipe_levou_mais_gols(self):
        #  para encontrar a equipe que levou mais gols
        pass

    def equipe_menos_gols(self):
        #para encontrar a equipe com menos gols
        pass 
    
    def adicionar_aluno_equipe(self):
        nome_equipe = self.__tela_equipe.solicita_equipe()
        equipe = self.pega_equipe_por_nome(nome_equipe)
        if equipe:
            matricula_aluno = self.__tela_equipe.solicita_matricula_aluno()
            aluno = self.__controlador_sistema.pega_aluno_por_matricula(matricula_aluno)
            if aluno.curso == equipe.curso.nome_curso:
                equipe.alunos.append(aluno)
                self.__tela_equipe.mostrar_mensagem("Aluno adicionado à equipe!")
            else:
                self.__tela_equipe.mostrar_mensagem("O aluno inserido não é do curso dessa equipe")
        else:
            self.__tela_equipe.mostrar_mensagem("Equipe não encontrada!")

    def remover_aluno_equipe(self):
        nome_equipe = self.__tela_equipe.solicita_equipe()
        equipe = self.pega_equipe_por_nome(nome_equipe)
        if equipe:
            nome_aluno = input("Digite o nome do aluno a ser removido: ")
            for i, aluno in enumerate(equipe.alunos):
                if aluno.nome == nome_aluno:
                    del equipe.alunos[i]
                    self.__tela_equipe.mostrar_mensagem("Aluno removido da equipe!")
                    return
            self.__tela_equipe.mostrar_mensagem("Aluno não encontrado na equipe!")
        else:
            self.__tela_equipe.mostrar_mensagem("Equipe não encontrada!")

    def retornar_incio(self):
        self.__controlador_sistema.abre_tela_equipe()