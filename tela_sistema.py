

class TelaSistema():
    #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_opcoes(self):
        print("-------- GERENCIAMENTO DE CAMPEONATOS DE FUTEBOL DA UFSC ---------")
        print("Escolha sua opcao")
        print("1 - Alunos")
        print("2 - Árbitros")
        print("3 - Equipes") #add demais
        print("0 - Finalizar sistema")
        opcao = int(input("Escolha a opcão: "))
        return opcao