

class TelaCampeonato:
    def tela_opcoes_campeonato(self):
        print("\n-------- CAMPEONATO --------")
        print("1: Criar Novo Campeonato")
        print("2: Listar Campeonatos")
        print("3: Selecionar Campeonato")
        print("0: Voltar para o menu inicial")
        return int(input("Digite a opção desejada: "))

    def  solicita_nome_campeonato(self):
        return input("Digite o nome do campeonato: ")

    def mostra_dados_campeonato(self, campeonato):
        print(f"Nome do Campeonato: {campeonato.nome_campeonato}")
        print("Equipes:")
        for equipe in campeonato.equipes:
            print(f"  - {equipe.nome}")
        print("Partidas:")
        # for partida in campeonato.get_partidas():
        #     print(f"  - {partida}")  # Assumindo que você tem uma representação em string para a partida

    def mostra_partidas_campeonato(self, campeonato):
        print(f"Partidas do Campeonato: {campeonato.nome_campeonato}")
        for i, partida in enumerate(campeonato.get_partidas()):
            print(f"Partida {i+1}: {partida}")  # Assumindo que 'partida' tem uma representação em string

    def mostra_ganhador_campeonato(self, campeonato):
        ganhador = campeonato.get_ganhador()
        if ganhador:
            print(f"Ganhador do Campeonato {campeonato.nome_campeonato}: {ganhador.get_nome()}")
        else:
            print(f"O campeonato {campeonato.nome_campeonato} ainda não tem um ganhador definido.")

    def mostrar_mensagem(self, mensagem):
        print(mensagem)