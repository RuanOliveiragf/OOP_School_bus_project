from pessoa_juridica import PessoaJuridica

class Escola(PessoaJuridica):
    def __init__(self, nome, nome_fantasia, num_funcionario, nome_oficial, cpf_cnpj, endereco, telefone):
        super().__init__(nome_fantasia, num_funcionario, nome_oficial, cpf_cnpj, endereco, telefone)
        self.__nome = nome
        self.__alunos = []

    def apresentar_dados(self):
        super().apresentar_dados()
        print("Nome: " + self.nome)
        print("CNPJ: " + self.cpf_cnpj)
        print("Telefone: " + self.telefone)
        print("Endereço: " + str(self.endereco))
        print("Alunos Matriculados: " + self.exibir_alunos())

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def matricular_aluno(self, aluno):
        self.__alunos.append(aluno)
        return "Aluno matriculado com sucesso"

    def exibir_alunos(self):
        t = " "
        for aluno in self.__alunos:
            t += " " + self.listar_alunos(aluno)
        return t

    def listar_alunos(self, aluno):
        return "\nMatrícula: " + str(aluno.matricula) + " | Nome: " + aluno.nome_oficial + " | Série: " + aluno.serie

    # Demais getters e setters herdados de PessoaJuridica podem ser mantidos aqui
