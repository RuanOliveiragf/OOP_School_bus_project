# Conteúdo do arquivo main.py
from rotas import Rota
from pessoa_juridica import PessoaJuridica
from pessoa_fisica import PessoaFisica
from endereco import Endereco
from datetime import date
from escola import Escola
from aluno import Aluno
from ponto_de_parada import PontoDeParada
from contrato import Contrato
from motorista import Motorista

# Exemplo de utilização
endereco_exemplo = Endereco(rua="Rua ABC", numero=123, complemento="", bairro="Centro")
data_nascimento_exemplo = date(2000, 1, 1)  # Substitua isso pela data desejada

pessoa_fisica_exemplo = PessoaFisica(
    nome="Fulano",
    mae="Mãe",
    pai="Pai",
    naturalidade="Cidade",
    data_nascimento=data_nascimento_exemplo,
    nome_oficial="Fulano Silva",
    cpf_cnpj="123.456.789-01",
    endereco=endereco_exemplo,
    telefone="987654321"
)

# Exibindo dados da pessoa física
pessoa_fisica_exemplo.apresentar_dados_pessoa_fisica()

# Exemplo de utilização
pessoa_juridica_exemplo = PessoaJuridica(
    nome_fantasia="Empresa ABC",
    num_funcionario=50,
    nome_oficial="Empresa ABC Ltda.",
    cpf_cnpj="12.345.678/0001-90",
    endereco=endereco_exemplo,
    telefone="987654321"
)

# Exibindo dados da pessoa jurídica
pessoa_juridica_exemplo.apresentar_dados_pessoa_juridica()

# Criando um objeto Aluno
aluno_exemplo = Aluno(matricula=1, serie="9º ano", nome="Aluno 1", mae="Mãe 1", pai="Pai 1",
                      naturalidade="Cidade 1", data_nascimento=date(2005, 5, 5), nome_oficial="Aluno 1 Silva",
                      cpf_cnpj="987.654.321-01", endereco=endereco_exemplo, telefone="123456789")

aluno_exemplo2 = Aluno(matricula=2, serie="8º ano", nome="Aluno 2", mae="Mãe 2", pai="Pai 2",
                       naturalidade="Cidade 2", data_nascimento=date(2006, 6, 6), nome_oficial="Aluno 2 Silva",
                       cpf_cnpj="876.543.210-01", endereco=endereco_exemplo, telefone="987654321")

# Criando um objeto Escola
endereco_escola = Endereco(rua="Rua da Escola", numero=123, complemento="", bairro="Centro")
escola_exemplo = Escola(nome="Escola Primária", nome_fantasia="Escola ABC", num_funcionario=30,
                        nome_oficial="Escola Primária Ltda.", cpf_cnpj="12.345.678/0001-90", endereco=endereco_escola,
                        telefone="987654321")

# Criando dois pontos de parada
ponto1 = PontoDeParada(nome="Ponto 1", latitude=123.456, longitude=-45.678)
ponto2 = PontoDeParada(nome="Ponto 2", latitude=456.789, longitude=-67.890)

# Criando uma rota
rota_exemplo = Rota()

# Adicionando os pontos de parada à rota
rota_exemplo.adiciona_ponto(ponto1)
rota_exemplo.adiciona_ponto(ponto2)

# Matriculando o aluno na escola
escola_exemplo.matricular_aluno(aluno_exemplo)
escola_exemplo.matricular_aluno(aluno_exemplo2)

# Criando um contrato
data_inicio_contrato = date(2022, 1, 1)
data_fim_contrato = date(2022, 12, 31)
contrato_exemplo = Contrato(num_contrato=1, data_inicio=data_inicio_contrato, data_fim=data_fim_contrato, valor=5000.0)

# Criando um motorista
endereco_motorista = Endereco(rua="Rua do Motorista", numero=123, complemento="", bairro="Centro")
motorista_exemplo = Motorista(num_habilitacao="123456789", cat_habilitacao="A", tipo=1, num_contrato=1, nome="Motorista",
                              mae="Mãe Motorista", pai="Pai Motorista", naturalidade="Cidade Motorista",
                              data_nascimento=date(1990, 5, 10), nome_oficial="Motorista Silva",
                              cpf_cnpj="987.654.321-01", endereco=endereco_motorista, telefone="555-1234")

# Adicionando o contrato ao motorista
motorista_exemplo.add_contrato(contrato_exemplo)

# Apresentando os dados do aluno
print("\nDados do Aluno:")
aluno_exemplo.apresentar_dados()

print("\nDados do Segundo Aluno:")
aluno_exemplo2.apresentar_dados()

# Apresentando os dados da escola
escola_exemplo.apresentar_dados()

# Mostrando os dados da rota
print("\nDados da Rota:")
rota_exemplo.mostrar_dados()

motorista_exemplo.apresentar_dados()