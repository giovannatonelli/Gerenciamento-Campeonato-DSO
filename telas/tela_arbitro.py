import PySimpleGUI as sg

class TelaArbitro:
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes_arbitro(self):
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
        elif values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        sg.theme('BlueMono')
        layout = [
            [sg.Text('-------- ÁRBITRO --------', font=("Times New Roman", 25))],
            [sg.Text('Escolha sua opção', font=("Times New Roman", 15))],
            [sg.Radio('Listar árbitros', "RD1", key='1')],
            [sg.Radio('Adicionar árbitro', "RD1", key='2')],
            [sg.Radio('Excluir árbitro', "RD1", key='3')],
            [sg.Radio('Alterar dados do árbitro', "RD1", key='4')],
            [sg.Radio('Voltar para o menu inicial', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Árbitros').Layout(layout)

    def solicita_dados_arbitro(self):
        sg.theme('BlueMono')
        layout = [
            [sg.Text('-------- DADOS ÁRBITRO ----------', font=("Times New Roman", 25))],
            [sg.Text('Nome:', size=(15, 1), font=("Times New Roman", 12)), sg.InputText('', key='nome')],
            [sg.Text('CPF:', size=(15, 1), font=("Times New Roman", 12)), sg.InputText('', key='cpf')],
            [sg.Text('Data de nascimento (ddmmyy):', size=(15, 1), font=("Times New Roman", 12)), sg.InputText('', key='data_nascimento')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Árbitros').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        cpf = values['cpf']
        data_nascimento = values['data_nascimento']

        self.close()
        return {"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento}

    def mostra_dados_arbitro(self, todos_dados_arbitros):
        layout = [
            [sg.Text('-------- DADOS DOS ÁRBITROS ----------')], 
            [sg.Multiline(todos_dados_arbitros, size=(50, 20), disabled=True)]
        ]
        self.__window = sg.Window("Dados dos Árbitros", layout, resizable=True)
        button, values = self.__window.read()
        self.__window.close()

    def escolhe_arbitro(self):
        sg.theme('BlueMono')
        layout = [
            [sg.Text('-------- SELECIONAR ÁRBITRO ----------', font=("Times New Roman", 25))],
            [sg.Text('Digite o CPF do árbitro que deseja selecionar:', font=("Times New Roman", 15))],
            [sg.Text('CPF:', size=(15, 1), font=("Times New Roman", 12)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona Árbitro').Layout(layout)

        button, values = self.open()
        cpf = values['cpf']
        self.close()
        return cpf

    def mostrar_mensagem(self, mensagem):
        sg.popup("", mensagem)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
