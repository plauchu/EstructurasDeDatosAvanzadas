/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package merge;

/**
 *
 * @author RPLAUCHUR
 */
public class Merge {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        int [] a = {3, 5, 5 , 1 , -3 , 1, 27};
        System.out.println(imprimeArreglo(a));
        mergeSort(a);
        System.out.println(imprimeArreglo(a));
    }
    
    public static String imprimeArreglo(int [] a){
        StringBuilder sb = new StringBuilder();
        
        for(int i = 0; i < a.length ; i++){
            sb.append(a[i]+ " ");
        }
        
        return sb.toString();
    }
    
    public static void mergeSort(int [] a) {
        mergeSort(a, 0 , a.length-1);
    }
    
    public static void mergeSort(int [] a, int low, int high) {
        if(low<high){
            int middle = low+(high-low)/2;
            mergeSort(a, low, middle);
            mergeSort(a, middle+1, high);
            merge(a,low,middle,high);
        }
    }
    
    public static void merge(int [] a, int low, int middle, int high) {
        int aux [] = new int[a.length];
        int i, j, k;
        
        for(i= low;i<=high;i++){
            aux[i]= a[i];
        }
        i=low;
        j=middle+1;
        k=low;
        while(i<=middle&j<=high){
            if(aux[i]<=aux[j]){
                a[k]=aux[i];
                i++;
            }else{
                a[k]=aux[j];
                j++;
            }
            k++;
        }
        while(i<=middle){
            a[k]=aux[i];
            k++;
            i++;
        }
        while(i<=middle){
            a[k]=aux[j];
            k++;
            j++;
        }
    }
}
