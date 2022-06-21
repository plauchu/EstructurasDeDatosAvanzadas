/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package árboles;

/**
 *
 * @author Plauchu
 */
public class Nodo<T extends Comparable <T>>{
    private Nodo<T> izq,der;
    private T dato;
    
    public Nodo(){
        dato=null;
        izq=der=null;
    }
    public Nodo(T dato){
        this.dato=dato;
        izq=der=null;
    }
    public T getDato(){
        return dato;
    }
    public void setDato(T dato){
        this.dato=dato;
    }
    public Nodo<T> getIzquierdo(){
        return izq;
    }
    public void setIzq(Nodo<T> izquierda){
        this.izq=izquierda;
    }
    
    public Nodo<T> getDerecho(){
        return der;
    }
    public void setDer(Nodo<T> derecha){
        this.der=derecha;
    }
    @Override
    public String toString(){
        return dato.toString()+"\n";
    }
    public void cuelga(Nodo<T> N){
        if(N==null)
            return;
        if(N.getDato().compareTo(dato)<=0)
            izq=N;
    }
}
