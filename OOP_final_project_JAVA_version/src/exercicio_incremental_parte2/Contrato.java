package exercicio_incremental_parte2;
import java.util.ArrayList;
import java.util.Date;
import java.util.Iterator;

public class Contrato {
    private int num_contrato;
    private Date data_inicio;
    private Date data_fim;
    private double valor;
    //private Motorista motorista;
    private ArrayList<Motorista> motorista;
    //private Veiculo veiculo;
    private ArrayList<Veiculo> veiculo;
    private ArrayList<Fonecedor>fornecedor;
    

    public Contrato(int num_contrato, Date data_inicio, Date data_fim, double valor) {
        this.num_contrato = num_contrato;
        this.data_inicio = data_inicio;
        this.data_fim = data_fim;
        this.valor = valor;
        this.veiculo = new ArrayList<>();
        this.motorista = new ArrayList<>();
    }
    
    //metodo para adicionar veiculo
    public String alteraVeiculo(Veiculo veiculo) {
        if(veiculo.getTipo()==1){
            this.veiculo.add(veiculo);
            return "veiculo adicionado com succeso";
        }else{
            return "veiculo proprio nao pode ser adicionado";
        }
        
    }
    //metodo para remover veiculo
    public String alteraVeiculo(String placa){
        for(Iterator<Veiculo>it = veiculo.iterator(); it.hasNext();){
            Veiculo x = it.next();
            if(x.getPlaca()==placa){
                this.veiculo.remove(x);
                return "Veiculo removido com sucesso";                
            }else{
                return "Veiculo nao consta no contrato para ser removido";
            }
        }
        return "";
    }
    
    public void adicionaFornecedor(Fonecedor fornecedor){
        this.fornecedor.add(fornecedor);
    }
    
    public String alteraMotorista(Motorista motorista) {
        if(motorista.getTipo()==1){
            this.motorista.add(motorista);
            return "motorista adicionado com succeso";
        }else{
            return "motorista servidor nao pode ser adicionado";
        }
        
    }
    
    public String alteraMotorista(String cpf_cnpj){
        for(Iterator<Motorista>it = motorista.iterator(); it.hasNext();){
            Motorista x = it.next();
            if(x.getCpf_cnpj()==cpf_cnpj){
                this.motorista.remove(x);
                return "Motorista removido com sucesso";                
            }else{
                return "Motorista nao consta no contrato para ser removido";
            }
        }
        return "";
    }

    public int getNum_contrato() {
        return num_contrato;
    }

    public void setNum_contrato(int num_contrato) {
        this.num_contrato = num_contrato;
    }

    public Date getData_inicio() {
        return data_inicio;
    }

    public void setData_inicio(Date data_inicio) {
        this.data_inicio = data_inicio;
    }

    public Date getData_fim() {
        return data_fim;
    }

    public void setData_fim(Date data_fim) {
        this.data_fim = data_fim;
    }

    public double getValor() {
        return valor;
    }

    public void setValor(double valor) {
        this.valor = valor;
    }
    
    
}
