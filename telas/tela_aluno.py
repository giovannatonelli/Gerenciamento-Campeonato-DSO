import PySimpleGUI as sg

class TelaAluno:
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes_aluno(self):
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
            [sg.Text('-------- ALUNOS ----------', font=("Times New Roman", 25))],
            [sg.Text('Escolha sua opção', font=("Times New Roman", 15))],
            [sg.Radio('Listar alunos', "RD1", key='1')],
            [sg.Radio('Adicionar aluno', "RD1", key='2')],
            [sg.Radio('Excluir aluno', "RD1", key='3')],
            [sg.Radio('Alterar dados do aluno', "RD1", key='4')],
            [sg.Radio('Voltar para o menu inicial', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Alunos').Layout(layout)

    def solicita_dados_aluno(self):
        sg.theme('BlueMono')
        layout = [
            [sg.Text('-------- DADOS ALUNO ----------', font=("Times New Roman", 25))],
            [sg.Text('Nome:', size=(15, 1), font=("Times New Roman", 12)), sg.InputText('', key='nome')],
            [sg.Text('CPF:', size=(15, 1), font=("Times New Roman", 12)), sg.InputText('', key='cpf')],
            [sg.Text('Data de nascimento (ddmmyy):', size=(15, 1), font=("Times New Roman", 12)), sg.InputText('', key='data_nascimento')],
            [sg.Text('Matrícula:', size=(15, 1), font=("Times New Roman", 12)), sg.InputText('', key='matricula')],
            [sg.Text('Curso:', size=(15, 1), font=("Times New Roman", 12)), sg.InputText('', key='curso')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Alunos').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        cpf = values['cpf']
        data_nascimento = values['data_nascimento']
        matricula = values['matricula']
        curso = values['curso']

        self.close()
        return {"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "matricula": matricula, "curso": curso}

    def mostra_dados_aluno(self, todos_dados_alunos):
        layout = [
            [sg.Text('-------- DADOS DOS ALUNOS ----------')], 
            [sg.Multiline(todos_dados_alunos, size=(50, 20), disabled=True)]
        ]
        self.__window = sg.Window("Dados dos Alunos", layout, resizable=True)
        button, values = self.__window.read()
        self.__window.close()

    def seleciona_aluno(self):
        sg.theme('BlueMono')
        layout = [
            [sg.Text('-------- SELECIONAR ALUNO ----------', font=("Times New Roman", 25))],
            [sg.Text('Digite a matrícula do aluno que deseja selecionar:', font=("Times New Roman", 15))],
            [sg.Text('Matrícula:', size=(15, 1), font=("Times New Roman", 12)), sg.InputText('', key='matricula')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona Aluno').Layout(layout)

        button, values = self.open()
        matricula = values['matricula']
        self.close()
        return matricula

    def mostrar_mensagem(self, mensagem):
        sg.popup("", mensagem)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
