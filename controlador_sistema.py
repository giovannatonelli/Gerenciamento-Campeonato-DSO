from tela_sistema import TelaSistema
from controlador_aluno import ControladorAluno
from controlador_arbitro import ControladorArbitro
from controlador_partida import ControladorPartida
from controlador_campeonato import ControladorCampeonato
from controlador_curso import ControladorCurso
from controlador_equipe import ControladorEquipe

class ControladorSistema:
    def __init__(self):
        self.__controlador_aluno = ControladorAluno(self)
        self.__controlador_arbitro = ControladorArbitro(self)
        self.__controlador_curso = ControladorCurso(self)
        self.__controlador_equipe = ControladorEquipe(self)
        self.__controlador_partida = ControladorPartida(self)
        self.__controlador_campeonato = ControladorCampeonato(self)
        self.__tela_sistema = TelaSistema()
    
#######################################################
    def inicializa_sistema(self):
        self.abre_tela()
#######################################################
    @property
    def controlador_aluno(self):
        return self.__controlador_aluno
    
    @property
    def controlador_arbitro(self):
        return self.__controlador_arbitro

    @property
    def controlador_curso(self):
        return self.__controlador_curso

    @property
    def controlador_equipe(self):
        return self.__controlador_equipe

    @property
    def controlador_campeonato(self):
        return self.__controlador_campeonato

    @property
    def controlador_partida(self):
        return self.__controlador_partida
#################################################

    def controla_arbitos(self):
        # Chama o controlador de Arbitros
        self.__controlador_arbitro.abre_tela_arbitro()

    def controla_alunos(self):
        # Chama o controlador de Alunos
        self.__controlador_aluno.abre_tela_aluno()
    
    def controla_partida(self):
        self.__controlador_partida.abre_tela_partida()
    
    def controla_equipe(self):
        self.__controlador_equipe.abre_tela_equipe()

    def controla_curso(self):
        self.__controlador_curso.abre_tela_curso()

    def controla_campeonato(self):
        self.__controlador_campeonato.abre_tela_campeonato()

    def busca_equipe(self, equipe: str):
       return self.__controlador_equipe.pega_equipe_por_nome(equipe)
    
    def busca_arbitro(self):
        return self.__controlador_arbitro.busca_arbitro()
    
    def valida_curso(self, curso: str):
        return self.__controlador_curso.valida_curso(curso)

##################################################################
    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.controla_alunos, 2: self.controla_arbitos, 3: self.controla_curso,
                        4: self.controla_equipe, 5: self.controla_partida, 6: self.controla_campeonato, 
                        0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
