import PySimpleGUI as sg

class TelaEquipe:
    def __init__(self):
        self.__window = None

    def tela_opcoes_equipe(self):
        sg.theme('BlueMono')
        layout = [
            [sg.Text('-------- EQUIPE --------', font=("Times New Roman", 18))],
            [sg.Text('Escolha sua opção:', font=("Times New Roman", 14))],
            [sg.Radio('Listar equipes', "RD1", key='1')],
            [sg.Radio('Adicionar equipe', "RD1", key='2')],
            [sg.Radio('Excluir equipe', "RD1", key='3')],
            [sg.Radio('Alterar dados da equipe', "RD1", key='4')],
            [sg.Radio('Adicionar aluno à equipe', "RD1", key='5')],
            [sg.Radio('Remover aluno da equipe', "RD1", key='6')],
            [sg.Radio('Voltar para o menu inicial', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Opções de Equipe').Layout(layout)

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
        elif values['5']:
            opcao = 5
        elif values['6']:
            opcao = 6
        elif values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def solicita_dados_equipe(self):
        sg.theme('BlueMono')
        layout = [
            [sg.Text('-------- DADOS EQUIPE ----------', font=("Times New Roman", 25))],
            [sg.Text('Nome:', font=("Times New Roman", 12)), sg.InputText('', key='nome')],
            [sg.Text('Curso:', size=(15, 1), font=("Times New Roman", 12)), sg.InputText('', key='curso')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Nome da Equipe').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        curso = values['curso']

        self.close()
        return {"nome": nome, "curso": curso}
    
    def solicita_equipe(self):
        sg.theme('BlueMono')
        layout = [
            [sg.Text('-------- SELECIONAR EQUIPE ----------', font=("Times New Roman", 25))],
            [sg.Text('Digite o nome da equipe que deseja selecionar:', font=("Times New Roman", 15))],
            [sg.Text('Nome equipe:', size=(15, 1), font=("Times New Roman", 12)), sg.InputText('', key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona Aluno').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        self.close()
        return nome

    def solicita_curso(self):
        sg.theme('BlueMono')
        layout = [
            [sg.Text('Digite o nome do curso:', font=("Times New Roman", 14))],
            [sg.InputText('', key='curso')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Curso da Equipe').Layout(layout)

        button, values = self.open()
        nome_curso = values['curso']
        self.close()
        return nome_curso

    def solicita_matricula_aluno(self):
        sg.theme('BlueMono')
        layout = [
            [sg.Text('Digite a matrícula do aluno:', font=("Times New Roman", 14))],
            [sg.InputText('', key='matricula')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Matrícula do Aluno').Layout(layout)

        button, values = self.open()
        matricula_aluno = values['matricula']
        self.close()
        return matricula_aluno

    def mostra_dados_equipes(self, todos_dados_equipes):
        layout = [
            [sg.Text('-------- DADOS DAS EQUIPES ----------')], 
            [sg.Multiline(todos_dados_equipes, size=(50, 20), disabled=True)]
        ]
        self.__window = sg.Window("Dados das Equipes", layout, resizable=True)
        button, values = self.__window.read()
        self.__window.close()

    def mostra_curso_equipe(self, equipe):
        if equipe.curso:
            sg.popup(f"Curso da equipe {equipe.nome}: {equipe.curso.nome}", title='Curso da Equipe', font=("Times New Roman", 14))
        else:
            sg.popup(f"Curso da equipe {equipe.nome}: Não definido", title='Curso da Equipe', font=("Times New Roman", 14))

    def mostra_pontos_equipe(self, equipe):
        sg.popup(f"Número de pontos da equipe {equipe.nome}: {equipe.num_pontos}", title='Pontos da Equipe', font=("Times New Roman", 14))

    def mostrar_mensagem(self, mensagem):
        sg.popup(mensagem, font=("Times New Roman", 14))

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()
