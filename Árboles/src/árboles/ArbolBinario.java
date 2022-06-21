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
public class ArbolBinario<T extends Comparable <T>>{
    private Nodo<T> raíz;
    private int cont;
    
    public ArbolBinario(){
        raíz=null;
        cont=0;
    }
    public ArbolBinario(T dato){
        raíz=new Nodo(dato);
        cont=1;
    }
    public void agrega(T dato){
        if(raíz==null){
            raíz=new Nodo(dato);
            return;
        }
        agrega(raíz,new Nodo(dato));
        cont++;
    } 
    private void agrega(Nodo<T> actual,Nodo<T> dato){
        if(actual.getDato().compareTo(dato.getDato())>0){
            if(actual.getIzquierdo()==null){
                actual.setIzq(dato);
                return;
            }
            agrega(actual.getIzquierdo(),dato);
        }else{
           if(actual.getDerecho()==null){
               actual.setDer(dato);
               return;
           } 
           agrega(actual.getDerecho(),dato);
        }
    }
    public void imprimirPreOrder(){
        imprimir(raíz);
    }
    private void imprimir(Nodo<T> tmp){
        System.out.print(tmp.toString());
        if(tmp.getIzquierdo()!=null)
            imprimir(tmp.getIzquierdo());
        if(tmp.getDerecho()!=null)
            imprimir(tmp.getDerecho());
    }
    public void imprimirPostOrder(){
        imprimirPost(raíz);
    }
    private void imprimirPost(Nodo<T> tmp){
        if(tmp.getIzquierdo()!=null)
            imprimirPost(tmp.getIzquierdo());
        if(tmp.getDerecho()!=null)
            imprimirPost(tmp.getDerecho());
        System.out.print(tmp.toString());
    }
    public void imprimirInOrder(){
        imprimirEnOrden(raíz);
    }
    private void imprimirEnOrden(Nodo<T> tmp){
        if(tmp.getIzquierdo()!=null)
            imprimirEnOrden(tmp.getIzquierdo());
        System.out.print(tmp.toString());
        if(tmp.getDerecho()!=null)
            imprimirEnOrden(tmp.getDerecho());
    }
    public void imprimirConNivel(){
        imprimirConNivel(raíz,1);
        System.out.println();
    }
    private void imprimirConNivel(Nodo<T> tmp,int nivel){
        if(tmp!=null){
            imprimirConNivel(tmp.getIzquierdo(),nivel+1);
            System.out.println(tmp.getDato().toString()+"("+nivel+")");
            imprimirConNivel(tmp.getDerecho(),nivel+1);
        }
    }
    public void elimina (T dato) throws EmptyCollectionException{
        Nodo<T> actual,papá;
        if(raíz==null)
            throw new EmptyCollectionException("árbol vacío");
        actual=raíz;
        papá=actual;
        while(actual!=null&&actual.getDato().compareTo(dato)!=0){
            papá=actual;
            if(dato.compareTo(actual.getDato())<= 0)
                actual=actual.getIzquierdo();
            else actual=actual.getDerecho();
        }
        //PRIMER CASO --> Nodo hoja
        if(actual.getIzquierdo()==null&&actual.getDerecho()==null){
            if(actual == raíz)
                raíz=null;
            else{
                if(papá.getIzquierdo()== actual)
                    papá.setIzq(null);
                else papá.setDer(null);
            }
            cont--;
            return;
        }
        //SEGUNDO CASO --> solo tiene un hijo
        if(actual.getDerecho()==null){
            if(actual==raíz)
                raíz=actual.getIzquierdo();
            else papá.cuelga(actual.getIzquierdo());
            cont--;
            return;
        }
        //TERCER CASO --> tiene hijos de los dos lados
        if(actual.getIzquierdo()!=null&&actual.getDerecho()!=null){
            Nodo<T> sucInOrd,papá2;
            sucInOrd=actual.getDerecho();
            papá2=sucInOrd;
            while(sucInOrd.getIzquierdo()!=null){
                papá2=sucInOrd;
                sucInOrd=sucInOrd.getIzquierdo();
            }
            actual.setDato(sucInOrd.getDato());
            if(papá2!=sucInOrd)
                papá2.setIzq(sucInOrd.getDerecho());
            else actual.setDer(sucInOrd.getDerecho());
            cont--;
        }  
    }
    public int getAltura(){
        return getAltura(raíz,0,0);
    }
    private int getAltura(Nodo<T> actual,int contDer,int contIzq){
        if(actual==null)
            return 0;
        contDer=1+getAltura(actual.getDerecho(),contDer,contIzq);
        contIzq=1+getAltura(actual.getIzquierdo(),contDer,contIzq);
        return Math.max(contDer,contIzq);
    }
}
