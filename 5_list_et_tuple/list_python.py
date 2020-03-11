#!/usr/bin/python3.4
# -*-coding:utf-8 -*

my_list = list()
my_list.append(5)
list_2 = [1,2,3]

"""acceder a un element de la liste """
valor = list_2[0]

print(my_list)
print(list_2)
print("le premier element de la liste est {}".format(list_2[0]))

""" imprimer les elements de la liste"""
ma_liste = [
    4,
    9,
    0,
    4, 5,  6]

print(len(ma_liste))

print(""" parcour element dans la liste""")

for elmt in ma_liste:
    print("element {}".format(elmt))

print(""" enlever element depuis une liste""")
del ma_liste[1]

for elmt in ma_liste:
    print("element {}".format(elmt))

print(""" enlever element depuis une liste avec remove""")
ma_liste.remove(4)

for elmt in ma_liste:
    print("element {}".format(elmt))

print("""parcour lliste avec enumerate""")
for index,elmt in enumerate(ma_liste):
    print("la valeur en la position {} est {}".format(index,elmt))
