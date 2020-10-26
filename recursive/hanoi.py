# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 09:07:07 2020

@author: raghed
"""
def deplacer(n,depart,arrivee) :
   
    print ("disque",n,depart,"->",arrivee)

def hanoi_recursif(n,debut,inter,fin) :
    """jeu des tours de Hanoi :
    déplacer n disques de la tour gauche à la tour droite
    en utilisant la tour milieu comme tour de transit
    """
    if n > 0 :
        hanoi_recursif(n-1,debut,fin,inter)
        deplacer(n,debut,fin)
        hanoi_recursif(n-1,inter,debut,fin)
       
hanoi_recursif(4,"A","B","C")