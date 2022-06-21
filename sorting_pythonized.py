# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 11:22:06 2019

@author: Plauchu
"""

"""
Cambios con respecto a Sorting.py:
    1) Uso de "notación serpiente" en lugar de "notación camello".
    2) Intercambio ("swap") en dos pasos en lugar de tres (ver función
    "ordenamiento_por_seleccion_directa").
    3) Uso de "funciones variables", es decir, colocar los nombres de
    funciones dentro de variables (como si las funciones fueran datos) pero
    luego ejecutar las funciones (como si las funciones fueran código).
    4) Uso de "plot" para visualizar la gráfica de resultados directamente
    desde Python en lugar de producir un archivo CSV de salida y externamente
    usar Excel para producir la gráfica basándose en los datos de dicho archivo.
"""


def ordenamiento_por_seleccion_directa(lista_valores):
    i=0
    while i<len(lista_valores):
        min=i
        indices=list(range(i+1,len(lista_valores)))
        for indice in indices:
            if lista_valores[indice]<lista_valores[min]:
                min=indice
        #Intercambio de los valores de lista_valores[min] y lista_valores[i]:
        lista_valores[min],lista_valores[i]=lista_valores[i],lista_valores[min]
        i=i+1

#Prueba:
lista1=[3,4,5,2,1,-14] 
ordenamiento_por_seleccion_directa(lista1)
print(lista1)
          
"""
Original en Java:
    // Applies the straight selection algorithm to array 'a,' which is assumed
    // to be full (contains no "holes" or empty cells), in order to sort its
    // elements, assumed to be primitive integer values:
    public static void selectionSort(int a[]) {
        int i,j,min,aux;
        
        for(i=0;i<a.length-1;i=i+1) {
            min=i;
            for(j=i+1;j<a.length;j=j+1)
                if(a[j]<a[min])
                    min=j;
            aux=a[min];
            a[min]=a[i];
            a[i]=aux;
        }
    }
"""


def ordenamiento_por_insercion_directa(lista_valores):
    i=1
    while i<len(lista_valores):
        sig=lista_valores[i]
        hueco=i
        while hueco>0 and sig<lista_valores[hueco-1]:
            lista_valores[hueco]=lista_valores[hueco-1]
            hueco=hueco-1
        lista_valores[hueco]=sig
        i=i+1

#Prueba:
lista1=[3,4,5,2,1,-14] 
ordenamiento_por_insercion_directa(lista1)
print(lista1)


"""
Original en Java:
    // Applies the straight insertion algorithm to array 'a,' which is assumed
    // to be full (contains no "holes" or empty cells), in order to sort its
    // elements, assumed to be primitive integer values:
    public static void insertionSort(int a[]) {
        int i,j,next,hole;
        
        for(i=1;i<a.length;i=i+1) {
            next=a[i];
            hole=i;
            while(hole>0&&next<a[hole-1]) {
                a[hole]=a[hole-1];
                hole=hole-1;
            }
            a[hole]=next;
        }
    }
"""

def merge_sort(lista_valores):
    merge_sort_r(lista_valores,0,len(lista_valores)-1)

def merge_sort_r(lista_valores,lim_inf,lim_sup):
    if lim_inf<lim_sup:
        indice_intermedio=lim_inf+(lim_sup-lim_inf)//2
        merge_sort_r(lista_valores,lim_inf,indice_intermedio)
        merge_sort_r(lista_valores,indice_intermedio+1,lim_sup)
        merge(lista_valores,lim_inf,indice_intermedio,lim_sup)

def merge(lista_valores,lim_inf,indice_intermedio,lim_sup):
    aux=list(lista_valores)
    i=lim_inf
    j=indice_intermedio+1
    k=lim_inf
    while i<=indice_intermedio and j<=lim_sup:
        if aux[i]<=aux[j]:
            lista_valores[k]=aux[i]
            i=i+1
        else:
            lista_valores[k]=aux[j]
            j=j+1
        k=k+1
    while i<=indice_intermedio:
        lista_valores[k]=aux[i]
        k=k+1
        i=i+1
    while j<=lim_sup:
        lista_valores[k]=aux[j]
        k=k+1
        j=j+1

#Prueba:
lista1=[3,4,5,2,1,-14] 
merge_sort(lista1)
print(lista1)

"""
    // Original en Java:
    // Applies the mergesort algorithm to array 'a,' which is assumed
    // to be full (contains no "holes" or empty cells), in order to sort its
    // elements, assumed to be primitive integer values:
    public static void mergeSort(int a[]) {
        mergeSort(a,0,a.length-1);
    }

    private static void mergeSort(int a[],int lowIndex,int highIndex) {
        // Check if low is smaller then high (if not, the array is already
        // sorted):
        if (lowIndex<highIndex) {
            // Get the index of the element which is in the middle (or just to
            // the left of the middle, if there is an even number of elements):
            int middleIndex=lowIndex+(highIndex-lowIndex)/2;
            // Sort the left side of the array in place:
            mergeSort(a,lowIndex,middleIndex);
            // Sort the right side of the array in place:
            mergeSort(a,middleIndex+1,highIndex);
            // Combine the virtual sub-arrays resulting from both previous sorts:
            merge(a,lowIndex,middleIndex,highIndex);
        }
    }

    private static void merge(int[] a,int lowIndex,int middleIndex,int highIndex) {
        int aux[]=new int[a.length];
        int i,j,k;
        
        // Copy both parts into the auxiliary array:
        for(i=lowIndex;i<=highIndex;i=i+1)
            aux[i]=a[i];
        // Copy the smallest values from either the left or the right side of
        // the auxiliary array back to the original array:
        i=lowIndex;
        j=middleIndex+1;
        k=lowIndex;
        while(i<=middleIndex&&j<=highIndex) {
            if(aux[i]<=aux[j]) {
                a[k]=aux[i];
                i++;
            }
            else {
                a[k]=aux[j];
                j++;
            }
            k++;
        }
        // Copy the rest of the left side of the auxiliary array into the
        // original array:
        while(i<=middleIndex) {
            a[k]=aux[i];
            k++;
            i++;
        }
        // Copy the rest of the right side of the auxiliary array into the
        // original array:
        while(j<=highIndex) {
            a[k]=aux[j];
            k++;
            j++;
        }
    }
}

"""

#Returns a list of the first N integer values in ascending numerical order:
def generate_ordered_list(n):
    return list(range(1,n+1,1))
#Prueba:
a=generate_ordered_list(3)
print(a)

#Returns a list of the first N integer values in descending numerical order:
def generate_inverse_ordered_list(n):
    return list(range(n,0,-1))
#Prueba:
a=generate_inverse_ordered_list(3)
print(a)

#Returns a list of N random integers whose values fall between 0 and 999:
import random
def generate_random_ordered_list(n):
    res=[]
    for i in range(0,n):
        x=random.randint(0,999)
        res.append(x)
    return res
#Prueba:
a=generate_random_ordered_list(3)
print(a)

#Runs a test in which each of selection sort, insertion sort, and mergesort
#are run on each of three arrays (one in ascending order, one in inverse
#order and one in random order) for arrays of size 5, 10, 15,...,200:
import time
import matplotlib.pyplot as plt
def test():
    valores_x=[]
    valores_y_seleccion_directa=[]
    valores_y_insercion_directa=[]
    valores_y_merge_sort=[]
    
    #Repeats nine tests for each array size, storing processing time for the
    #sorting operation in each test:
    tamanio=5
    INCREMENTO=5
    TAMANIOFINAL=20
    while tamanio<=TAMANIOFINAL:
        valores_x=valores_x+[tamanio]
        
        #Creates three test lists (ascending order, inverse order, random order):
        lista_ordenada=generate_ordered_list(tamanio)
        lista_en_orden_inverso=generate_inverse_ordered_list(tamanio)
        lista_de_valores_aleatorios=generate_random_ordered_list(tamanio)
        print("Ordered list to sort:\n")
        print(lista_ordenada)
        print("Inverse ordered list to sort:\n")
        print(lista_en_orden_inverso)
        print("List of random values to sort:\n")
        print(lista_de_valores_aleatorios)

        #For each sorting method to test:
        for metodo in (ordenamiento_por_seleccion_directa,ordenamiento_por_insercion_directa,merge_sort):
            #For each testing list (in ascending order, in descending order, and in random order):
            for lista in (lista_ordenada,lista_en_orden_inverso,lista_de_valores_aleatorios):
                # Tests current sort method on current list and stores results in file:
                copia=list(lista)
                print(copia)
                time_before=time.perf_counter()
                metodo(copia)
                time_after=time.perf_counter()
                diff=time_after-time_before
                if lista is lista_de_valores_aleatorios:
                    if metodo is ordenamiento_por_seleccion_directa:
                        valores_y_seleccion_directa=valores_y_seleccion_directa+[diff]
                    elif metodo is ordenamiento_por_insercion_directa:
                        valores_y_insercion_directa=valores_y_insercion_directa+[diff]
                    else:
                        valores_y_merge_sort=valores_y_merge_sort+[diff]
                print(copia)
        tamanio=tamanio+INCREMENTO
    plt.xlabel("Número de datos")
    plt.ylabel("Unidades de tiempo")
    plt.plot(valores_x,valores_y_seleccion_directa,label="Selección directa")
    plt.plot(valores_x,valores_y_insercion_directa,label="Inserción directa")
    plt.plot(valores_x,valores_y_merge_sort,label="Mergesort")
    plt.legend(loc="upper left")
    
test()

