from arbitro import Arbitro
from tela_arbitro import TelaArbitro


class ControladorArbitro():
    def __init__(self):
        self.__arbitros = []
        self.__tela_arbitro = TelaArbitro()

    def pega_arbitro_por_cpf(self, cpf: str):
        for arbitro in self.__arbitros:
            if(arbitro.cpf == cpf):
                return arbitro

    def inclui_arbitro(self):
        dados_arbitro = self.__tela_arbitro.solicita_dados_arbitro()
        novo_arbitro = Arbitro (dados_arbitro["nome"], dados_arbitro["cpf"], dados_arbitro["data_nascimento"], dados_arbitro["num_partidas"])
        if isinstance(novo_arbitro, Arbitro):
            for arbitro in self.__arbitros:
                if novo_arbitro.matricula == arbitro.matricula:
                    return None
                self.__arbitros.append(novo_arbitro)
                return novo_arbitro

    def listar_arbitros(self):
        for arbitro in self.__arbitros:
            self.__tela_arbitro.mostra_dados_arbitro({"nome": arbitro.nome, "cpf": arbitro.cpf, "data_nascimento": arbitro.data_nascimento, "matricula": arbitro.matricula})
        if len(self.__arbitros) == 0:
            self.__tela_arbitro.mostrar_mensagem("A lista está vazia")

    def altera_arbitro(self):
        self.lista_arbitros()
        matricula_arbitro = self.__tela_arbitro.seleciona_arbitro()
        arbitro = self.pega_arbitro_por_matricula(matricula_arbitro)

        if(arbitro is not None):
            novos_dados_arbitro = self.__tela_arbitro.solicita_dados_arbitro()
            arbitro.nome = novos_dados_arbitro["nome"]
            arbitro.cpf = novos_dados_arbitro["cpf"]
            arbitro.data_nascimento = novos_dados_arbitro["data_nascimento"]
            arbitro.matricula =  novos_dados_arbitro["matricula"]

    def exclui_arbitro(self):
        self.__listar_arbitros()
        matricula_arbitro = self.__tela_arbitro.escolhe_amigo()
        arbitro = self.pega_arbitro_por_matricula(matricula_arbitro)

        if(arbitro is not None):
            self.__arbitros.remove(arbitro)
            self.__tela.arbitro.mostrar_mensagem("arbitro removido com sucesso")
            #avaliar possibilidade de colocar uma opcao "deseja listar os arbitros?"
            self.listar_arbitros()
        else:
            self.__tela_arbitro.mostrar_mensagem("Esse arbitro não existe")

    def retornar_incio(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.listar_arbitros, 2: self.inclui_arbitro, 3: self.exclui_arbitro, 4: self.altera_arbitro, 5: self.retornar_incio}

        executando = True 
        while executando:
            lista_opcoes[self.__tela_arbitro.tela_opcoes_arbitro()]()