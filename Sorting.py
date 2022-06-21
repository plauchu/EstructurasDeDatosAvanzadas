# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 11:22:06 2019

@author: Plauchu
"""

def ordenamientoPorSeleccionDirecta(listaValores):
    i=0
    while i<len(listaValores):
        min=i
        indices=list(range(i+1,len(listaValores)))
        for indice in indices:
            if listaValores[indice]<listaValores[min]:
                min=indice
        aux=listaValores[min]
        listaValores[min]=listaValores[i]
        listaValores[i]=aux
        i=i+1

#Prueba:
lista1=[3,4,5,2,1,-14] 
ordenamientoPorSeleccionDirecta(lista1)
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


def ordenamientoPorInsercionDirecta(listaValores):
    i=1
    while i<len(listaValores):
        sig=listaValores[i]
        hueco=i
        while hueco>0 and sig<listaValores[hueco-1]:
            listaValores[hueco]=listaValores[hueco-1]
            hueco=hueco-1
        listaValores[hueco]=sig
        i=i+1

#Prueba:
lista1=[3,4,5,2,1,-14] 
ordenamientoPorInsercionDirecta(lista1)
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

def mergeSort(listaValores):
    mergeSortR(listaValores,0,len(listaValores)-1)

def mergeSortR(listaValores,limInf,limSup):
    if limInf<limSup:
        indiceIntermedio=limInf+(limSup-limInf)//2
        mergeSortR(listaValores,limInf,indiceIntermedio)
        mergeSortR(listaValores,indiceIntermedio+1,limSup)
        merge(listaValores,limInf,indiceIntermedio,limSup)

def merge(listaValores,limInf,indiceIntermedio,limSup):
    aux=list(listaValores)
    i=limInf
    j=indiceIntermedio+1
    k=limInf
    while i<=indiceIntermedio and j<=limSup:
        if aux[i]<=aux[j]:
            listaValores[k]=aux[i]
            i=i+1
        else:
            listaValores[k]=aux[j]
            j=j+1
        k=k+1
    while i<=indiceIntermedio:
        listaValores[k]=aux[i]
        k=k+1
        i=i+1
    while j<=limSup:
        listaValores[k]=aux[j]
        k=k+1
        j=j+1

#Prueba:
lista1=[3,4,5,2,1,-14] 
mergeSort(lista1)
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
def generateOrderedList(n):
    return list(range(1,n+1,1))
#Prueba:
a=generateOrderedList(3)
print(a)

#Returns a list of the first N integer values in descending numerical order:
def generateInverseOrderedList(n):
    return list(range(n,0,-1))
#Prueba:
a=generateInverseOrderedList(3)
print(a)

#Returns a list of N random integers whose values fall between 0 and 999:
import random
def generateRandomOrderedList(n):
    res=[]
    for i in range(0,n):
        x=random.randint(0,999)
        res.append(x)
    return res
#Prueba:
a=generateRandomOrderedList(3)
print(a)

#Runs a test in which each of selection sort, insertion sort, and mergesort
#are run on each of three arrays (one in ascending order, one in inverse
#order and one in random order) for arrays of size 5, 10, 15,...,200:
import time
def test():
    #Opens output file to write results in CSV format for easier post-processing:
    f=open("PythonData1.csv","w+")
    f.write("ProblemSize:,SelectionSortOrderedArrayTime:,SelectionSortInverseOrderArrayTime:,SelectionSortRandomOrderArrayTime:,InsertionSortOrderedArrayTime:,InsertionSortInverseOrderArrayTime:,InsertionSortRandomOrderArrayTime:,MergeSortOrderedArrayTime:,MergeSortInverseOrderArrayTime:,MergeSortRandomOrderArrayTime:,\n")
    
    #Repeats nine tests for each array size, storing processing time for the
    #sorting operation in each test:
    tamanio=5
    INCREMENTO=5
    TAMANIOFINAL=200
    while tamanio<=TAMANIOFINAL:
        f.write("%d," % tamanio)
        
        #Creates three test lists (ascending order, inverse order, random order):
        listaOrdenada=generateOrderedList(tamanio)
        listaEnOrdenInverso=generateInverseOrderedList(tamanio)
        listaDeValoresAleatorios=generateRandomOrderedList(tamanio)
        print("Ordered list to sort:\n")
        print(listaOrdenada)
        print("Inverse ordered list to sort:\n")
        print(listaEnOrdenInverso)
        print("List of random values to sort:\n")
        print(listaDeValoresAleatorios)
        
        #Tests selection sort on a list whose elements are already in ascending order:
        copia=list(listaOrdenada)
        print(copia)
        timeBefore=time.perf_counter()
        ordenamientoPorSeleccionDirecta(copia)
        timeAfter=time.perf_counter()
        diff=timeAfter-timeBefore
        f.write("%f," % diff)
        print(copia)

        #Tests selection sort on a list whose elements are originally in inverse order:
        copia=list(listaEnOrdenInverso)
        print(copia)
        timeBefore=time.perf_counter()
        ordenamientoPorSeleccionDirecta(copia)
        timeAfter=time.perf_counter()
        diff=timeAfter-timeBefore
        f.write("%f," % diff)
        print(copia)

        #Tests selection sort on a list whose elements are in random order:
        copia=list(listaDeValoresAleatorios)
        print(copia)
        timeBefore=time.perf_counter()
        ordenamientoPorSeleccionDirecta(copia)
        timeAfter=time.perf_counter()
        diff=timeAfter-timeBefore
        f.write("%f," % diff)
        print(copia)

        #Tests insertion sort on a list whose elements are already in ascending order:
        copia=list(listaOrdenada)
        print(copia)
        timeBefore=time.perf_counter()
        ordenamientoPorInsercionDirecta(copia)
        timeAfter=time.perf_counter()
        diff=timeAfter-timeBefore
        f.write("%f," % diff)
        print(copia)

        #Tests insertion sort on a list whose elements are originally in inverse order:
        copia=list(listaEnOrdenInverso)
        print(copia)
        timeBefore=time.perf_counter()
        ordenamientoPorInsercionDirecta(copia)
        timeAfter=time.perf_counter()
        diff=timeAfter-timeBefore
        f.write("%f," % diff)
        print(copia)

        #Tests insertion sort on a list whose elements are in random order:
        copia=list(listaDeValoresAleatorios)
        print(copia)
        timeBefore=time.perf_counter()
        ordenamientoPorInsercionDirecta(copia)
        timeAfter=time.perf_counter()
        diff=timeAfter-timeBefore
        f.write("%f," % diff)
        print(copia)

        #Tests mergesort on a list whose elements are already in ascending order:
        copia=list(listaOrdenada)
        print(copia)
        timeBefore=time.perf_counter()
        mergeSort(copia)
        timeAfter=time.perf_counter()
        diff=timeAfter-timeBefore
        f.write("%f," % diff)
        print(copia)
        
        #Tests mergesort on a list whose elements are originallyy in inverse order:
        copia=list(listaEnOrdenInverso)
        print(copia)
        timeBefore=time.perf_counter()
        mergeSort(copia)
        timeAfter=time.perf_counter()
        diff=timeAfter-timeBefore
        f.write("%f," % diff)
        print(copia)

        #Tests mergesort on a list whose elements are in random order:
        copia=list(listaDeValoresAleatorios)
        print(copia)
        timeBefore=time.perf_counter()
        mergeSort(copia)
        timeAfter=time.perf_counter()
        diff=timeAfter-timeBefore
        f.write("%f\n" % diff)
        print(copia)

        tamanio=tamanio+INCREMENTO
    f.close()

test()

