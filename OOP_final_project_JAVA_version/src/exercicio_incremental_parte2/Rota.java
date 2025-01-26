package exercicio_incremental_parte2;

import java.util.ArrayList;
import java.util.Iterator;

public class Rota {
    private ArrayList<PontoDeParada> pontos;
    private int id;
    private static int total_rotas = 0;

    public Rota() {
        this.pontos = new ArrayList();
        total_rotas++;
        this.id = total_rotas;
    }
    
    public void adicionaPonto(PontoDeParada p){
        pontos.add(p);
    }
    
    public int calculaDemanda(){
        int demanda = 0;
        for(Iterator<PontoDeParada>it = pontos.iterator();it.hasNext();){
            PontoDeParada x = it.next();
            demanda = demanda + x.getAlunos().size();
        }return demanda;
    }
    
    public static int numero_rotas(){
        return total_rotas;
    }
    
    
    public ArrayList<PontoDeParada> getPontos() {
        return pontos;
    }

    public void setPontos(ArrayList<PontoDeParada> pontos) {
        this.pontos = pontos;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    void setPontos(PontoDeParada m) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
    
    
}
