class TelaCampeonatoSelecionado:
    def tela_opcoes_campeonato_selecionado(self, campeonato):
        self.mostra_nome_campeonato(campeonato)
        print("1: Adicionar Equipes")
        print("2: Mostrar Equipes")
        print("3: Número de Equipes")
        print("4: Mostrar Partidas")
        print("5: Gerar Partidas")
        print("6: Gerar Resultados")
        print("7: Mostrar Pódio")
        print("0: Voltar para CAMPEONATOS")
        return int(input("Digite a opção desejada: "))
    
    def mostra_nome_campeonato(self, campeonato):
        print("-------------",campeonato.nome_campeonato,"-------------")

    def escolhe_equipe(self):
        return input("Escolha equipe para fazer parte do campeonato: ")

    def mostra_equipes(self, campeonato):
        print()
        print("Equipes:")
        for equipe in campeonato.equipes:
            print(f"  - {equipe.nome}")

    def mostra_numero_de_equipes(self, campeonato):
        print(len(campeonato.equipes))
    
    def mostra_partidas(self, campeonato):
        print("Partidas:")
        for partida in campeonato.partidas:
            print(f"  - {partida.equipe_1.nome}     x   {partida.equipe_2.nome}     - {partida.data_partida} - {partida.arbitro.nome}")

        print()
            
    def mostra_resultado_partida(self, partida):
        print(f"  - {partida.equipe_1.nome} {partida.num_gols_eq1}    x   {partida.num_gols_eq2} {partida.equipe_2.nome}  - {partida.data_partida}")

    def mostrar_podio(self, podio: dict):
        for chave, valor in podio:
            print(f"Time: {chave.nome}, Pontos: {valor[0]}, Saldo de Gols: {valor[1]}")

    def mostrar_mensagem(self, msg: str):
        print(msg)
