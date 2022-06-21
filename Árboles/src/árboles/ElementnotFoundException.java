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
class ElementnotFoundException extends Exception {

    ElementnotFoundException(String árbol_vacio) {
        super("Elemento no encontrado."+árbol_vacio);
    }
    
}
