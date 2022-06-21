# -*- coding: utf-8 -*-
"""
Editor de Spyder

by: plauchu
"""

def ordenamientoPorSeleccionDirecta(listaValores):
    i=0
    while i < len(listaValores)-1:
        min=i
        indices = list(range(i+1, len(listaValores)))
        for indice in indices:
            if listaValores[indice]<listaValores[min]:
                min=indice
        aux=listaValores[min]
        listaValores[min]=listaValores[i]
        listaValores[i]=aux
        i=i+1

arr=[3,8,5,1,-3,1,27]
print(arr)
ordenamientoPorSeleccionDirecta(arr)
print(arr)

def ordenamientoPorInsercionDirecta(listaValores):
    i=1
    while i < len(listaValores):
        sig=listaValores[i]
        hueco=i
        while hueco>0 and sig<listaValores[hueco-1]:
            listaValores[hueco]=listaValores[hueco-1]
            hueco=hueco-1
        listaValores[hueco]=sig
        i=i+1
        
arr=[3,8,5,1,-3,1,27]
print(arr)
ordenamientoPorInsercionDirecta(arr)
print(arr)


