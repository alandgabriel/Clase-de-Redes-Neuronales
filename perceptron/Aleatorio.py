#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 17:55:50 2020

@author: alan
"""


class Aleatorio:
    
    def __init__(self):
        self.seed = 1181
        
        
    def gen(self,N, lInf, lSup):
        rnd = []
        for i in range (N):
            a=float(630360016)
            m=float(2147483647)
            self.seed=(a*self.seed)%m
            U=self.seed/m
            r=lSup-lInf
            rnd.append(int((U*r)+lInf))
        return rnd