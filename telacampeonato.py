class TelaCampeonato:
    def __init__(self):
        self.__controlador_campeonato = ControladorCampeonato()

    def tela_opcoes_campeonato(self):
        print("\n-------- CAMPEONATO --------")
        print("1: Criar Novo Campeonato")
        print("2: Listar Campeonatos")
        print("3: Incluir Ganhador do Campeonato")  # Opção para adicionar o ganhador posteriormente
        print("4: Voltar para o menu inicial")
        print()
        return int(input("Digite a opção desejada: "))

    def solicita_nome_campeonato(self):
        nome = input("Digite o nome do campeonato: ")
        return nome

    def mostra_dados_campeonato(self, campeonato):
        print(f"Nome do Campeonato: {campeonato.get_nome_campeonato()}")
        print("Equipes:")
        for equipe in campeonato.get_equipes():
            print(f"  - {equipe.get_nome()}")
        print("Partidas:")
        for partida in campeonato.get_partidas():
            print(f"  - {partida}")  # Assumindo que você tem uma representação em string para a partida

    def mostra_partidas_campeonato(self, campeonato):
        print(f"Partidas do Campeonato: {campeonato.get_nome_campeonato()}")
        for i, partida in enumerate(campeonato.get_partidas()):
            print(f"Partida {i+1}: {partida}")  # Assumindo que 'partida' tem uma representação em string

    def mostra_ganhador_campeonato(self, campeonato):
        ganhador = campeonato.get_ganhador()
        if ganhador:
            print(f"Ganhador do Campeonato {campeonato.get_nome_campeonato()}: {ganhador.get_nome()}")
        else:
            print(f"O campeonato {campeonato.get_nome_campeonato()} ainda não tem um ganhador definido.")