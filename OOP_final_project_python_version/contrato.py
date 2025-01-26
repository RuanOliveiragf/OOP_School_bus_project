from datetime import date
from motorista import Motorista
#from veiculo import Veiculo
from fornecedor import Fornecedor
from pessoa_juridica import PessoaJuridica

class Contrato:
    def __init__(self, num_contrato, data_inicio, data_fim, valor):
        self.__num_contrato = num_contrato
        self.__data_inicio = data_inicio
        self.__data_fim = data_fim
        self.__valor = valor
        self.__veiculo = []
        self.__motorista = []
        self.__fornecedor = []

    @property
    def num_contrato(self):
        return self.__num_contrato

    @num_contrato.setter
    def num_contrato(self, num_contrato):
        self.__num_contrato = num_contrato

    @property
    def data_inicio(self):
        return self.__data_inicio

    @data_inicio.setter
    def data_inicio(self, data_inicio):
        self.__data_inicio = data_inicio

    @property
    def data_fim(self):
        return self.__data_fim

    @data_fim.setter
    def data_fim(self, data_fim):
        self.__data_fim = data_fim

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    def altera_veiculo(self, veiculo):
        if veiculo.tipo == 1:
            self.__veiculo.append(veiculo)
            return "Veículo adicionado com sucesso"
        else:
            return "Veículo próprio não pode ser adicionado"
    '''
    def remove_veiculo(self, placa):
        for v in self.__veiculo:
            if v.placa == placa:
                self.__veiculo.remove(v)
                return "Veículo removido com sucesso"
        return "Veículo não consta no contrato para ser removido"
    '''

    #so adciona se for forncedor
    
    def adiciona_pessoa_juridica(self, pessoa_juridica):
            if isinstance(pessoa_juridica, PessoaJuridica) and isinstance(pessoa_juridica, Fornecedor):
                self.__fornecedor.append(pessoa_juridica)
                return "Pessoa Jurídica (Fornecedor) adicionada com sucesso ao contrato"
            else:
                return "Erro: O objeto fornecido não é uma Pessoa Jurídica (Fornecedor) válida."


    def adiciona_fornecedor(self, fornecedor):
        self.__fornecedor.append(fornecedor)

    def altera_motorista(self, motorista):
        if motorista.tipo == 1:
            self.__motorista.append(motorista)
            return "Motorista adicionado com sucesso"
        else:
            return "Motorista servidor não pode ser adicionado"

    def remove_motorista(self, cpf_cnpj):
        for m in self.__motorista:
            if m.cpf_cnpj == cpf_cnpj:
                self.__motorista.remove(m)
                return "Motorista removido com sucesso"
        return "Motorista não consta no contrato para ser removido"
    
    