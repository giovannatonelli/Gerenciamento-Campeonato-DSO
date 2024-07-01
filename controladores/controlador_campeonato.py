from telas.tela_campeonato import TelaCampeonato
from telas.tela_campeonato_selecioando import TelaCampeonatoSelecionado
from entidades.campeonato import Campeonato
from entidades.equipe import Equipe
from entidades.partida import Partida
from itertools import combinations
import random
from datetime import datetime, timedelta
from exceptions.campeonato_exceptions import CampeonatoNaoExisteException
from exceptions.campeonato_exceptions import EquipesInsuficientesException
from exceptions.equipes_exceptions import EquipeNaoExisteException
from exceptions.lista_vazia_exception import ListaVaziaException
from DAOS.campeonato_dao import CampeonatoDAO

class ControladorCampeonato:
    def __init__(self, controlador_sistema):
        #self.__campeonato_DAO = []
        self.__campeonato_DAO = CampeonatoDAO()
        self.__tela_campeonato = TelaCampeonato()
        self.__campeonato = None
        self.__tela_campeonato_selecionado = TelaCampeonatoSelecionado()
        self.__controlador_sistema = controlador_sistema

    def cria_novo_campeonato(self):
        nome_campeonato = self.__tela_campeonato.solicita_nome_campeonato()
        novo_campeonato = Campeonato(nome_campeonato)
        self.__campeonato_DAO.add(novo_campeonato)
        self.__campeonato = novo_campeonato

    def seleciona_campeonato(self):
        try:
            nome = self.__tela_campeonato.solicita_nome_campeonato()
            if len(self.__campeonato_DAO.get_all()) == 0:
                raise CampeonatoNaoExisteException()
            for campeonato in self.__campeonato_DAO.get_all():
                if campeonato.nome_campeonato == nome:
                    self.__campeonato = campeonato
                    self.abre_tela_campeonato_selecionado()
                else:
                    raise CampeonatoNaoExisteException()
        except CampeonatoNaoExisteException as e:
            self.__tela_campeonato.mostrar_mensagem(e)

    def gera_partidas(self):
        try:
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
                raise EquipesInsuficientesException()
        except EquipesInsuficientesException as e:
                self.__tela_campeonato_selecionado.mostrar_mensagem(e)


    def gera_resultado_partida(self):
        for partida in self.__campeonato.partidas:
            partida.num_gols_eq1 = random.randint(0, 10)
            partida.num_gols_eq2 = random.randint(0, 10)
            self.__tela_campeonato_selecionado.mostra_resultado_partida(partida)
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

    def mostrar_podio(self):
        podio = self.__campeonato.definir_podio()
        self.__tela_campeonato_selecionado.mostrar_podio(podio)

    def gera_data_aleatoria(self):
        inicio = datetime(2024,4,7)
        fim  = datetime(2024,10,7)
        delta = fim - inicio
        int_delta = delta.days
        dias_aleatorios = random.randint(0, int_delta)
        data_aleatoria = inicio + timedelta(days=dias_aleatorios)
        data_formatada = data_aleatoria.strftime('%d/%m/%Y')
        return data_formatada

    def valida_quantidade_equipes(self):
        if len(self.__campeonato.equipes) >= 2:
            return True
        return False

    def mostra_dados_do_campeonato(self):
        self.__tela_campeonato.mostra_dados_campeonatos(self.__campeonato)

    def mostrar_nome_campeonato(self):
        self.__tela_campeonato_selecionado.mostra_nome_campeonato(self.__campeonato)

    def mostrar_equipes(self):
        self.__tela_campeonato_selecionado.mostra_equipes(self.__campeonato)
    
    def mostrar_numero_de_equipes(self):
        self.__tela_campeonato_selecionado.mostra_numero_de_equipes(self.__campeonato)

    def mostrar_partidas(self):
        self.__tela_campeonato_selecionado.mostra_partidas(self.__campeonato)

    def adc_equipe_no_campeonato(self):
        equipe = self.__controlador_sistema.busca_equipe(self.__tela_campeonato_selecionado.escolhe_equipe())
        try:
            if isinstance(equipe, Equipe):
                self.__campeonato.adc_equipe(equipe)
            else:
                raise EquipeNaoExisteException()
        except EquipeNaoExisteException as e:
                self.__tela_campeonato_selecionado.mostrar_mensagem(e)
                self.__abre_tela_campeonato_selecionado()
        
    def listar_campeonatos(self):
        try:
            if not self.__campeonato_DAO:
                raise ListaVaziaException()
            
            todos_dados_campeonatos = ""
            for campeonato in self.__campeonato_DAO.get_all():
                dados_campeonato = f"Nome do Campeonato: {campeonato.nome_campeonato}\n\nEquipes:\n" + \
                                '\n'.join([f"  - {equipe.nome}" for equipe in campeonato.equipes]) + "\n\n"
                todos_dados_campeonatos += dados_campeonato
            
            self.__tela_campeonato.mostra_dados_campeonatos(todos_dados_campeonatos)
        
        except ListaVaziaException as e:
            self.__tela_campeonato.mostrar_mensagem(e)

    def abre_tela_campeonato(self):
        lista_opcoes = {1: self.cria_novo_campeonato, 
                        2: self.listar_campeonatos, 
                        3: self.seleciona_campeonato, 
                        0: self.retornar_incio}
        while True:
            opcao_escolhida = self.__tela_campeonato.tela_opcoes_campeonato()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def abre_tela_campeonato_selecionado(self):
        lista_opcoes = {1: self.adc_equipe_no_campeonato , 
                        2: self.mostrar_equipes, 
                        3: self.mostrar_numero_de_equipes, 
                        4: self.mostrar_partidas,
                        5:self.gera_partidas, 
                        6: self.gera_resultado_partida, 
                        7:self.mostrar_podio, 
                        0: self.abre_tela_campeonato}
        while True:
            opcao_escolhida = self.__tela_campeonato_selecionado.tela_opcoes_campeonato_selecionado(self.__campeonato)
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def retornar_incio(self):
        self.__controlador_sistema.abre_tela()