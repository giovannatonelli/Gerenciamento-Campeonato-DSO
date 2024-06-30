import PySimpleGUI as sg

class TelaCampeonato:
    def __init__(self):
        self.__window = None

    def tela_opcoes_campeonato(self):
        sg.theme('BlueMono')
        layout = [
            [sg.Text('-------- CAMPEONATO --------', font=("Times New Roman", 18))],
            [sg.Text('Escolha sua opção:', font=("Times New Roman", 14))],
            [sg.Radio('Criar Novo Campeonato', "RD1", key='1')],
            [sg.Radio('Listar Campeonatos', "RD1", key='2')],
            [sg.Radio('Selecionar Campeonato', "RD1", key='3')],
            [sg.Radio('Voltar para o menu inicial', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Opções de Campeonato').Layout(layout)

        button, values = self.open()
        opcao = None
        if values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        elif values['3']:
            opcao = 3
        elif values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def solicita_nome_campeonato(self):
        sg.theme('BlueMono')
        layout = [
            [sg.Text('Digite o nome do campeonato:', font=("Times New Roman", 14))],
            [sg.InputText('', key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Nome do Campeonato').Layout(layout)

        button, values = self.open()
        nome_campeonato = values['nome']
        self.close()
        return nome_campeonato

    def mostra_dados_campeonato(self, campeonato):
        sg.popup_scrolled(f"Nome do Campeonato: {campeonato.nome_campeonato}\n\nEquipes:\n" +
                          '\n'.join([f"  - {equipe.nome}" for equipe in campeonato.equipes]), title='Dados do Campeonato', font=("Times New Roman", 14))

    def mostra_partidas_campeonato(self, campeonato):
        sg.popup_scrolled(f"Partidas do Campeonato {campeonato.nome_campeonato}:\n\n" +
                          '\n'.join([f"Partida {i+1}: {partida}" for i, partida in enumerate(campeonato.get_partidas())]), title='Partidas do Campeonato', font=("Times New Roman", 14))

    def mostra_ganhador_campeonato(self, campeonato):
        ganhador = campeonato.get_ganhador()
        if ganhador:
            sg.popup(f"Ganhador do Campeonato {campeonato.nome_campeonato}: {ganhador.get_nome()}", font=("Times New Roman", 14))
        else:
            sg.popup(f"O campeonato {campeonato.nome_campeonato} ainda não tem um ganhador definido.", font=("Times New Roman", 14))

    def mostrar_mensagem(self, mensagem):
        sg.popup(mensagem, font=("Times New Roman", 14))

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()
