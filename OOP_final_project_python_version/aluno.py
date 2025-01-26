from pessoa_fisica import PessoaFisica

class Aluno(PessoaFisica):
    def __init__(self, matricula, serie, nome, mae, pai, naturalidade, data_nascimento, nome_oficial, cpf_cnpj, endereco, telefone):
        super().__init__(nome, mae, pai, naturalidade, data_nascimento, nome_oficial, cpf_cnpj, endereco, telefone)
        self.__matricula = matricula
        self.__serie = serie
        

    def apresentar_dados(self):
        super().apresentar_dados()
        #print(self.endereco)
        print("Matrícula: " + str(self.matricula))
        print("Série: " + self.serie)

    def verificar_tipo(self):
        tipo_super_classe = super().verificar_tipo()
        return tipo_super_classe + " Aluno"

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def serie(self):
        return self.__serie

    @serie.setter
    def serie(self, serie):
        self.__serie = serie
