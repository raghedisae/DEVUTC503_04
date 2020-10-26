# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 00:07:07 2020

@author: raghed
"""

a,b,c,d = 0.09,0.00001,0.25,0.000005

def U(un):
    if un==0:
        return 53000
    else:
        #print (un)
        return U(un-1)*(1+a-b*V(un-1))

def V(vn):
    if vn==0:
        return 9000
    else:
        return V(vn-1)*(1-c +d*U(vn-1))




#generateur
time_min = 1
time_max =20

for i in range (time_min, time_max):
    print ("instant",i,": (",U(i),",",V(i),")")

