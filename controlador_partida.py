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
