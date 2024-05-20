class TelaEquipe:
    def __init__(self):
        pass 

    def tela_opcoes_equipe(self):
        print("\n-------- EQUIPE --------")
        print("1: Listar equipes")
        print("2: Adicionar equipe")
        print("3: Excluir equipe")
        print("4: Alterar dados da equipe")
        print("5: Adicionar aluno à equipe")
        print("6: Remover aluno da equipe")
        print("7: Voltar para o menu inicial")
        print()
        return int(input("Digite a opção desejada: "))

    def solicita_equipe(self):
        nome = input("Digite o nome da equipe: ")
        return nome
    
    def solicita_curso(self):
        return input("Digite o nome do curso: ")
    
    def solicita_matricula_aluno(self):
        return input("Digite a matricula do aluno que deseja adicionar à equipe: ")

    def mostra_dados_equipe(self, equipe):
        print(f"Nome: {equipe.nome}")
        print("Alunos:")
        for aluno in equipe.alunos:
            print(f"  - {aluno.nome}") 

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def mostra_curso_equipe(self, equipe):
        print(f"Curso da equipe {equipe.nome}: {equipe.curso.nome if equipe.curso else 'Não definido'}")

    def mostra_pontos_equipe(self, equipe):
        print(f"Número de pontos da equipe {equipe.nome}: {equipe.num_pontos}")

    def mostrar_mensagem(self, mensagem):
        print(mensagem)