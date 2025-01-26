package exercicio_incremental_parte2;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Date;
import java.util.Iterator;
import java.util.Scanner;

public class Aplicacao {
    private static ArrayList<Aluno>objeto_aluno = new ArrayList<>();
    private static ArrayList<Escola>objeto_escola = new ArrayList<>();
    private static ArrayList<Motorista>objeto_motorista = new ArrayList<>();
    private static ArrayList<Contrato>objeto_contrato = new ArrayList<>();
    private static ArrayList<Veiculo>objeto_veiculo = new ArrayList<>();
    private static ArrayList<PontoDeParada>objeto_ponto = new ArrayList<>();
    private static ArrayList<Rota>objeto_rota = new ArrayList<>();
    private static ArrayList<Endereco>objeto_endereco = new ArrayList<>();
    private static ArrayList<Fonecedor>objeto_fornecedor = new ArrayList<>();
    
    public static void main(String[] args) throws ParseException {
        int opcao;  
        String nome_oficial;
        String nome;
        String mae;
        String pai;
        String naturalidade;
        //String cpf;
        Date data_nascimento;
        String rua;
        int numero;
        String complemento;
        String bairro;
        String telefone;
        int matricula;
        String serie;
        
        //-------------------------------------------------------//
        String cnpj;
        //-------------------------------------------------------//
        Escola escola;
        PontoDeParada pontoDeParada;
        String nome_fantasia;
        int num_funcionario;
        //-------------------------------------------------------//
        int tipo, num_contrato;
        String nome_social, num_habilitacao, cat_habilitacao, cpf_cnpj;
        //-------------------------------------------------------//
        Date data_inicio, data_fim;
        double valor;
        //-------------------------------------------------------//
        String placa, modelo;
        int ano, capacidade;
        //-------------------------------------------------------//
        double latitude, longitude;
        //-------------------------------------------------------//
        int id;
        Scanner s1 = new Scanner(System.in);
        SimpleDateFormat dateFormat = new SimpleDateFormat("dd/MM/yyyy");
        
        do{
            
            System.out.println("1 - Criar aluno");
            System.out.println("2 - Criar motorista");
            System.out.println("3 - Criar contrato");
            System.out.println("4 - Criar escola");
            System.out.println("5 - Criar veiculo");
            System.out.println("6 - Criar ponto de parada");
            System.out.println("7 - Criar uma nova rota, adicionando pontos de parada a ela");
            System.out.println("8 - Calcular a demanda de uma rota específica");
            System.out.println("9 - Exibir o número total de rotas criadas.");
            System.out.println("10 - Exibir o número total de pontos de parada criados.");
            System.out.println("11 - Exibir informações de um Aluno, Motorista, Escola ou Fornecedor");
            System.out.println("12 - Exibir o tipo da pessoa.");
            System.out.println("13 - Sair do programa.");
            System.out.print("Escolha uma das opções acima: ");
            opcao = s1.nextInt();
            s1.nextLine();
            System.out.println(opcao);
  
            switch(opcao){
            case 1:
                if(objeto_escola.isEmpty()){
                    System.out.println("Nao ha escolas, por favor criar uma escolhendo a opcao 4");
                }else{
                    System.out.print("Informe o nome civil do aluno: ");
                    nome_oficial = s1.next();
                    
                    System.out.print("Informe o nome do aluno: ");
                    nome = s1.next();
                    
                    System.out.print("Informe o nome da mae: ");
                    mae = s1.next();
                    
                    System.out.print("Informe o nome do pai: ");
                    pai = s1.next();
                    
                    System.out.print("Informe a naturalidade: ");
                    naturalidade = s1.next();
                    
                    System.out.print("Informe o cpf: ");
                    cpf_cnpj = s1.next();
                    
                    System.out.print("Informe a data de nascimento: ");
                    String dataNascimentoStr = s1.next();
                    data_nascimento = dateFormat.parse(dataNascimentoStr);
                    //System.out.println(data_nascimento);
                    
                    System.out.print("Informe a rua: ");
                    rua = s1.next();
                    
                    System.out.print("Informe o numero: ");
                    numero = s1.nextInt();
                    s1.nextLine();
                    
                    System.out.print("Informe o complemento: ");
                    complemento = s1.next();
                    
                    System.out.print("Informe o bairro: ");
                    bairro = s1.next();
                    
                    Endereco e = new Endereco(rua,numero,complemento,bairro);
                    
                    objeto_endereco.add(e);
                    
                    System.out.print("Informe o telefone: ");
                    telefone = s1.next();
                    
                    System.out.print("Informe a matricula: ");
                    matricula = s1.nextInt();
                    s1.nextLine();
                    
                    System.out.print("Informe a serie: ");
                    serie = s1.next();
                    
                    Aluno x = new Aluno(matricula,serie,nome,mae,pai,naturalidade,data_nascimento,nome_oficial,cpf_cnpj,e,telefone);
                    objeto_aluno.add(x);
                }      
                
                break;
                
            case 2:
                System.out.print("Informe se o motorista é terceirizado (digite 1) ou se ele é servidor (digite 0): ");
                tipo = s1.nextInt();
                s1.nextLine();
                
                if(tipo == 1){
                    if(objeto_contrato.isEmpty()){
                        System.out.println("Não há contratos para vincular o motorista, por favor criar contrato utilizando a opcao 3");
                    }else{
                        System.out.print("Nome civil: ");
                        nome_oficial = s1.nextLine();
                        
                    System.out.print("Deseja informar nome social [1] SIM [2] NAO");
                    opcao = s1.nextInt();
                    s1.nextLine();
                    
                    if (opcao == 1){
                        System.out.print("Informe o nome social: ");
                        nome = s1.nextLine();
                    }else{
                        nome = nome_oficial;
                    }

                    System.out.print("Nome da mãe: ");
                    mae = s1.nextLine();
                                            
                    System.out.print("Nome do pai: ");
                    pai = s1.nextLine();
                                            
                    System.out.print("Naturalidade: ");
                    naturalidade = s1.next();

                    System.out.print("CPF/CNPJ: ");
                    cpf_cnpj = s1.next();

                    System.out.print("Data de nascimento: ");
                    String dataNascimentoStr = s1.next();
                    data_nascimento = dateFormat.parse(dataNascimentoStr);

                    System.out.print("Rua: ");
                    rua = s1.next();

                    System.out.print("Número da casa: ");
                    numero = s1.nextInt(); 

                    System.out.print("Complemento: ");
                    complemento = s1.next();

                    System.out.print("Bairro: ");
                    bairro = s1.next();
                    
                    Endereco e = new Endereco(rua, numero, complemento, bairro);
                    objeto_endereco.add(e);
                    
                    System.out.print("Telefone: ");
                    telefone = s1.next();

                    System.out.print("Número de habilitação: ");
                    num_habilitacao = s1.next();

                    System.out.print("Categoria de habilitação: ");
                    cat_habilitacao = s1.next();

                    System.out.println("Tipo: teceirizado");

                    System.out.print("Número de contrato: ");
                    num_contrato = s1.nextInt();
                    
                
                    Motorista z = new Motorista(num_habilitacao,cat_habilitacao,tipo, num_contrato,nome, mae, pai, naturalidade, data_nascimento, nome_oficial, cpf_cnpj,e,telefone);
                    }
                    
                }else if(tipo == 0){
                    
                    System.out.print("Nome civil: ");
                    nome_oficial = s1.next();

                    System.out.print("Deseja informar nome social [1] SIM [2] NAO");
                    opcao = s1.nextInt();
                    
                    if (opcao == 1){
                        System.out.print("Informe o nome social: ");
                        nome = s1.next();
                    }else{
                        nome = nome_oficial;
                    }

                    System.out.print("Nome da mãe: ");
                    mae = s1.next();

                    System.out.print("Nome do pai: ");
                    pai = s1.next();

                    System.out.print("Naturalidade: ");
                    naturalidade = s1.next();

                    System.out.print("CPF/CNPJ: ");
                    cpf_cnpj = s1.next();

                    System.out.print("Data de nascimento: ");
                    String dataNascimentoStr = s1.next();
                    data_nascimento = dateFormat.parse(dataNascimentoStr);

                    System.out.print("Rua: ");
                    rua = s1.next();

                    System.out.print("Número da casa: ");
                    numero = s1.nextInt(); 

                    System.out.print("Complemento: ");
                    complemento = s1.next();

                    System.out.print("Bairro: ");
                    bairro = s1.next();
                    
                    Endereco e = new Endereco(rua, numero, complemento, bairro);
                    objeto_endereco.add(e);

                    System.out.print("Telefone: ");
                    telefone = s1.next();

                    System.out.print("Número de habilitação: ");
                    num_habilitacao = s1.next();

                    System.out.print("Categoria de habilitação: ");
                    cat_habilitacao = s1.next();

                    System.out.print("Tipo: servidor");
           
                    Motorista z = new Motorista(num_habilitacao,cat_habilitacao,tipo,nome, mae, pai, naturalidade, data_nascimento, nome_oficial, cpf_cnpj,e,telefone);
                }else{
                    System.out.println("opcao invalida");
                }
                break;
            case 3: 
                System.out.println("Para criar um contrato informe os dados solicitados abaixo: ");
                
                System.out.print("Número do contrato: ");
                num_contrato = s1.nextInt();
                s1.nextLine();
                
                
                System.out.print("Data de início do contrato (dd/MM/yyyy): ");
                String dataInicioStr = s1.next();
                data_inicio = dateFormat.parse(dataInicioStr);
                
                System.out.print("Data de término do contrato (dd/MM/yyyy): ");
                String dataFimStr = s1.next();
                data_fim = dateFormat.parse(dataFimStr);
             
                System.out.print("Valor do contrato: ");
                valor = s1.nextDouble();

                Contrato c = new Contrato(num_contrato, data_inicio, data_fim, valor);
                objeto_contrato.add(c);
                
                break;
                
            case 4:
                System.out.println("Para criar uma escola informe os seguintes dados: ");
                
                System.out.println("Informe o nome da escola: ");
                nome = s1.next();
                
                System.out.println("Informe o nome fantasia: ");
                nome_fantasia = s1.nextLine();
                s1.nextLine(); 
                
                System.out.println("Informe o numero de funcionarios: ");
                num_funcionario = s1.nextInt();
                s1.nextLine();
                
                System.out.println("Informe o cnpj: ");
                cpf_cnpj = s1.next();
                
                System.out.println("Informe o telefone: ");
                telefone = s1.next();
                
                System.out.print("Rua: ");
                rua = s1.next();

                System.out.print("Número da casa: ");
                numero = s1.nextInt(); 

                System.out.print("Complemento: ");
                complemento = s1.next();

                System.out.print("Bairro: ");
                bairro = s1.next();
                    
                nome_oficial = "";
                
                Endereco es = new Endereco(rua, numero, complemento, bairro);
                objeto_endereco.add(es);
                
                Escola y = new Escola(nome, nome_fantasia, num_funcionario, nome_oficial ,cpf_cnpj, es, telefone);
                objeto_escola.add(y);
                //System.out.println(objeto_escola.get(0));
                break;
                
            case 5:
                System.out.println("Informe se o veiculo é próprio (digite 0) ou alugado (digite 1): ");
                tipo = s1.nextInt();
                if(tipo == 1){
                    if(objeto_contrato == null){
                        
                        System.out.println("Nao ha contratos para associar o veiculo, por favor criar um contrato selecionando a opcao 3");
                    
                    }else{
                        
                        System.out.print("Placa do veículo: ");
                        placa = s1.next();

                        System.out.print("Ano do veículo: ");
                        ano = s1.nextInt();

                        System.out.print("Modelo do veículo: ");
                        modelo = s1.next();

                        System.out.print("Capacidade do veículo: ");
                        capacidade = s1.nextInt();

                        System.out.print("Tipo do veículo: alugado");

                        System.out.print("Número do contrato: ");
                        num_contrato = s1.nextInt();
                        
                        Veiculo v = new Veiculo(placa, ano, modelo, capacidade, tipo, num_contrato);
                        objeto_veiculo.add(v);

                    }
                    
                }else if(tipo == 0){
                    System.out.print("Placa do veículo: ");
                    placa = s1.next();

                    System.out.print("Ano do veículo: ");
                    ano = s1.nextInt();

                    System.out.print("Modelo do veículo: ");
                    modelo = s1.next();

                    System.out.print("Capacidade do veículo: ");
                    capacidade = s1.nextInt();

                    System.out.print("Tipo do veículo: alugado");
                    
                    Veiculo v = new Veiculo(placa, ano, modelo, capacidade, tipo);
                    objeto_veiculo.add(v);
                    
                }else{
                    System.out.println("opcao invalida!");
                }
                break;
                
            case 6:
                System.out.println("Para criar um ponto de parada insira as guintes informações");
                
                System.out.print("Informe o nome do ponto: ");
                nome = s1.nextLine();
                
                System.out.print("informe a latitude: ");
                latitude = s1.nextDouble();
                s1.nextLine();
                
                System.out.print("Informe a longitude: ");
                longitude = s1.nextDouble();
                s1.nextLine();
                
                PontoDeParada p = new PontoDeParada(nome, latitude, longitude);
                objeto_ponto.add(p);
                break;
                
            case 7:
                Rota r = new Rota();
                objeto_rota.add(r);
                
                System.out.println("---Informe os pontos de parada da rota---");
                System.out.println("Deseja informar um ponto? [1]SIM [0]NAO");
                opcao = s1.nextInt();
                s1.nextLine();
                
                while(opcao == 1){
                    System.out.println("Informe o id do ponto que deseja adicionar: ");
                    id = s1.nextInt();
                    s1.nextLine();
                    
                    PontoDeParada pontoEscolhido = null;
                    
                    for(PontoDeParada m : objeto_ponto){
                        
                        if(m.getId() == id){
                            pontoEscolhido = m;
                            break;
                        }
                    }
                    
                    if(pontoEscolhido != null){
                        r.adicionaPonto(pontoEscolhido);
                        System.out.println("Ponto adicionado com sucesso. Deseja adicionar outro ponto? [1] SIM [0] NÃO");
                        opcao = s1.nextInt();
                        s1.nextLine();
                    }else {
                        System.out.println("Ponto não encontrado. Deseja informar outro ponto? [1] SIM [0] NÃO");
                        opcao = s1.nextInt();
                        s1.nextLine();
                    }
                }
                
                break;    
            case 8:
                System.out.print("Informe o id da rota: ");
                id = s1.nextInt();
                
                for(Iterator<Rota>it = objeto_rota.iterator();it.hasNext();){
                    Rota x = it.next();
                    if(x.getId() == id){
                        System.out.println("A demanda da rota é: " + x.calculaDemanda());
                    }else{
                        System.out.println("Rota nao encontrada");
                    }
                }
                break;
            case 9:
                if(objeto_rota.isEmpty()){
                    System.out.println("Nao ha rotas criadas, selecionar a opcao 7");
                }else{
                    System.out.println("Numero total de rotas: " + objeto_rota.size());
                }
                break;
                
            case 10:
                if(objeto_ponto.isEmpty()){
                    System.out.println("Não há pontos de parada criados");
                }else{
                    System.out.println("Numero de pontos de parada criados: " + objeto_ponto.size());
                }
                break;
            case 11:
                System.out.println("informe que informação deseja obter: ");
                System.out.println("[1] - Aluno");
                System.out.println("[2] - Motorista");
                System.out.println("[3] - Escola");
                System.out.println("[4] - Fornecedor");
                opcao = s1.nextInt();
                s1.nextLine();
                
                if(opcao == 1){
                    System.out.println("Informe o nome oficial do Aluno: ");
                    nome_oficial = s1.nextLine();
                    for(int i = 0; i<objeto_aluno.size();i++){
                        Aluno x = objeto_aluno.get(i);
                        if(x.getNome_oficial() == nome_oficial){
                            System.out.println(x.toString());
                            break;
                        }
                    }
                }else if(opcao == 2){
                    System.out.println("Informe o nome oficial do motorista: ");
                    nome_oficial = s1.nextLine();
                    for(int i = 0; i <objeto_motorista.size();i++){
                        Motorista x = objeto_motorista.get(i);
                        if(x.getNome_oficial() == nome_oficial){
                            System.out.println(x.toString());
                            break;
                        }
                    }
                }else if(opcao == 3){
                    System.out.println("Informe o nome da escola: ");
                    nome = s1.nextLine();
                    for(int i = 0; i <objeto_escola.size();i++){
                        Escola x = objeto_escola.get(i);
                        if(x.getNome() == nome){
                            System.out.println(x.toString());
                            break;
                        }
                    }
                }else if(opcao == 4){
                    System.out.println("Insira o nome do fornecedor: ");
                    nome_fantasia = s1.nextLine();
                    for(int i = 0; i <objeto_fornecedor.size();i++){
                        Fonecedor x = objeto_fornecedor.get(i);
                        if(x.getNome_fantasia()== nome_fantasia){
                            System.out.println(x.toString());
                            break;
                        }
                    }
                }
                break;
                
            case 12:
                
                break;
        }
        }while(opcao != 13);
    }
}
