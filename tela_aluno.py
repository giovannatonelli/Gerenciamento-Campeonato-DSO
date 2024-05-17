

class TelaAluno():
    #tratamento de dados(str...)
    def tela_opcoes_aluno(self):
        print()
        print("-------- ALUNO --------")
        print("1: Listar alunos")
        print("2: Adicionar aluno")
        print("3: Excluir aluno")
        print("4: Alterar dados do aluno")
        print("5: Voltar para o menu incial")
        print()
        opcao_escolhida = int(input("Digite a opção desejada: "))
        return opcao_escolhida

    def solicita_dados_aluno(self):
        print()
        print("Insira aqui os dados do aluno:")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        data_nascimento = input("Data de nascimento: ")
        matricula = input("Matrícula: ")

        return {"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "matricula": matricula}

    def mostra_dados_aluno(self, dados_aluno):
        print()
        print("NOME: ", dados_aluno["nome"])
        print("CPF: ", dados_aluno["cpf"])
        print("DATA DE NASCIMENTO: ", dados_aluno["data_nascimento"])
        print("MATRICULA: ", dados_aluno["matricula"])

    def seleciona_aluno(self):
        matricula = input("Digite a matricula do aluno que deseja: ")
        return matricula

    def mostrar_mensagem(self, mensagem):
        print(mensagem)
