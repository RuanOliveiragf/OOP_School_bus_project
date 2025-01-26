import datetime
from escola import Escola
from endereco import Endereco
from aluno import Aluno
from motorista import Motorista
from contrato import Contrato
from ponto_de_parada import PontoDeParada
from rotas import Rota
from veiculo import Veiculo
from fornecedor import Fornecedor

objeto_aluno = []
objeto_escola = []
objeto_motorista = []
objeto_contrato = []
objeto_veiculo = []
objeto_ponto = []
objeto_rota = []
objeto_endereco = []
objeto_fornecedor = []

def trataOpcao():
    opcoes_validas = list(range(1, 15))  
    while True:
        try:
            opcao = int(input("Escolha uma das opções acima: "))
            if opcao in opcoes_validas:
                return opcao  
            else:
                print("Erro: Por favor, escolha uma opção válida.")
        except ValueError:
            print("Erro: Por favor, insira um número inteiro.")

def trataNumero():
    while True:
        try:
            numero = int(input("Informe o número: "))
            return numero  
        except ValueError:
            print("Erro: Por favor, insira um número inteiro.")

def trataNumeroContrato():
    while True:
        try:
            num_contrato = int(input("Número de contrato: "))
            return num_contrato  
        except ValueError:
            print("Erro: Por favor, insira um número inteiro para o número de contrato.")

def trataDataNascimento():
    while True:
        data_nascimento_str = input("Data de nascimento (DD/MM/AAAA): ")
        try:
            data_nascimento = datetime.datetime.strptime(data_nascimento_str, "%d/%m/%Y").date()
            return data_nascimento  
        except ValueError:
            print("Erro: Por favor, insira a data no formato correto (DD/MM/AAAA).")



opcao = 0

while opcao != 14:
    print("1 - Criar aluno")
    print("2 - Criar motorista")
    print("3 - Criar contrato")
    print("4 - Criar escola")
    print("5 - Criar veiculo")
    print("6 - Criar ponto de parada")
    print("7 - Criar uma nova rota, adicionando pontos de parada a ela")
    print("8 - Calcular a demanda de uma rota específica")
    print("9 - Exibir o número total de rotas criadas.")
    print("10 - Exibir o número total de pontos de parada criados.")
    print("11 - Exibir informações de um Aluno, Motorista, Escola ou Fornecedor")
    print("12 - Exibir o tipo da pessoa.")
    print("13 - Criar fornecedor")
    print("14 - Sair do programa.")

    opcao = trataOpcao()

    if opcao == 1:
        if not objeto_escola:
            print("Não há escolas, por favor, crie uma escolhendo a opção 4.")
        else:
            print("Informe o nome civil do aluno:")
            nome_oficial = input()
            
            print("Informe o nome do aluno:")
            nome = input()
            
            print("Informe o nome da mãe:")
            mae = input()
            
            print("Informe o nome do pai:")
            pai = input()
            
            print("Informe a naturalidade:")
            naturalidade = input()
            
            print("Informe o CPF:")
            cpf_cnpj = input()
            
            data_nascimento = trataDataNascimento()
            
            print("Informe a rua:")
            rua = input()
            
            numero = trataNumero()
 
            print("Informe o complemento:")
            complemento = input()
            
            print("Informe o bairro:")
            bairro = input()
            
            es_aluno = Endereco(rua, numero, complemento, bairro)
            objeto_endereco.append(es_aluno)
            
            print("Informe o telefone:")
            telefone = input()
            
            while True:
                try:
                    matricula = int(input("Informe a matrícula: "))
                    break  
                except ValueError:
                    print("Erro: Por favor, insira um número inteiro.")

            print("Matrícula inserida:", matricula)

            
            print("Informe a série:")
            serie = input()
            
            aluno = Aluno(matricula, serie, nome, mae, pai, naturalidade, data_nascimento, nome_oficial, cpf_cnpj, es_aluno, telefone)
            objeto_aluno.append(aluno)
        pass

    elif opcao == 2:

        tipo = int(input("Informe se o motorista é terceirizado (digite 1) ou se ele é servidor (digite 0): "))

        if tipo == 1:
            if not objeto_contrato:
                print("Não há contratos para vincular o motorista, por favor criar contrato utilizando a opção 3")
            else:
                nome_oficial = input("Nome civil: ")
                
                opcao = int(input("Deseja informar nome social [1] SIM [2] NAO"))
                
                if opcao == 1:
                    nome = input("Informe o nome social: ")
                else:
                    nome = nome_oficial

                mae = input("Nome da mãe: ")
                pai = input("Nome do pai: ")
                naturalidade = input("Naturalidade: ")
                cpf_cnpj = input("CPF/CNPJ: ")
                data_nascimento_str = input("Data de nascimento: ")
                data_nascimento = datetime.datetime.strptime(data_nascimento_str, "%d/%m/%Y").date()

                rua = input("Rua: ")
                numero = trataNumero()

                complemento = input("Complemento: ")
                bairro = input("Bairro: ")

                e = Endereco(rua, numero, complemento, bairro)
                objeto_endereco.append(e)
                
                telefone = input("Telefone: ")
                num_habilitacao = input("Número de habilitação: ")
                cat_habilitacao = input("Categoria de habilitação: ")

                print("Tipo: terceirizado")

                num_contrato = input("infore o nuero de contrato: ")

                tipo = 1
                z = Motorista(num_habilitacao, cat_habilitacao, num_contrato, nome, mae, pai, naturalidade, data_nascimento, nome_oficial, cpf_cnpj, e, telefone)
                objeto_motorista.append(z)

        elif tipo == 0:
            nome_oficial = input("Nome civil: ")

            opcao = input("deseja informar nome social [1]sim[2]nao")
            
            if opcao == 1:
                nome = input("Informe o nome social: ")
            else:
                nome = nome_oficial

            mae = input("Nome da mãe: ")
            pai = input("Nome do pai: ")
            naturalidade = input("Naturalidade: ")
            cpf_cnpj = input("CPF/CNPJ: ")

            data_nascimento = trataDataNascimento()

            rua = input("Rua: ")

            numero = trataNumero()

            complemento = input("Complemento: ")
            bairro = input("Bairro: ")
            
            e = Endereco(rua, numero, complemento, bairro)
            objeto_endereco.append(e)

            telefone = input("Telefone: ")
            num_habilitacao = input("Número de habilitação: ")
            cat_habilitacao = input("Categoria de habilitação: ")

            print("Tipo: servidor")
            tipo = 0
            z = Motorista(num_habilitacao, cat_habilitacao, tipo, nome, mae, pai, naturalidade, data_nascimento, nome_oficial, cpf_cnpj, e, telefone)
            objeto_motorista.append(z)

        else:
            print("Opção inválida")
        pass

    elif opcao == 3:
        print("Para criar um contrato, informe os dados solicitados abaixo:")
        num_contrato = trataNumeroContrato()
        data_inicio_str = input("Data de início do contrato (dd/MM/yyyy): ")
        data_inicio = datetime.datetime.strptime(data_inicio_str, "%d/%m/%Y").date()
        data_fim_str = input("Data de término do contrato (dd/MM/yyyy): ")
        data_fim = datetime.datetime.strptime(data_fim_str, "%d/%m/%Y").date()
        valor = float(input("Valor do contrato: "))
        c = Contrato(num_contrato, data_inicio, data_fim, valor)
        objeto_contrato.append(c)
        pass

    elif opcao == 4:
        print("Para criar uma escola, informe os seguintes dados: ")
        nome = input("Informe o nome da escola: ")
        nome_fantasia = input("Informe o nome fantasia: ")
        num_funcionario = int(input("Informe o número de funcionários: "))
        cpf_cnpj = input("Informe o CNPJ: ")
        telefone = input("Informe o telefone: ")
        rua = input("Rua: ")

        numero = trataNumero()

        complemento = input("Complemento: ")
        bairro = input("Bairro: ")
        nome_oficial = ""
        es = Endereco(rua, numero, complemento, bairro)
        objeto_endereco.append(es)
        y = Escola(nome,nome_fantasia,num_funcionario,nome_oficial,cpf_cnpj,es,telefone)
        objeto_escola.append(y)
        pass
    elif opcao == 5:
        print("Informe se o veiculo é próprio (digite 0) ou alugado (digite 1): ")
        tipo = int(input())

        if tipo == 1:
            if not objeto_contrato:
                print("Não há contratos para associar o veículo, por favor, criar um contrato selecionando a opção 3")
            else:
                placa = input("Placa do veículo: ")
                ano = int(input("Ano do veículo: "))
                modelo = input("Modelo do veículo: ")
                capacidade = int(input("Capacidade do veículo: "))
                print("Tipo do veículo: alugado")

                num_contrato = trataNumeroContrato()
                
                veiculo = Veiculo(placa, ano, modelo, capacidade, tipo, num_contrato)
                objeto_veiculo.append(veiculo)

        elif tipo == 0:
            placa = input("Placa do veículo: ")
            ano = int(input("Ano do veículo: "))
            modelo = input("Modelo do veículo: ")
            capacidade = int(input("Capacidade do veículo: "))
            print("Tipo do veículo: próprio")

            veiculo = Veiculo(placa, ano, modelo, capacidade, tipo)
            objeto_veiculo.append(veiculo)

        else:
            print("Opção inválida!")
        pass
    elif opcao == 6:
        print("Para criar um ponto de parada insira as seguintes informações")

        nome = input("Informe o nome do ponto: ")

        while True:
            try:
                latitude = float(input("Informe a latitude: "))
                break  
            except ValueError:
                print("Erro: Por favor, insira um número válido para a latitude.")

        print("Latitude inserida:", latitude)

        while True:
            try:
                longitude = float(input("Informe a longitude: "))
                break  
            except ValueError:
                print("Erro: Por favor, insira um número válido para a longitude.")

        print("Longitude inserida:", longitude)

        p = PontoDeParada(nome, latitude, longitude)
        objeto_ponto.append(p)
        pass

    elif opcao == 7:        
        
        rota = Rota()
        objeto_rota.append(rota)

        print("---Informe os pontos de parada da rota---")
        while True:
            try:
                opcao = int(input("Deseja informar um ponto? [1] SIM [0] NÃO "))
                if opcao == 1 or opcao == 0:
                    break  
                else:
                    print("Erro: Por favor, insira 1 para SIM ou 0 para NÃO.")
            except ValueError:
                print("Erro: Por favor, insira um número válido (1 ou 0).")

        print("Opção selecionada:", opcao)


        while opcao == 1:
            id_ponto = int(input("Informe o id do ponto que deseja adicionar: "))
            ponto_escolhido = None

            for ponto in objeto_ponto:
                if ponto.id == id_ponto:
                    ponto_escolhido = ponto
                    break

            if ponto_escolhido:
                rota.adiciona_ponto(ponto_escolhido)
                opcao = int(input("Ponto adicionado com sucesso. Deseja adicionar outro ponto? [1] SIM [0] NÃO"))
            else:
                opcao = int(input("Ponto não encontrado. Deseja informar outro ponto? [1] SIM [0] NÃO"))


        pass

    elif opcao == 8:
        id_rota = int(input("Informe o ID da rota: "))
        rota_encontrada = False

        for rota in objeto_rota:
            if rota.id == id_rota:
                
                print(f"A demanda da rota é: {rota.calcula_demanda()}")
                rota_encontrada = True
                break

        if not rota_encontrada:
            print("Rota não encontrada")
        pass

    elif opcao == 9:
        if not objeto_rota:
            print("Não há rotas criadas, selecionar a opção 7")
        else:
            print("Número total de rotas:", len(objeto_rota))

        pass
    elif opcao == 10:
        if not objeto_ponto:
            print("Não há pontos de parada criados")
        else:
            print("Número de pontos de parada criados:", len(objeto_ponto))
        pass
    elif opcao == 11:
        print("Informe que informação deseja obter:")
        print("[1] - Aluno")
        print("[2] - Motorista")
        print("[3] - Escola")
        print("[4] - Fornecedor")
        opcao = int(input())

        if opcao == 1:
            print("Informe o nome oficial do Aluno:")
            nome_oficial = input()
            aluno_encontrado = None

            for aluno in objeto_aluno:
                if aluno.nome_oficial == nome_oficial:
                    aluno_encontrado = aluno
                    break

            if aluno_encontrado:
                aluno_encontrado.apresentar_dados()
            else:
                print("Aluno não encontrado")

        elif opcao == 2:
            print("Informe o nome oficial do motorista:")
            nome_oficial = input()
            motorista_encontrado = None

            for motorista in objeto_motorista:
                if motorista.nome_oficial == nome_oficial:
                    motorista_encontrado = motorista
                    break

            if motorista_encontrado:
                motorista_encontrado.apresentar_dados()
            else:
                print("Motorista não encontrado")

        elif opcao == 3:
            print("Informe o nome da escola:")
            nome = input()
            escola_encontrada = None

            for escola in objeto_escola:
                if escola.nome == nome:
                    escola_encontrada = escola
                    break

            if escola_encontrada:
                escola_encontrada.apresentar_dados()
            else:
                print("Escola não encontrada")

        elif opcao == 4:
            print("Informe o nome do fornecedor:")
            nome_fantasia = input()
            fornecedor_encontrado = None

            for fornecedor in objeto_fornecedor:
                if fornecedor.nome_fantasia == nome_fantasia:
                    fornecedor_encontrado = fornecedor
                    break

            if fornecedor_encontrado:
                fornecedor_encontrado.apresentar_dados()
            else:
                print("Fornecedor não encontrado")


        else:
            print("Opção inválida")

        pass
    elif opcao == 12:
        # Lógica para a opção 12 - Exibir tipo da pessoa
        pass
    elif opcao == 13:
        print("Informe os dados do Fornecedor:")
            
        nome_fantasia = input("Nome Fantasia: ")
        num_funcionario = int(input("Número de Funcionários: "))
        nome_oficial = input("Nome Oficial: ")
        cpf_cnpj = input("CNPJ: ")
        
        print("Informe a rua:")
        rua = input()
            
        numero = trataNumero()
            
        print("Informe o complemento:")
        complemento = input()
            
        print("Informe o bairro:")
        bairro = input()

        endereco_forn = Endereco(rua,numero,complemento,bairro)
        objeto_endereco.append(endereco_forn)

        telefone = input("Telefone: ")
        fornecedor = Fornecedor(nome_fantasia, num_funcionario, nome_oficial, cpf_cnpj, endereco_forn, telefone)
        objeto_fornecedor.append(fornecedor)
        pass
    elif opcao == 14:
        print("Saindo do programa.")
    else:
        print("Opção inválida. Tente novamente.")