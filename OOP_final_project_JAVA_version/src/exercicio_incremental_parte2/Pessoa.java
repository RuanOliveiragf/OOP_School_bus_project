package exercicio_incremental_parte2;

public class Pessoa {
    protected String nome_oficial;
    protected String cpf_cnpj;
    protected Endereco endereco;
    protected String telefone;

    public Pessoa(String nome_oficial, String cpf_cnpj, Endereco endereco, String telefone) {
        this.nome_oficial = nome_oficial;
        this.cpf_cnpj = cpf_cnpj;
        this.endereco = endereco;
        this.telefone = telefone;
    }
    
    public Pessoa(String cpf_cnpj, Endereco endereco, String telefone) {
        this.cpf_cnpj = cpf_cnpj;
        this.endereco = endereco;
        this.telefone = telefone;
    }
    
    public void apresentarDados() {
        System.out.println("Nome: " + getNome_oficial());
        System.out.println("CPF/CNPJ: " + getCpf_cnpj());
        System.out.println("Endereço: " + getEndereco());
        System.out.println("Telefone: " + getTelefone());
    }
    
    public String verificarTipo() {
        return "Pessoa";
    }
    

    protected String getNome_oficial() {
        return nome_oficial;
    }

    public void setNome_oficial(String nome_oficial) {
        this.nome_oficial = nome_oficial;
    }

    protected String getCpf_cnpj() {
        return cpf_cnpj;
    }

    public void setCpf_cnpj(String cpf_cnpj) {
        this.cpf_cnpj = cpf_cnpj;
    }

    public Endereco getEndereco() {
        return endereco;
    }

    public void setEndereco(Endereco endereco) {
        this.endereco = endereco;
    }

    public String getTelefone() {
        return telefone;
    }

    public void setTelefone(String telefone) {
        this.telefone = telefone;
    }
    
    
    
}
