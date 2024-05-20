import random

class TelaPartida():
    def tela_opcoes_partida(self):
        print()
        print("-------- PARTIDAS --------")
        print("1: Listar partidas")
        print("2: Adicionar partida")
        print("3: Alterar dados partida")
        print("4: Informações da Partida")
        print("0: Voltar para o menu incial")
        print()
        opcao_escolhida = int(input("Digite a opção desejada: "))
        return opcao_escolhida
    
    
    def ecolhe_arbitro(self):
        arbitro = input("Digite o CPF do arbrito: ")
        return arbitro
    
    def solicita_dados_partida(self):
        print("-------------")
        print("Insira os dados")
        # print("Insira aqui os dados da partida:")
        # id_partida = input("ID da Partida: ")
        # equipe_1 = input("Equipe 1: ")
        # equipe_2 = input("Equipe 2: ")
        # data_partida = input("Data da Partida: ")
        # num_gols_eq1 = inputs("Número de gols da equipe 1")
        # num_gols_eq2 = input("Número de gols da equipe 2")
        # arbitro = input("Árbitro que apitou a partida")

        # return {"id_partida": id_partida, "equipe_1": equipe_1, "equipe_2": equipe_2,
        #         "data_partida": data_partida, "num_gols_eq1": num_gols_eq1,
        #         "num_gols_eq2": num_gols_eq2, "arbitro": arbitro}

    def mostra_dados_partida(self, dados_partida):
        print()
        print("ID DA PARTIDA: ", dados_partida["id_partida"])
        print("EQUIPE 1: ", dados_partida["equipe_1"])
        print("EQUIPE 2: ", dados_partida["equipe_2"])
        print("DATA DA PARTIDA: ", dados_partida["data_partida"])
        print("NÚMERO DE GOLS DA EQUIPE 1: ", dados_partida["num_gols_eq1"])
        print("NÚMERO DE GOLS DA EQUIPE 2: ", dados_partida["num_gols_eq2"])
        print("ARBITRO DA PARTIDA: ", dados_partida["arbitro"])

    def seleciona_partida(self):
        id_partida = input("Digite o ID da partida que deseja: ")
        return id_partida

    def mostrar_mensagem(self, mensagem):
        print(mensagem)
    
    def mostrar_mensagem(self, mensagem):
        print(mensagem)


##1. Cada curso precisa ter pelo menos 1 time.
#2. Em cada time, só podem ser cadastrados alunos do mesmo curso.
##3. Cada partida tem time ganhador, perdedor ou empate. O número de gols que cada
#time fez pode ser registrado manualmente ou gerado aleatoriamente.
#4. O sistema escolhe aleatoriamente as primeiras partidas e calcula as próximas com base
#nos resultados.
#5. Ao final de cada partida, o número de partidas do referido árbitro deve ser
#incrementado.