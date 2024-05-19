class ControladorCampeonato:
    def __init__(self):
        self.campeonatos = []
        self.tela_campeonato = TelaCampeonato()

    def cria_novo_campeonato(self):
        nome_campeonato = self.tela_campeonato.solicita_nome_campeonato()
        equipes = self.solicita_equipes_campeonato()  # Função para adicionar equipes ao campeonato
        novo_campeonato = Campeonato(equipes=equipes, nome_campeonato=nome_campeonato)
        self.campeonatos.append(novo_campeonato)
        self.tela_campeonato.mostrar_mensagem("Campeonato criado com sucesso!")

    def solicita_equipes_campeonato(self):
        equipes = []
        while True:
            nome_equipe = input("Digite o nome da equipe (ou deixe em branco para finalizar): ")
            if not nome_equipe:
                break
            #buscar a equipe pelo nome
            equipe = self.pega_equipe_por_nome(nome_equipe)  # lógica de busca
            if equipe:
                equipes.append(equipe)
            else:
                print("Equipe não encontrada!")
        return equipes

    def listar_campeonatos(self):
        if self.campeonatos:
            for campeonato in self.campeonatos:
                self.tela_campeonato.mostra_dados_campeonato(campeonato)
        else:
            self.tela_campeonato.mostrar_mensagem("Nenhum campeonato cadastrado!")

    def abre_tela_campeonato(self):
        while True:
            opcao = self.tela_campeonato.tela_opcoes_campeonato()
            if opcao == 1:
                self.cria_novo_campeonato()
            elif opcao == 2:
                self.listar_campeonatos()
            elif opcao == 3:
                self.inclui_ganhador_campeonato()
            elif opcao == 4:
                return 
            else:
                print("Opção inválida!")

    def inclui_ganhador_campeonato(self):
        nome_campeonato = self.tela_campeonato.solicita_nome_campeonato()
        campeonato = self.pega_campeonato_por_nome(nome_campeonato)
        if campeonato:
            nome_equipe_ganhadora = input("Digite o nome da equipe ganhadora: ")
            equipe_ganhadora = self.pega_equipe_por_nome(nome_equipe_ganhadora)
            if equipe_ganhadora:
                campeonato.set_ganhador(equipe_ganhadora)  #método set_ganhador em Campeonato
                self.tela_campeonato.mostrar_mensagem("Ganhador do campeonato definido com sucesso!")
            else:
                print("Equipe não encontrada!")
        else:
            print("Campeonato não encontrado!")

    def pega_campeonato_por_nome(self, nome):
        for campeonato in self.campeonatos:
            if campeonato.get_nome_campeonato() == nome:
                return campeonato
        return None

    def pega_equipe_por_nome(self, nome_equipe):
        # lógica para buscar a equipe pelo nome
        pass 