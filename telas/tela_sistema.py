import PySimpleGUI as sg

class TelaSistema:
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        elif values['3']:
            opcao = 3
        elif values['4']:
            opcao = 4
        elif values['5']:
            opcao = 5
        elif values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        sg.theme('BlueMono')
        layout = [
            [sg.Text('-------- GERENCIAMENTO DE CAMPEONATOS DE FUTEBOL DA UFSC ---------', font=("Times New Roman", 25))],
            [sg.Text('Escolha sua opção', font=("Times New Roman", 15))],
            [sg.Radio('Alunos', "RD1", key='1')],
            [sg.Radio('Árbitros', "RD1", key='2')],
            [sg.Radio('Cursos', "RD1", key='3')],
            [sg.Radio('Equipes', "RD1", key='4')],
            [sg.Radio('Campeonato', "RD1", key='5')],
            [sg.Radio('Finalizar sistema', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Gerenciamento').Layout(layout)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
