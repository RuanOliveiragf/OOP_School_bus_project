package exercicio_incremental_parte2;

import java.util.Arrays;
import java.util.Date;

public class Aluno extends PessoaFisica{
    /*private String rua;
    private int numero;
    private String complemento;
    private String bairro;
    */
    private Endereco endereco;
    private String telefone;
    private int matricula;
    private String serie;
    private Escola escola;
    private PontoDeParada pontoDeParada;

    public Aluno(int matricula, String serie, String nome, String mae, String pai, String naturalidade, Date data_nascimento, String nome_oficial, String cpf_cnpj, Endereco endereco, String telefone) {
        super(nome, mae, pai, naturalidade, data_nascimento, nome_oficial, cpf_cnpj, endereco, telefone);
        this.matricula = matricula;
        this.serie = serie;
        this.endereco = endereco;
    }

    /*
    public Aluno(String rua, int numero, String complemento, String bairro, String telefone, int matricula, String serie) {
        this.rua = rua;
        this.numero = numero;
        this.complemento = complemento;
        this.bairro = bairro;
        this.telefone = telefone;
        this.matricula = matricula;
        this.serie = serie;
    }
    
    */
    
    
    @Override
    public void apresentarDados() {
        super.apresentarDados();
        System.out.println(endereco.toString());
        System.out.println("Matrícula: " + getMatricula());
        System.out.println("Série: " + getSerie());
    }
    
    @Override
    public String verificarTipo() {
        String tipoSuperClasse = super.verificarTipo();
        return tipoSuperClasse + " Aluno";
    }

    public int getMatricula() {
        return matricula;
    }

    public void setMatricula(int matricula) {
        this.matricula = matricula;
    }

    public String getSerie() {
        return serie;
    }

    public void setSerie(String serie) {
        this.serie = serie;
    }
    
    
}
