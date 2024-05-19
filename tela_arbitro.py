

class TelaArbitro():
    #tratamento de dados(str...)
    def tela_opcoes_arbitro(self):
        print()
        print("-------- ÁRBITRO --------")
        print("1: Listar árbitros")
        print("2: Adicionar árbitro")
        print("3: Excluir árbitro")
        print("4: Alterar dados do árbitro")
        print("5: Voltar para o menu incial")
        print()
        opcao_escolhida = int(input("Digite a opção desejada: "))
        return opcao_escolhida

    def solicita_dados_arbitro(self):
        print()
        print("Insira aqui os dados do aluno:")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        data_nascimento = input("Data de nascimeneto: ")
        num_partidas = input("Número de Partidas: ")

        return {"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "num_partidas": num_partidas}

    def mostra_dados_arbitro(self, dados_arbitro):
        print("NOME: ", dados_arbitro["nome"])
        print("CPF: ", dados_arbitro["cpf"])
        print("DATA DE NASCIMENTO: ", dados_arbitro["data_nascimento"])
        print("NÚMERO DE PARTIDAS: ", dados_arbitro["num_partidas"])

    def escolhe_arbitro(self):
        cpf = input("Digite o CPF do árbitro que deseja escolher: ")
        return cpf

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

