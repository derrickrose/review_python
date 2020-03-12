#!/usr/bin/python3.4
# -*-coding:utf-8 -*

""" dictionnaire """
dictionnaire = dict()
dictionnaire["voalohany"]='first'
dictionnaire["faharoa"]='second'
dictionnaire["fahatelo"]='third'
print(dictionnaire)


""" autre moyen de definir un dictionnaire """
dicto = {}
dicto['ray']="un"
dicto['roa']="deux"
print(dicto)


""" considerons un echiquier """
""" http://www.echecspourtous.com/?page_id=168 """

echiquier = dict()
echiquier[('a',1)]='tour blanc 1'
echiquier[('a',2)]= 'pion blanc'
echiquier[('b',2)]= 'pion blanc'
echiquier[('c',2)]= 'pion blanc'
echiquier[('d',2)]= 'pion blanc'

""" le parcours d'un dictionnaire liste les clees """          
for elm in echiquier:
    print(elm)

""" liste aussi est passage par référence """

""" pour supprimer un element dun dictionnaire """
del echiquier[('a',1)]
print(echiquier)
valor =  echiquier.pop(('a',2))
print(echiquier)
print("valor " +str(valor))

""" parcours des clees """
for  index, key in enumerate(echiquier.keys()):
    print("numero {} la clee {} et valeur {}".format(index,key,echiquier[key]))


""" on se sert parfois des dictionnaires pour stocker des fonctions """

""" parcours des dictionnaires aveec .keys() .values() .items() """


