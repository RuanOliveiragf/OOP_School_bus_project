package exercicio_incremental_parte2;

import java.util.ArrayList;

public class Fonecedor extends PessoaJuridica {
    private ArrayList<Contrato>contratos;

    public Fonecedor(String nome_fantasia, int num_funcionario, String nome_oficial, String cpf_cnpj, Endereco endereco, String telefone) {
        super(nome_fantasia, num_funcionario, nome_oficial, cpf_cnpj, endereco, telefone);
        this.contratos = contratos;
        this.contratos = new ArrayList<>();
    }

    public ArrayList<Contrato> getContratos() {
        return contratos;
    }

    public void setContratos(ArrayList<Contrato> contratos) {
        this.contratos = contratos;
    }
    
    @Override
    public String verificarTipo() {
        String tipoSuperClasse = super.verificarTipo(); 
        return tipoSuperClasse + " Fornecedor";
    }
    
    
    
}
