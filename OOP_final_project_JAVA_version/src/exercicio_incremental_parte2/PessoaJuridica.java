package exercicio_incremental_parte2;

public class PessoaJuridica extends Pessoa {
    private String nome_fantasia;
    private int num_funcionario;

    public PessoaJuridica(String nome_fantasia, int num_funcionario, String nome_oficial, String cpf_cnpj, Endereco endereco, String telefone) {
        super(nome_oficial, cpf_cnpj, endereco, telefone);
        this.nome_fantasia = nome_fantasia;
        this.num_funcionario = num_funcionario;
    }

    public String getCNPJ(){
        return cpf_cnpj;
    }
    
    public String getNome_fantasia() {
        return nome_fantasia;
    }

    public void setNome_fantasia(String nome_fantasia) {
        this.nome_fantasia = nome_fantasia;
    }

    public int getNome_funcionario() {
        return num_funcionario;
    }

    public void setNome_funcionario(int num_funcionario) {
        this.num_funcionario = num_funcionario;
    }
    
    
}
