package exercicio_incremental_parte2;

import java.util.ArrayList;
import java.util.Date;
import java.util.Iterator;

public class Motorista extends PessoaFisica {
    /*private String rua;
    private int numero;
    private String complemento;
    private String bairro;*/   
    private String num_habilitacao;
    private String cat_habilitacao;
    private int tipo;
    private int num_contrato;
    private ArrayList<Contrato> contratos;

    public Motorista(String num_habilitacao,String cat_habilitacao, int tipo, int num_contrato, String nome, String mae, String pai, String naturalidade, Date data_nascimento, String nome_oficial, String cpf_cnpj, Endereco endereco, String telefone) {
        super(nome, mae, pai, naturalidade, data_nascimento, nome_oficial, cpf_cnpj, endereco, telefone);
        this.num_habilitacao = num_habilitacao;
        this.cat_habilitacao = cat_habilitacao;
        this.tipo = tipo;
        this.num_contrato = num_contrato;
        this.contratos = contratos;
        this.endereco = endereco;
        this.contratos = new ArrayList<>();
    }

    public Motorista(String num_habilitacao, String cat_habilitacao, int tipo, String nome, String mae, String pai, String naturalidade, Date data_nascimento, String nome_oficial, String cpf_cnpj, Endereco endereco, String telefone) {
        super(nome, mae, pai, naturalidade, data_nascimento, nome_oficial, cpf_cnpj, endereco, telefone);
        this.num_habilitacao = num_habilitacao;
        this.cat_habilitacao = cat_habilitacao;
        this.tipo = tipo;
        this.contratos = contratos;
        this.contratos = new ArrayList<>();
    }   
    
    
/*
    public Motorista(String rua, int numero, String complemento, String bairro, String num_habilitacao, String cat_habilitacao, int tipo, int num_contrato) {
        this.rua = rua;
        this.numero = numero;
        this.complemento = complemento;
        this.bairro = bairro;
        this.telefone = telefone;
        this.num_habilitacao = num_habilitacao;
        this.cat_habilitacao = cat_habilitacao;
        this.tipo = tipo;
        this.num_contrato = num_contrato;
        this.contratos = new ArrayList<>();
        //exigeContrato();
    }
*/
    
    /*
    public Motorista(String nome_civil, String nome, String mae, String pai, String naturalidade, String cpf_cnpj, Date data_nascimento, String rua, int numero, String complemento, String bairro,String num_habilitacao, String cat_habilitacao, int tipo) {
        this.rua = rua;
        this.numero = numero;
        this.complemento = complemento;
        this.bairro = bairro;
        this.telefone = telefone;
        this.num_habilitacao = num_habilitacao;
        this.cat_habilitacao = cat_habilitacao;
        this.tipo = tipo;
        this.contratos = new ArrayList<>();
        exigeContrato();
    }

*/
    @Override
    public void apresentarDados() {
        super.apresentarDados(); // Chama o método da classe pai para exibir os atributos comuns
        System.out.println(endereco.toString());
        System.out.println("Número de Habilitação: " + getNum_habilitacao());
        System.out.println("Categoria de Habilitação: " + getCat_habilitacao());
        System.out.println("Tipo: " + (getTipo() == 0 ? "Servidor Público" : "Terceirizado"));
        if(getTipo() == 1){
            System.out.println("Número de Contrato: " + getNum_contrato());
        }
        
    }
    
     @Override
    public String verificarTipo() {
        String tipoSuperClasse = super.verificarTipo();
        return tipoSuperClasse + " Motorista";
    }
    
    public String adicionaContrato(Contrato contratos){
        if(this.getTipo()==1 && this.getNum_contrato()!=0){
            this.contratos.add(contratos);
            return "contrato adicionado";
        }else if(this.getTipo()==1 && this.getNum_contrato()==0){
            return "motorista terceirizado sem numero de contrato informado, impossivel adicionar";
        }else{
            return "o motorista é do tipo servidor publico, nao é possivel associa-lo a um contrato";
        }
    }
    
    public void exigeContrato(){
        if(this.getTipo()==1 && this.getNum_contrato()==0){
            System.out.println("insira o numero do contrato");
        }else{
            this.num_contrato = num_contrato;
        }
    }
    
    
    public String verificaMotorista(){
        if(this.getTipo()==0){
            String t = "o motorista é servidor";
            return t;
        }else{
            String t = "o motorisra é terceirizado";
            return t;
        }
    }

    public String getNum_habilitacao() {
        return num_habilitacao;
    }

    public void setNum_habilitacao(String num_habilitacao) {
        this.num_habilitacao = num_habilitacao;
    }

    public String getCat_habilitacao() {
        return cat_habilitacao;
    }

    public void setCat_habilitacao(String cat_habilitacao) {
        this.cat_habilitacao = cat_habilitacao;
    }

    public int getTipo() {
        return tipo;
    }

    public void setTipo(int tipo) {
        this.tipo = tipo;
    }

    public int getNum_contrato() {
        return num_contrato;
    }

    public void setNum_contrato(int num_contrato) {
       if(this.getTipo()==0){
           System.out.println("Método inválido");
       }else{
           this.num_contrato = num_contrato;
       }     
    }

    void add(Motorista motorista) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
    
    
}
