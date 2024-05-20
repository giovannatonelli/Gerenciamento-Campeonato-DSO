

class TelaAluno():
    #tratamento de dados(str...)
    def tela_opcoes_aluno(self):
        print()
        print("-------- ALUNO --------")
        print("1: Listar alunos")
        print("2: Adicionar aluno")
        print("3: Excluir aluno")
        print("4: Alterar dados do aluno")
        print("0: Voltar para o menu incial")
        print()
        opcao_escolhida = int(input("Digite a opção desejada: "))
        return opcao_escolhida

    def solicita_dados_aluno(self):
        print()
        print("Insira aqui os dados do aluno:")
        while True:
            try:
                nome = input("Nome: ").strip()
                # if not nome:
                #     raise ValueError("Nome inválido. Por favor, insira um nome válido.")
                
                cpf = input("CPF: ").strip()
                # if not cpf.isdigit() or len(cpf) != 11:
                #     raise ValueError("CPF inválido. Por favor, insira um CPF válido contendo apenas dígitos.")
                
                data_nascimento = input("Data de nascimento(ddmmyy): ").strip()
                # if not len(data_nascimento) != 8:
                #     raise ValueError("Verifique se está digitando a data de nascimento no formato ddmmyy")

                matricula = input("Matrícula: ").strip()
                # if not matricula:
                #     raise ValueError("Matrícula inválida. Por favor, insira uma matrícula válida.")

                curso = input("Nome do curso: ").strip()
            
                # Se todas as entradas forem válidas, saímos do loop
                break
            
            except ValueError as e:
                print("Erro:", e)

        return {"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "matricula": matricula, "curso": curso}

    def mostra_dados_aluno(self, dados_aluno):
        print()
        print("NOME: ", dados_aluno["nome"])
        print("CPF: ", dados_aluno["cpf"])
        print("DATA DE NASCIMENTO: ", dados_aluno["data_nascimento"])
        print("MATRICULA: ", dados_aluno["matricula"])
        print("CURSO:", dados_aluno ["curso"] )

    def seleciona_aluno(self):
        matricula = input("Digite a matricula do aluno que deseja: ")
        return matricula

    def mostrar_mensagem(self, mensagem):
        print(mensagem)