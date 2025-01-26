package exercicio_incremental_parte2;

import java.util.Iterator;

public class Veiculo {
    private String placa;
    private int ano;
    private String modelo;
    private int capacidade;
    private int tipo;
    private int num_contrato;
    private Contrato contrato;

    public Veiculo(String placa, int ano, String modelo, int capacidade, int tipo, int num_contrato) {
        this.placa = placa;
        this.ano = ano;
        this.modelo = modelo;
        this.capacidade = capacidade;
        this.tipo = tipo;
        this.num_contrato = num_contrato;
        //exigeContrato();
    }

    public Veiculo(String placa, int ano, String modelo, int capacidade, int tipo) {
        this.placa = placa;
        this.ano = ano;
        this.modelo = modelo;
        this.capacidade = capacidade;
        this.tipo = tipo;
        exigeContrato();
    }
    
    public void exigeContrato(){
        if(this.getTipo()==1 && this.getNum_contrato()==0){
            System.out.println("insira o numero do contrato");
        }else{
            this.num_contrato = num_contrato;
        }
    }
    
    public void verificaVeiculo(){
     if(this.getTipo() == 0){
        String t = "o veiculo é proprio";
        System.out.println(t);
         //return t;
     }else{
        String t = "o veiculo é alugado";
        System.out.println(t);
        //return t;
     }
    }
    
    public String getPlaca() {
        return placa;
    }

    public void setPlaca(String placa) {
        this.placa = placa;
    }

    public int getAnod() {
        return ano;
    }

    public void setAno(int ano) {
        this.ano = ano;
    }

    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public int getCapacidade() {
        return capacidade;
    }

    public void setCapacidade(int capacidade) {
        this.capacidade = capacidade;
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
            System.out.println("Nao se pode colocar numero de contrato pois o veiculo é próprio");
        }else{
            this.num_contrato = num_contrato;
        }     
    }
    
    //public void teste(){
       // this.setNum_contrato(4);
    //}

    Iterator<Veiculo> iterator() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    void remove(Veiculo veiculo) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    void add(Veiculo veiculo) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
}
