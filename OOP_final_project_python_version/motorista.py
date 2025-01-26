from pessoa_fisica import PessoaFisica
from endereco import Endereco
from datetime import date

class Motorista(PessoaFisica):
    __total_rotas = 0

    def __init__(self, num_habilitacao, cat_habilitacao, tipo, num_contrato, nome, mae, pai, naturalidade, data_nascimento, nome_oficial, cpf_cnpj, endereco, telefone):
        super().__init__(nome, mae, pai, naturalidade, data_nascimento, nome_oficial, cpf_cnpj, endereco, telefone)
        self.__num_habilitacao = num_habilitacao
        self.__cat_habilitacao = cat_habilitacao
        self.__tipo = tipo
        self.__num_contrato = num_contrato
        self.__contratos = []

    def __init__(self, num_habilitacao, cat_habilitacao, tipo, nome, mae, pai, naturalidade, data_nascimento, nome_oficial, cpf_cnpj, endereco, telefone):
        super().__init__(nome, mae, pai, naturalidade, data_nascimento, nome_oficial, cpf_cnpj, endereco, telefone)
        self.__num_habilitacao = num_habilitacao
        self.__cat_habilitacao = cat_habilitacao
        self.__tipo = tipo
        self.__contratos = []


    @property
    def num_habilitacao(self):
        return self.__num_habilitacao

    @num_habilitacao.setter
    def num_habilitacao(self, num_habilitacao):
        self.__num_habilitacao = num_habilitacao

    @property
    def cat_habilitacao(self):
        return self.__cat_habilitacao

    @cat_habilitacao.setter
    def cat_habilitacao(self, cat_habilitacao):
        self.__cat_habilitacao = cat_habilitacao

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def num_contrato(self):
        return self.__num_contrato

    @num_contrato.setter
    def num_contrato(self, num_contrato):
        if self.tipo == 0:
            print("Método inválido")
        else:
            self.__num_contrato = num_contrato

    def add_contrato(self, contrato):
        if self.tipo == 1 and self.num_contrato != 0:
            self.__contratos.append(contrato)
            return "Contrato adicionado"
        elif self.tipo == 1 and self.num_contrato == 0:
            return "Motorista terceirizado sem número de contrato informado, impossível adicionar"
        else:
            return "O motorista é do tipo servidor público, não é possível associá-lo a um contrato"

    def exige_contrato(self):
        if self.tipo == 1 and self.num_contrato == 0:
            print("Insira o número do contrato")
        else:
            self.num_contrato = num_contrato

    def verifica_motorista(self):
        if self.tipo == 0:
            return "O motorista é servidor"
        else:
            return "O motorista é terceirizado"
        
    

    def apresentar_dados(self):
        super().apresentar_dados()
        print(self.endereco)
        print("Número de Habilitação:", self.num_habilitacao)
        print("Categoria de Habilitação:", self.cat_habilitacao)
        print("Tipo:", "Servidor Público" if self.tipo == 0 else "Terceirizado")
        if self.tipo == 1:
            print("Número de Contrato:", self.num_contrato)
            print("Contratos:")
            for contrato in self.__contratos:
                print(contrato)

    def verificar_tipo(self):
        tipo_super_classe = super().verificar_tipo()
        return tipo_super_classe + " Motorista"

    def __str__(self):
        contratos_str = [str(contrato) for contrato in self.__contratos]
        contratos_str = "\n".join(contratos_str)
        return f"{super().__str__()}, Número de Habilitação: {self.num_habilitacao}, Categoria de Habilitação: {self.cat_habilitacao}, Tipo: {self.tipo}, Número de Contrato: {self.num_contrato}\nContratos:\n{contratos_str}"

    def __repr__(self):
        return self.__str__()

