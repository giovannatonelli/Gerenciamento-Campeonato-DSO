from telas.tela_sistema import TelaSistema
from controladores.controlador_aluno import ControladorAluno
from controladores.controlador_arbitro import ControladorArbitro
from controladores.controlador_partida import ControladorPartida
from controladores.controlador_campeonato import ControladorCampeonato
from controladores.controlador_curso import ControladorCurso
from controladores.controlador_equipe import ControladorEquipe
import datetime

class ControladorSistema:
    def __init__(self):
        self.__controlador_aluno = ControladorAluno(self)
        self.__controlador_arbitro = ControladorArbitro(self)
        self.__controlador_curso = ControladorCurso(self)
        self.__controlador_equipe = ControladorEquipe(self)
        self.__controlador_partida = ControladorPartida(self)
        self.__controlador_campeonato = ControladorCampeonato(self)
        self.__tela_sistema = TelaSistema()

    def inicializa_sistema(self):
        self.abre_tela()

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
    
    def pega_aluno_por_matricula(self, matricula_aluno):
        return self.__controlador_aluno.pega_aluno_por_matricula(matricula_aluno)
    
    def valida_cpf(self, cpf):
        # Remove caracteres não numéricos
        cpf = ''.join(filter(str.isdigit, cpf))

        if len(cpf) != 11 or cpf == cpf[0] * 11:
            return False

        # Calcula o primeiro dígito verificador
        soma = 0
        for i in range(9):
            soma += int(cpf[i]) * (10 - i)
        digito1 = 11 - (soma % 11)
        if digito1 > 9:
            digito1 = 0

        # Calcula o segundo dígito verificador
        soma = 0
        for i in range(10):
            soma += int(cpf[i]) * (11 - i)
        digito2 = 11 - (soma % 11)
        if digito2 > 9:
            digito2 = 0

        # Verifica se os dígitos calculados são iguais aos fornecidos
        if int(cpf[9]) == digito1 and int(cpf[10]) == digito2:
            return True
        else:
            return False

    def valida_data_nascimento(self, data_nascimento):
        dia, mes, ano = map(int, data_nascimento.split('/'))
        try:
            datetime.date(ano, mes, dia)
            return True
        except ValueError:
            return False
                
    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.controla_alunos, 
                        2: self.controla_arbitos, 
                        3: self.controla_curso,
                        4: self.controla_equipe, 
                        5: self.controla_campeonato, 
                        0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
