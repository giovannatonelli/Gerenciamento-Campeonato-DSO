import PySimpleGUI as sg

class TelaCurso:
    def __init__(self):
        self.__window = None

    def tela_opcoes_curso(self):
        sg.theme('BlueMono')
        layout = [
            [sg.Text('-------- CURSO --------', font=("Times New Roman", 18))],
            [sg.Text('Escolha sua opção:', font=("Times New Roman", 14))],
            [sg.Radio('Listar cursos', "RD1", key='1')],
            [sg.Radio('Adicionar curso', "RD1", key='2')],
            [sg.Radio('Excluir curso', "RD1", key='3')],
            [sg.Radio('Alterar dados do curso', "RD1", key='4')],
            [sg.Radio('Voltar para o menu inicial', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Opções de Curso').Layout(layout)

        button, values = self.open()
        opcao = None
        if values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        elif values['3']:
            opcao = 3
        elif values['4']:
            opcao = 4
        elif values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def solicita_dados_curso(self):
        sg.theme('BlueMono')
        layout = [
            [sg.Text('Digite o código do curso:', font=("Times New Roman", 14))],
            [sg.InputText('', key='codigo')],
            [sg.Text('Digite o nome do curso:', font=("Times New Roman", 14))],
            [sg.InputText('', key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Dados do Curso').Layout(layout)

        button, values = self.open()
        codigo_curso = values['codigo']
        nome_curso = values['nome']
        self.close()
        return codigo_curso, nome_curso

    def seleciona_curso(self):
        sg.theme('BlueMono')
        layout = [
            [sg.Text('-------- SELECIONAR CURSO ----------', font=("Times New Roman", 25))],
            [sg.Text('Digite o código do curso que deseja selecionar:', font=("Times New Roman", 15))],
            [sg.Text('Código:', size=(15, 1), font=("Times New Roman", 12)), sg.InputText('', key='codigo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona Curso').Layout(layout)

        button, values = self.open()
        codigo = values['codigo']
        self.close()
        return codigo

    def mostra_dados_cursos(self, todos_dados_cursos):
        layout = [
            [sg.Text('-------- DADOS DOS CURSOS ----------')], 
            [sg.Multiline(todos_dados_cursos, size=(50, 20), disabled=True)]
            
        ]
        self.__window = sg.Window("Dados dos Cursos", layout, resizable=True)
        button, values = self.__window.read()
        self.__window.close()

    def mostra_equipe_curso(self, curso):
        if curso.equipe:
            sg.popup(f"Equipe associada: {curso.equipe.nome}", title='Equipe do Curso', font=("Times New Roman", 14))
        else:
            sg.popup("Nenhuma equipe associada a este curso.", title='Equipe do Curso', font=("Times New Roman", 14))

    def mostrar_mensagem(self, mensagem):
        sg.popup(mensagem, font=("Times New Roman", 14))

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()
