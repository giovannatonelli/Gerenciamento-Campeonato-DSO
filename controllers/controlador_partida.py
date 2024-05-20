##controlador partida
import random
from tela_campeonato import TelaCampeonato
from tela_campeonato_selecioando import TelaCampeonatoSelecionado
from controlador_arbitro import ControladorArbitro
from arbitro import Arbitro
from partida import Partida
from equipe import Equipe
from itertools import combinations
import random
from datetime import datetime, timedelta


class ControladorPartida():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__campeonato = None
        self.__tela_campeonato_selecionado = TelaCampeonatoSelecionado()
        self.__controlador_sistema = controlador_sistema


    def valida_quantidade_equipes(self):
        if len(self.__campeonato.equipes) >= 2:
            return True
        return False

########################################################
    def gera_partidas(self):
        if self.valida_quantidade_equipes():
            confrontos = list(combinations(self.__campeonato.equipes, 2))
            random.shuffle(confrontos)
            for partida in confrontos:
                equipe1 = partida[0]
                equipe2 = partida[1]
                arbitro = self.__controlador_sistema.busca_arbitro()
                data = self.gera_data_aleatoria()
                partida = Partida(equipe1, equipe2, arbitro, data)
                self.__campeonato.adc_partida(partida)
                arbitro.adc_num_partidas()
            self.__campeonato.gera_tabela_pontuacao()
            self.__tela_campeonato_selecionado.mostrar_mensagem("Partidas geradas com sucesso")
        else:
            self.__tela_campeonato_selecionado.mostrar_mensagem("Quantidade de equipes insuficiente")
            self.__abre_tela_campeonato_selecionado()

    def gera_resultado_partida(self):
        for partida in self.__campeonato.partidas:
            partida.num_gols_eq1 = random.randint(0, 10)
            partida.num_gols_eq2 = random.randint(0, 10)
            self.__tela_campeonato_selecionado.mostra_resultado_partida(partida)
            #fazer a validação para os artilheiros
            self.gera_pontuacao_partida(partida)   
    
    def gera_pontuacao_partida(self, partida):
        gols_eq1 = partida.num_gols_eq1
        gols_eq2 = partida.num_gols_eq2
        if gols_eq1 > gols_eq2:
            self.__campeonato.adiciona_pontucao_equipe(partida.equipe_1, 3)
        elif gols_eq2 > gols_eq1:
            self.__campeonato.adiciona_pontucao_equipe(partida.equipe_2, 3)
        else:
            self.__campeonato.adiciona_pontucao_equipe(partida.equipe_1, 1)
            self.__campeonato.adiciona_pontucao_equipe(partida.equipe_2, 1)
        self.__campeonato.adiciona_saldo_de_gols(partida.equipe_1, (gols_eq1-gols_eq2))
        self.__campeonato.adiciona_saldo_de_gols(partida.equipe_2, (gols_eq2-gols_eq1))