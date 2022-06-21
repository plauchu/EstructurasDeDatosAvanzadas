#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 14:46:02 2019

@author: Plauchu
"""

def odd_Even_Sort (lista_valores):
    ordenado = False
    while not ordenado:
        ordenado = True
        i=0
        while i<len(lista_valores)-1:
            if lista_valores[i + 1] < lista_valores[i]:
                aux = lista_valores[i]
                lista_valores[i] = lista_valores[i + 1]
                lista_valores[i + 1] = aux
                ordenado = False
            i = i + 2
        i=1
        while i<len(lista_valores)-1:
            if lista_valores[i + 1] < lista_valores[i]:
                aux = lista_valores[i]
                lista_valores[i] = lista_valores[i + 1]
                lista_valores[i + 1] = aux
                ordenado = False
            i = i + 2
        
#Prueba:
arr=[3,8,5,1,-3,1,27]
print(arr)
odd_Even_Sort(arr)
print(arr)