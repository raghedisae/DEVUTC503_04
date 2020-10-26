# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 21:45:38 2020

@author: raghed
"""

#nombre des elements
def nbelements(l):
    if l:
        return 1+nbelements(l[1:])
    else:
        return 0
#somme des  element
def sommeElement(l):
    if l:
       
        return  l[0] +sommeElement(l[1:])
    else:
        return 0
#moyenne
def moyenne(l):
    if l:
       
        return  sommeElement(l)/nbelements(l)
    else:
        return 0

#inserrer un element dans list triye
def inserrer(l, n): 
    for i in range(nbelements(l)): 
        if l[i] > n: 
            index = i 
            break
    
    l = l[:i] + [n] + l[i:] 
    return l
  
def trie(l):
    if len(l) <= 1:
        return l
    else:
        return trie([e for e in l[1:] if e <= l[0]]) + [l[0]] +\
            trie([e for e in l[1:] if e > l[0]])

def rendreMonnai(s,sm):
    '''s : somme a rendre,
       sm: système de monnaie en oredre décroissant
    '''
    print(s,sm)
    if sm:
       nbPieceMax=s//sm[0]
       print(list(range(nbPieceMax+1)))
       reste = rendreMonnai(s-(nbPieceMax*sm[0]), sm[1:])
       # print([nbPieceMax] + rep)
       # return ((sm[0],nbPieceMax),)+ reste
       return {sm[0]:nbPieceMax, **reste}
    else:
        return {}


l=[1,4,5,40,2]
print ("taille",nbelements(l))
print ("somme",sommeElement(l))
print ("moyenne",moyenne(l))
l2=[1,2,4,5]
n=3
print ("inserrer",n,"dans ",l2,":",inserrer(l2,3))
print ("trier ",l,":",trie(l))
print (rendreMonnai(7000,(5000,1000)))