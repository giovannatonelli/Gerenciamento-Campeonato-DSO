from controladoraluno import ControladorAluno

class TelaAluno():
    #tratamento de dados(str...)
    def tela_opcoes_aluno(self):
        print("ALUNOS DA UFSC")
        print("Escolha uma das opções: ")
        print("1: Listar alunos")
        print("2: Adicionar aluno")
        print("3: Excluir aluno")
        print("4: Alterar dados do aluno")
        print("5: Voltar para o menu incial")

        opcao_escolhida = int(input("Digite a opção desejada"))
        return opcao_escolhida

    def pega_aluno(self):
        print("DADOS AMIGO")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        data_nascimento = input("Data de nascimeneto: ")
        matricula = input("Matrícula: ")

        return {"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "matricula": matricula}

    def mostra_aluno(self, dados_aluno):
        print("NOME: ", dados_aluno["nome"])
        print("CPF: ", dados_aluno["cpf"])
        print("DATA DE NASCIMENTO: ", dados_aluno["data_nascimento"])
        print("MATRICULA: ", dados_aluno["matricula"])

    def escolhe_aluno(self):
        matricula = input("Digite a matricula do aluno que deseja escolher: ")
        return matricula

    def mostra_mensagem(self, mensagem):
        print(mensagem)

controlador_aluno = ControladorAluno()
print(controlador_aluno.abre_tela)