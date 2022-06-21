#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 12:27:35 2019

@author: Plauchu
"""

# Implementación de una pila en pyhton

class Stack: # Creamos la clase Stack
    def __init__(self):
        self.items = []
    
    def is_empty(self): # Metodo para verificar si la pila esta vacia
        return self.items == []
    
    def push(self, item): # Metodo para insertar elementos a la pila
        self.items.insert(0, item)
    
    def pop(self): # Metodo para eliminar el ultimo elemento apilado
        return self.items.pop(0)
    
    def __str__(self): # Metodo para mostrar los elementos de la pila
        return(self.items)

class Binary_Tree_Node:
    def __init__(self, dato):
        self._dato = dato
        self._ladoIzq = None
        self._ladoDer = None
    
    def getDato(self):
        return self._dato
    
    def getIzq(self):
        return self._ladoIzq
    
    def getDer(self):
        return self._ladoDer
    
    def setDato(self, dato):
        self._dato = dato
        
    def setIzq(self, sig):
        self._ladoIzq = sig
    
    
    def setDer(self, sig):
        self._ladoDer = sig
    
    def __str__(self):
        return str(self._dato)
    
class Binary_Tree:
    def __init__ (self, node):
        self._raiz = node
    
    def __iter__(self):
        return Iterador(self._raiz)
    
    def getRoot (self):
        return self._raiz
    
    def setIzq(self, nodo):
        self._raiz.setDer(nodo)
    
    def setDer(self, nodo):
        self._raiz.setIzq(nodo)
    
    def setRoot (self, node):
        node.setIzq(self._raiz)
        self._raiz = node
    
    def getLadoIzq(self):
        return self._raiz.getIzq()
    
    def getLadoDer(self):
        return self._raiz.getDer()
    
    def isEmpty(self):
        resp = False
        
        if(self._raiz == None):
            resp = True
        
        return resp
    
    def esHoja(self, nodo):
        resp = False
        
        if(nodo.getDer() == None and nodo.getIzq() == None):
            resp = True
        
        return resp
    
    def size():
        it = iter()
        cont = 0
        if(it.hasNext()):
            it.next()
            cont = cont + 1
        return cont

    def contains(data):
        return True;
    
    def find(self, data):
        if(self.isEmpty()):
            EmptyCollectionException("Colección vacía")
        return self._raiz  
    
    def __str__(self):
        return self.toString(self.getRoot(), 0)
    
    def toString(self, node, indent):
        indentation = []
        result = []
        
        if(node != None):
            i = 0
            while(i < indent):
                indentation.append(" ")
                i = i + 1
            if(self.esHoja(node)):
                result.append("[")
                result.append(node.getDato())
                result.append("]\n")
            else:
                result.append("(")
                result.append(node.getDato())
                result.append(")\n")
                if(node.getIzq()!= None):
                    result.append(indentation)
                    result.append("Izq.: ")
                    result.append(self.toString(node.getIzq(),indent+2))
                if(node.getDer()!= None):
                    result.append(indentation)
                    result.append("Der.: ")
                    result.append(self.toString(node.getDer(),indent+2))
        return str(result)

class ExpressionTree(Binary_Tree):
    def __init__(self, nodo):
        Binary_Tree_Node(nodo)
    
    def evaluateTree(self):
        flag = not isinstance(self.getRoot().getdato(), float)
        while(not flag):
            auxPrincipal = self.getRoot()
            evaluado = False
            while(not evaluado):
                auxIzq = auxPrincipal.getIzq()
                auxDer=auxPrincipal.getDer()
                
                flag2 = isinstance(auxIzq.getDato(), chr)
                
                if(flag2):
                    auxPrincipal = auxIzq
                else:
                    flag3 = isinstance(auxDer.getDato(), chr)
                    if(flag3):
                        auxPrincipal = auxDer
                    else:
                        evaluateNode(auxPrincipal)
                        evaluado = True
                        
        return float(self.getRoot().getDato())

def evaluateNode (nodo):
    aux = nodo.getIzq()
    resp = float(aux.getDato())
    nodo.setIzq(None)
    aux=nodo.getDer()
    
    carac = chr(nodo.getDato())
    
    if carac == '+':
        resp=resp+ float(aux.getDato())
    elif carac == '-':
        resp=resp- float(aux.getDato())
    elif carac == '/':
        #ver que no sea 0 lo que esta en aux
        resp=resp/ float(aux.getDato())
    elif carac == '*':
        resp=resp* float(aux.getDato())
    
    nodo.setDer(None)
    nodo.setDato(resp)
    
        
class TokenDesconocidoException(Exception):
    pass
 
class EmptyCollectionException(Exception):
    pass
       
class Iterador:
    def __init__(self, prim):
        self._actual = prim
    
    def hasNext(self):
        return self._actual != None

    def next(self):
        if (self.hasNext()):
            resul = self._actual.getDato()
            self._actual = self._actual.getDer()
            return resul
        else:
             raise StopIteration("No hay más elementos en la lista")

nodo1= Binary_Tree_Node(10)
nodo2= Binary_Tree_Node(11)
nodo3= Binary_Tree_Node(12)
arbol= Binary_Tree(nodo1)
arbol.setDer(nodo3)
arbol.setIzq(nodo2)
#print(arbol)    
print(arbol)     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

