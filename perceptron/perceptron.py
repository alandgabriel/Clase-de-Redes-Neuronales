#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 15:32:44 2020

@author: alan
"""

from ActivFunc import ActivFunc
from Aleatorio import Aleatorio
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from IPython.display import display

class Pnetwork:
    
    def __init__(self, x,t):
        
        self.datos = x
        self.targets =t
        Nw = min(np.size(x,0),np.size(x,1))
        Nb = max(np.size(x,0),np.size(x,1))
        rnd = Aleatorio()
        self.pesos =[]
        self.bias = []
        for i in range (np.size(self.targets,0)):
            self.pesos.append(rnd.gen(Nw,-1,1))                  #se inicializan los pesos y sesgos
            self.bias.append(rnd.gen(Nb,-1,1))
        self.pesos = np.array(self.pesos)
        self.bias = np.array(self.bias)
        
    def training (self):
        eSum = 100
        count = 0
        err = []
        while (eSum !=0):
            out = np.dot(self.pesos,self.datos) + self.bias
            a = ActivFunc(out.flatten()).Linear().reshape((3,4))
            e = self.targets-a
            eSum = np.sum(np.abs(e))
            err.append(eSum)
            self.pesos = self.pesos + np.dot(e,self.datos.T)
            self.bias = self.bias + e
            count += 1
        return  np.int32(a),count,err


#Perceptron


x = np.array( [[0,0,1,1], [0,1,0,1]])       #Se construye la entrada que consiste de las permutaciones posibles de dos bits
    
#%%  Red de perceptrones

t_Global = np.array([[0,0,0,1],[0,1,1,1],[1,0,0,0]])

network = Pnetwork(x,t_Global)
o_Global,i5,error = network.training()


d={'in':['00','01','10','11'],'AND':o_Global[0,:],'OR':o_Global[1,:],'NOR':o_Global[2,:]}

df =pd.DataFrame(d)
display(df)
#print(df.to_latex(caption='Tablas de verdad, red de perceptrones'))
plt.figure()
plt.title('serie de tiempo de error')
plt.xlabel('epocas')
plt.ylabel('error')
plt.plot(error)
plt.show()
