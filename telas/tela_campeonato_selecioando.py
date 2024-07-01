import PySimpleGUI as sg

class TelaCampeonatoSelecionado:
    def __init__(self):
        self.__window = None

    def tela_opcoes_campeonato_selecionado(self, campeonato):
        self.init_opcoes(campeonato.nome_campeonato)
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
        elif values['7']:
            opcao = 7
        elif values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def mostra_nome_campeonato(self, campeonato):
        sg.popup(f"------------- {campeonato} -------------", font=("Times New Roman", 16))

    def escolhe_equipe(self):
        sg.theme('BlueMono')
        layout = [
            [sg.Text('Escolha equipe para fazer parte do campeonato:', font=("Times New Roman", 14))],
            [sg.InputText('', key='equipe')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Escolher Equipe').Layout(layout)

        button, values = self.open()
        equipe = values['equipe']
        self.close()
        return equipe

    def mostra_equipes(self, campeonato):
        sg.popup_scrolled('\n'.join([f'  - {equipe}' for equipe in campeonato.equipes]), title='Equipes', font=("Times New Roman", 14))

    def mostra_numero_de_equipes(self, campeonato):
        sg.popup(f'Número de equipes: {len(campeonato.equipes)}', font=("Times New Roman", 16))

    def mostra_partidas(self, campeonato):
        partidas = '\n'.join([f"  - {partida.equipe_1.nome}     x   {partida.equipe_2.nome}     - {partida.data_partida} - {partida.arbitro.nome}" for partida in campeonato.partidas])
        sg.popup_scrolled(partidas, title='Partidas', font=("Times New Roman", 14))

    def mostra_resultado_partida(self, partida):
        sg.popup(f"  - {partida.equipe_1.nome} {partida.num_gols_eq1}    x   {partida.num_gols_eq2} {partida.equipe_2.nome}  - {partida.data_partida}", font=("Times New Roman", 14))

    def mostrar_podio(self, podio: dict):
        podio_str = '\n'.join([f"Time: {chave.nome}, Pontos: {valor[0]}, Saldo de Gols: {valor[1]}" for chave, valor in podio])
        sg.popup_scrolled(podio_str, title='Pódio', font=("Times New Roman", 14))

    def mostrar_mensagem(self, msg: str):
        sg.popup(msg, font=("Times New Roman", 14))

    def init_opcoes(self, nome_campeonato):
        sg.theme('BlueMono')
        layout = [
            [sg.Text(f'------------- {nome_campeonato} -------------', font=("Times New Roman", 16))],
            [sg.Text('Escolha sua opção:', font=("Times New Roman", 14))],
            [sg.Radio('Adicionar Equipes', "RD1", key='1')],
            [sg.Radio('Mostrar Equipes', "RD1", key='2')],
            [sg.Radio('Número de Equipes', "RD1", key='3')],
            [sg.Radio('Mostrar Partidas', "RD1", key='4')],
            [sg.Radio('Gerar Partidas', "RD1", key='5')],
            [sg.Radio('Gerar Resultados', "RD1", key='6')],
            [sg.Radio('Mostrar Pódio', "RD1", key='7')],
            [sg.Radio('Voltar para CAMPEONATOS', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Opções do Campeonato').Layout(layout)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
