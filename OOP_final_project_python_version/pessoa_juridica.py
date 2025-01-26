from pessoa import Pessoa
from endereco import Endereco

class PessoaJuridica(Pessoa):
    def __init__(self, nome_fantasia, num_funcionario, nome_oficial, cpf_cnpj, endereco, telefone):
        super().__init__(nome_oficial, cpf_cnpj, endereco, telefone)
        self.__nome_fantasia = nome_fantasia
        self.__num_funcionario = num_funcionario



    @property
    def cnpj(self):
        return self.cpf_cnpj

    @property
    def nome_fantasia(self):
        return self.__nome_fantasia

    @nome_fantasia.setter
    def nome_fantasia(self, nome_fantasia):
        self.__nome_fantasia = nome_fantasia

    @property
    def num_funcionario(self):
        return self.__num_funcionario

    @num_funcionario.setter
    def num_funcionario(self, num_funcionario):
        self.__num_funcionario = num_funcionario

    @property
    def cnpj(self):
        return super().cpf_cnpj

    def apresentar_dados_pessoa_juridica(self):
        print("==== Dados da Pessoa Jurídica ====")
        print("Nome Oficial: " + self.nome_oficial)
        print("CNPJ: " + self.cnpj)
        print("Endereço: " + str(self.endereco))
        print("Telefone: " + self.telefone)
        print("Nome Fantasia: " + self.nome_fantasia)
        print("Número de Funcionários: " + str(self.num_funcionario))
        print("===================================")
