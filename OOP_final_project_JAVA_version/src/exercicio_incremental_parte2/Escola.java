package exercicio_incremental_parte2;

import java.util.ArrayList;
import java.util.Iterator;

public class Escola extends PessoaJuridica {
    private String nome;
    private ArrayList<Aluno> aluno;

    public Escola(String nome, String nome_fantasia, int num_funcionario, String nome_oficial, String cpf_cnpj, Endereco endereco, String telefone) {
        super(nome_fantasia, num_funcionario, nome_oficial, cpf_cnpj, endereco, telefone);
        this.nome = nome;
        this.aluno = new ArrayList<>();
        
    }

    @Override
public void apresentarDados() {
    super.apresentarDados(); 
    System.out.println("Nome: " + getNome());
    System.out.println("CNPJ: " + getCpf_cnpj());
    System.out.println("Telefone: " + getTelefone());
    System.out.println("Endereço: " + getEndereco());
    System.out.println("Alunos Matriculados: " + exibirAlunos());
}

 @Override
    public String verificarTipo() {
        String tipoSuperClasse = super.verificarTipo();
        return tipoSuperClasse + " Escola";
    }
    
    /*
    public Escola(String nome, String cnpj, String telefone) {
        this.nome = nome;
        this.cnpj = cnpj;
        this.telefone = telefone;
        this.aluno = new ArrayList<>();
    }
*/
    
    public String matricularAluno(Aluno aluno){
        this.aluno.add(aluno);
        return "Aluno matriculado com sucesso";
    }
    
    public String exibirAlunos(){
        String t = " ";
        for(Iterator<Aluno>it = aluno.iterator();it.hasNext();){
            Aluno x = it.next();
            t = t + " " + listarAlunos(x);
        }return t;
    }
    
    public String listarAlunos(Aluno aluno){
        return "\nMatricula: " + aluno.getMatricula()+" | nome social: "+ aluno.getNome_oficial()+" | serie: "+aluno.getSerie();
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    
}
