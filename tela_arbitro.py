from controladorarbitro import ControladorArbitro


class TelaArbitro():
    #tratamento de dados(str...)
    def tela_opcoes_arbitro(self):
        print("ÁRBITROS DA UFSC")
        print("Escolha uma das opções: ")
        print("1: Listar árbitros")
        print("2: Adicionar árbitro")
        print("3: Excluir árbitro")
        print("4: Alterar dados do árbitro")
        print("5: Voltar para o menu incial")

        opcao_escolhida = int(input("Digite a opção desejada"))
        return opcao_escolhida

    def pega_arbitro(self):
        print("DADOS AMIGO")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        data_nascimento = input("Data de nascimeneto: ")
        matricula = input("Matrícula: ")

        return {"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "matricula": matricula}

    def mostra_arbitro(self, dados_arbitro):
        print("NOME: ", dados_arbitro["nome"])
        print("CPF: ", dados_arbitro["cpf"])
        print("DATA DE NASCIMENTO: ", dados_arbitro["data_nascimento"])
        print("MATRICULA: ", dados_arbitro["matricula"])

    def escolhe_arbitro(self):
        matricula = input("Digite a matricula do arbitro que deseja escolher: ")
        return matricula

    def mostra_mensagem(self, mensagem):
        print(mensagem)

controlador_arbitro = ControladorArbitro()
print(controlador_arbitro.abre_tela)