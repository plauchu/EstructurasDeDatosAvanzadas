# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 19:21:28 2019

@author: Plauchu
"""


class NilNode(object):
    """
    Se usa solamente para balancear el árbol al darle a los nodos hoja hijos nulos.
    """
    def __init__(self):
        self.red = False


NIL = NilNode() # Nil is the sentinel value for nodes


class RBNode(object):

    def __init__(self,data):
        self.red = False
        self.p = None
        self.data = data
        self.left = NIL
        self.right = NIL

class RedBlackTree(object):
    
    def __init__(self):
        self.root = None
        
    def leftrotate(self,node):
        y=node.right
        node.right=y.left
        if y.left is not NIL:
            y.left.p = node
        y.p = node.p
        if node.p == None:
            self.root=y
        elif node==node.p.left:
            node.p.left = y
        else: 
            node.p.right = y
        y.left = node
        node.p = y
        
    def rightrotate(self,node):
        y=node.p
        y.left=node.right
        if node.right is not NIL:
            node.right.p = y
        node.p = y.p
        if y.p == None:
            self.root=node
        elif y==y.p.right:
            y.p.right = node
        else: 
            y.p.left = node
        node.right = y
        y.p = node
            
            
    def RBinsert(self,node):
        y = NIL
        x = self.root
        while x is not NIL and x!=None:
            y = x
            if node.data < x.data:
                x=x.left
            else:
                x = x.right
        node.p = y
        if y is NIL:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node
        node.left = NIL
        node.right = NIL
        node.red = True
        while node.p.red:#A partir de aquí se ajusta el árbol para cumplir las propiedades del árbol ya que se insertó el nodo
            if node.p == node.p.p.left:
                y=node.p.p.right
                if y.red:#Este caso es para cuando el tío del nodo es rojo
                    node.p.red = False
                    y.red = False
                    node.p.p.red = True
                    node = node.p.p
                elif node == node.p.right:#aquí el tio del nodo es negro y el nodo es un hijo derecho
                    node = node.p
                    self.leftrotate(node)
                    node.p.red = False#Aquí se pasa al tercer caso que el tío es negro pero el nodo es hijo izquierdo
                    node.p.p.red=True
                    self.rightrotate(node.p.p)
            else:#Es lo mismo que el if pero para cuando el padre del nodo es hijo derecho
                y=node.p.p.right
                if y.red:
                    node.p.red = False
                    y.red = False
                    node.p.p.red = True
                    node = node.p.p
                elif node == node.p.left:
                    node = node.p
                    self.rightrotate(node)
                    node.p.red = False
                    node.p.p.red=True
                    self.leftrotate(node.p.p)
        self.root.red=False
    
    def minimo(node):
        while node.left is not NIL:
            node = node.left
        return node

    def rbtransplant(self,u,v):#usamos esto para mover subárboles dentro del árbol
        if u.p is None:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        v.p=u.p
    
    def rbdelete(self,node):
        y=node
        yo = y.red
        if node.left is NIL:
            x=node.right
            self.rbtransplant(node,node.right)
        elif node.right == NIL:
            x=node.left
            self.rbtransplant(node,node.left)
        else:
            y = node.right.minimo()
            yo = y.red
            x = y.right
            if y.p == node:
                x.p =y 
            else:
                self.rbtransplant(y,y.right)
                y.right = node.right
                y.right.p = y
            self.rbtransplant(node, y)
            y.left=node.left
            y.left.p=y
            y.red=node.red
        if not yo: #A partir de aquí se modifica el árbol para cumplir las propiedades del arreglo ya que se borró el nodo
            while x is not self.root and x.red is False:
                if x==x.p.left:
                    w = x.p.right
                    if w.red:
                        w.red=False#El hermano de x, que es w, es rojo. W necesita hijos negros, por lo que se hacen cambios de colores y una rotación
                        x.p.red = True
                        self.leftrotate(x.p)
                        w = x.p.right
                    if w.left.red is False and w.right.red is False:
                        w.red = True#Aquí w es negro y sus dos hijos son negros. Se cambia w y se cambia el padre de w si era rojo
                        x=x.p
                    elif w.right.red is False:#w es negro, su hijo derecho es negro y el hijo izquierdo es rojo
                        w.left.red = False
                        w.red = True
                        self.rightrotate(w)
                        w = x.p.right
                        w.red = x.p.red#W es negro y su hijo derecho es rojo
                        x.p.red = False
                        w.right.red = False
                        self.leftrotate(x.p)
                        x=self.root
                else:
                    w = x.p.false
                    if w.red:
                        w.red=False
                        x.p.red = True
                        self.right(x.p)
                        w = x.p.left
                    if w.right.red is False and w.left.red is False:
                        w.red = True
                        x=x.p
                    elif w.left.red is False:
                        w.right.red = False
                        w.red = True
                        self.leftrotate(w)
                        w = x.p.left
                    w.red = x.p.red
                    x.p.red = False
                    w.left.red = False
                    self.rightrotate(x.p)
                    x=self.root
            x.red = False
    
    def inorder(self):
        if self is not None and not NIL:
            self.root.left.inorder()
            print(self.root.data)
            self.root.right.inorder()
            


tree = RedBlackTree()
a = RBNode(1)
b = RBNode(2)
c= RBNode(3)
tree.RBinsert(a)
tree.RBinsert(b)
tree.RBinsert(c)
tree.rbdelete(b)
# print(tree.root)
