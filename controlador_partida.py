##controlador partida
import random
from controlador_arbitro import ControladorArbitro
from arbitro import Arbitro
from partida import Partida
from tela_partida import TelaPartida
from equipe import Equipe

class ControladorPartida():
    def __init__(self, controlador_sistema):
        self.__tela_partida = TelaPartida()
        self.__controlador_sistema = controlador_sistema

    def valida_quantidade_equipes(self):
        try:
                if self.__controlador_sistema.valida_quantidade_equipes():
                    self.define_partidas()
                else:
                    raise Exception("Quantidade de equipes insuficiente")
        except Exception as e:
                self.__tela_partida.mostrar_mensagem(f"Erro: {e}")
                self.retornar_incio()
                



    def pega_partida_por_id(self, id_partida: int):
        for partida in self.__partidas:
            if(partida.id_partida == id_partida):
                return partida
            
    def escolhe_equipe_1(self):
        self.__tela_partida.escolhe_equipe1()

    def inicia_partida(self):
        self.__tela_partida.solicita_dados_partida()
        equipe1 = self.__tela_partida.escolhe_equipe1()
        if isinstance(self.__controlador_sistema.busca_equipe(equipe1), Equipe):
            equipe2 = self.__tela_partida.escolhe_equipe2()
            if isinstance(self.__controlador_sistema.busca_equipe(equipe2), Equipe):
                if equipe1 != equipe2:
                    arbitro = self.__tela_partida.escolhe_arbitro()
                    if isinstance(self.__controlador_sistema.busca_arbitro(arbitro), Arbitro):
                        print("oi")
                       

    def abre_tela_partida(self):
        lista_opcoes = {1: self.inicia_partida, 0:self.retornar_incio}

        executando = True 
        while executando:
            lista_opcoes[self.__tela_partida.tela_opcoes_partida()]()

    def retornar_incio(self):
        self.__controlador_sistema.abre_tela_partida()