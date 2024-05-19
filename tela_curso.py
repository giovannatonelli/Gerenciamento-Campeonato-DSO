class TelaCurso:
    def __init__(self):
        pass

    def tela_opcoes_curso(self):
        print("\n-------- CURSO --------")
        print("1: Listar cursos")
        print("2: Adicionar curso")
        print("3: Excluir curso")
        print("4: Alterar dados do curso")
        print("5: Voltar para o menu inicial")
        print()
        return int(input("Digite a opção desejada: "))

    def solicita_dados_curso(self):
        codigo = int(input("Digite o código do curso: "))
        nome = input("Digite o nome do curso: ")
        return codigo, nome

    def mostra_dados_curso(self, curso):
        print(f"Código: {curso.codigo_curso}")
        print(f"Nome: {curso.nome_curso}")

    def mostra_equipe_curso(self, curso):
        if curso.equipe:
            print(f"Equipe associada: {curso.equipe.nome}")
        else:
            print("Nenhuma equipe associada a este curso.")