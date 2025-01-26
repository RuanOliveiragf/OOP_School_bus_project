from pessoa_juridica import PessoaJuridica
#from contrato import Contrato

class Fornecedor(PessoaJuridica):
    def __init__(self, nome_fantasia, num_funcionario, nome_oficial, cpf_cnpj, endereco, telefone):
        super().__init__(nome_fantasia, num_funcionario, nome_oficial, cpf_cnpj, endereco, telefone)
        self.__contratos = []

    @property
    def contratos(self):
        return self.__contratos

    @contratos.setter
    def contratos(self, contratos):
        self.__contratos = contratos

    def __str__(self):
        return f"{super().__str__()}, Contratos: {self.contratos}"

    def __repr__(self):
        return self.__str__()

    def verificar_tipo(self):
        tipo_super_classe = super().verificar_tipo()
        return tipo_super_classe + " Fornecedor"
