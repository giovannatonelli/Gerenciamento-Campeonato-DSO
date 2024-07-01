import random
from entidades.arbitro import Arbitro
from telas.tela_arbitro import TelaArbitro
from exceptions.arbitro_exceptions import ArbitroRepetidoException
from exceptions.lista_vazia_exception import ListaVaziaException
from exceptions.pessoas_exceptions import PessoaNCadastradaException
from exceptions.arbitro_exceptions import ArbitroNCadastradoException
from DAOS.arbitro_dao import ArbitroDAO

class ControladorArbitro():
    def __init__(self, controlador_sistema):
        #self.__arbitros = []
        self.__arbitro_DAO = ArbitroDAO()
        self.__tela_arbitro = TelaArbitro()
        self.__controlador_sistema = controlador_sistema

    def pega_arbitro_por_cpf(self, cpf: str):
        #for arbitro in self.__arbitros:
        for arbitro in self.__arbitro_DAO.get_all():
            if(arbitro.cpf == cpf):
                return arbitro
            else:
                return None

    def inclui_arbitro(self):
        dados_arbitro = self.__tela_arbitro.solicita_dados_arbitro()
        try:
            novo_arbitro = Arbitro (dados_arbitro["nome"], 
                                dados_arbitro["cpf"], 
                                dados_arbitro["data_nascimento"])
            if not self.__controlador_sistema.valida_cpf( dados_arbitro["cpf"]):
                raise ValueError("CPF inválido. Por favor, digite um CPF válido")
            elif isinstance(novo_arbitro, Arbitro):
                try:
                    #for arbitro in self.__arbitros:
                    for arbitro in self.__arbitro_DAO.get_all():
                        if novo_arbitro.cpf == arbitro.cpf:
                            raise ArbitroRepetidoException()
                    #self.__arbitros.append(novo_arbitro)
                    self.__arbitro_DAO.add(novo_arbitro)
                    self.__tela_arbitro.mostrar_mensagem("Árbitro adicionado com sucesso")
                    return novo_arbitro
                except ArbitroRepetidoException as e:
                    self.__tela_arbitro.mostrar_mensagem(e)
        except ValueError as e:
            self.__tela_arbitro.mostrar_mensagem(e)

    def listar_arbitros(self):
        try:
            #if len(self.__arbitros) == 0:
            if len(self.__arbitro_DAO.get_all()) == 0:
                raise ListaVaziaException()
            
            todos_dados_arbitros = ""
            #for arbitro in self.__arbitros:
            for arbitro in self.__arbitro_DAO.get_all():
                dados_arbitro = f"NOME: {arbitro.nome}\nCPF: {arbitro.cpf}\nDATA DE NASCIMENTO: {arbitro.data_nascimento}\nNÚMERO DE PARTIDAS: {arbitro.num_partidas}\n\n"
                todos_dados_arbitros += dados_arbitro
            
            self.__tela_arbitro.mostra_dados_arbitro(todos_dados_arbitros)

        except ListaVaziaException as e:
            self.__tela_arbitro.mostrar_mensagem(e)

    def altera_arbitro(self):
        cpf_arbitro = self.__tela_arbitro.escolhe_arbitro()
        arbitro = self.pega_arbitro_por_cpf(cpf_arbitro)

        if(arbitro is not None):
            novos_dados_arbitro = self.__tela_arbitro.solicita_dados_arbitro()
            arbitro.nome = novos_dados_arbitro["nome"]
            arbitro.cpf = novos_dados_arbitro["cpf"]
            arbitro.data_nascimento = novos_dados_arbitro["data_nascimento"]
            self.__arbitro_DAO.update(arbitro)

    def exclui_arbitro(self):
        cpf_arbitro = self.__tela_arbitro.escolhe_arbitro()
        arbitro = self.pega_arbitro_por_cpf(cpf_arbitro)
        try:
            if(arbitro is not None):
                #self.__arbitros.remove(arbitro)
                self.__arbitro_DAO.remove(arbitro.cpf)
                self.__tela_arbitro.mostrar_mensagem("Árbitro removido com sucesso")
            else:
                raise PessoaNCadastradaException
        except PessoaNCadastradaException as e:
                self.__tela_arbitro.mostrar_mensagem(e)

    def busca_arbitro(self):
        try:
            if len(self.__arbitro_DAO.get_all()) == 0: 
            #if len(self.__arbitros) == 0:
                raise ArbitroNCadastradoException
            else:
                return random.choice(list(self.__arbitro_DAO.get_all()))
        except ArbitroNCadastradoException as e:
            self.__tela_arbitro.mostrar_mensagem(e)
        

    def retornar_incio(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela_arbitro(self):
        lista_opcoes = {1: self.listar_arbitros, 
                        2: self.inclui_arbitro, 
                        3: self.exclui_arbitro, 
                        4: self.altera_arbitro, 
                        0: self.retornar_incio}

        executando = True 
        while executando:
            lista_opcoes[self.__tela_arbitro.tela_opcoes_arbitro()]()