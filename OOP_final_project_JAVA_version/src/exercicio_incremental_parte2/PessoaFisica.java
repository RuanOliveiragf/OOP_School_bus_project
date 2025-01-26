package exercicio_incremental_parte2;

import java.util.Date;

public class PessoaFisica extends Pessoa {
   private String nome;
   private String mae;
   private String pai;
   private String naturalidade;
   private Date data_nascimento;

    public PessoaFisica(String nome, String mae, String pai, String naturalidade, Date data_nascimento, String nome_oficial, String cpf_cnpj, Endereco endereco, String telefone) {
        super(nome_oficial, cpf_cnpj, endereco, telefone);
        this.nome = nome;
        this.mae = mae;
        this.pai = pai;
        this.naturalidade = naturalidade;
        this.data_nascimento = data_nascimento;
    }
    
    public String getCPF(){
        return cpf_cnpj;
    }
   
   public String getNomeOficial(){
       return nome_oficial;
   }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getMae() {
        return mae;
    }

    public void setMae(String mae) {
        this.mae = mae;
    }

    public String getPai() {
        return pai;
    }

    public void setPai(String pai) {
        this.pai = pai;
    }

    public String getNaturalidade() {
        return naturalidade;
    }

    public void setNaturalidade(String naturalidade) {
        this.naturalidade = naturalidade;
    }

    public Date getData_nascimento() {
        return data_nascimento;
    }

    public void setData_nascimento(Date data_nascimento) {
        this.data_nascimento = data_nascimento;
    }
   
   
}
