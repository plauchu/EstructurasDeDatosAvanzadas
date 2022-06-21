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
public class Árboles {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        ArbolBinario<Integer> ab=new ArbolBinario(10);
        ab.agrega(9);
        ab.agrega(15);
        ab.agrega(7);
        ab.agrega(14);
        ab.agrega(17);
        ab.agrega(5);
        ab.agrega(8);
        ab.agrega(11);
        ab.agrega(16);
        ab.agrega(20);
        ab.agrega(3);
        ab.agrega(6);
        ab.agrega(12);
        ab.agrega(19);
        ab.agrega(22);
        ab.agrega(1);
        ab.agrega(4);
        ab.agrega(13);
        ab.agrega(18);
        ab.agrega(21);
        ab.agrega(24);
        ab.agrega(0);
        ab.agrega(2);
        ab.agrega(23);
        ab.agrega(25);
        
//        System.out.println("Pre:");
//        ab.imprimirPreOrder();
        //System.out.println();
        //ab.elimina(2);
        //ab.imprimirInOrder();
        ab.imprimirConNivel();
//        System.out.println("Post:");
//        ab.imprimirPostOrder();
        System.out.println(ab.getAltura());
    }
    
}
