##controlador partida
import random
from controlador_arbitro import ControladorArbitro
from tela_arbitro import TelaArbitro
from arbitro import Arbitro
from partida import Partida
from tela_partida import TelaPartida

class ControladorPartida():
    def __init__(self):
        self.__partidas = []
        self.__tela_partida = TelaPartida()

    def pega_partida_por_id(self, id_partida: int):
        for partida in self.__partidas:
            if(partida.id_partida == id_partida):
                return partida

    def inclui_partida(self):
        dados_partida = self.__tela_partida.solicita_dados_partida()
        nova_partida = Partida(dados_partida["id_partida"], dados_partida["equipe_1"],
                               dados_partida["equipe_2"], dados_partida["data_partida"],
                               dados_partida["num_gols_eq1"], dados_partida["num_gols_eq2"],
                               dados_partida["arbitro"])
        if isinstance(nova_partida, Partida):
            for partida in self.__partidas:
                if nova_partida.id_partida == partida.id_partida:
                    return None
            self.__partidas.append(nova_partida)
            return nova_partida

    def listar_partidas(self):
        for partida in self.__partidas:
            self.__tela_partida.mostra_dados_partida({"id_partida": partida.id_partida,
                                                      "equipe_1": partida.equipe_1,
                                                      "equipe_2": partida.equipe_2,
                                                      "data_partida": partida.data_partida,
                                                      "num_gols_eq1": partida.num_gols_eq1,
                                                      "num_gols_eq_2": partida.num_gols_eq2, 
                                                      "arbitro": partida.arbitro})
        if len(self.__partidas) == 0:
            self.__tela_partida.mostrar_mensagem("A lista de partidas está vazia")

    def time_ganhador(self, id_partida: int):
        partida = self.pega_partida_por_id(id_partida)
        if not partida:
            self.__tela_partida.mostrar_mensagem("Partida não encontrada")
            return None

        partida.num_gols_eq1 = random.randint(1, 10)
        partida.num_gols_eq2 = random.randint(1, 10)
    
        if partida.num_gols_eq1 > partida.num_gols_eq_2:
            resultado = f"A equipe vencedora dessa partida foi: {partida.equipe_1} com {partida.num_gols_eq1} gols"
        elif partida.num_gols_eq1 < partida.num_gols_eq2:
            resultado = f"A equipe vencedora dessa partida foi: {partida.equipe_2} com {partida.num_gols_eq2} gols"
        else:
            resultado = "O jogo terminou empatado"

        self.__tela_partida.mostrar_mensagem(resultado)
        return resultado



    #def registrar_partida(self):
        #arbitro = self.__tela_arbitro.escolhe_arbitro()
        #partida = Partida(id_partida, arbitro)
        #self.partidas[id_partida] = partida
        #arbitro.incrementar_partidas()


##3. Cada partida tem time ganhador, perdedor ou empate. O número de gols que cada
#time fez pode ser registrado manualmente ou gerado aleatoriamente.
#4. O sistema escolhe aleatoriamente as primeiras partidas e calcula as próximas com base
#nos resultados.
#5. Ao final de cada partida, o número de partidas do referido árbitro deve ser
#incrementado.