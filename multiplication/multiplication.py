#!/usr/bin/python3.4
# -*-coding:utf-8 -*
"""module multipli contenant la fonction table"""

import os

def table(nb,max=10):
    i = 0
    while i < max:
        print(nb," * ",i+1," = ",nb*(i+1))
        i+=1
      
# test de la fonction table
if __name__ == "__main__":
    table(4,12)
    os.system("pause")
