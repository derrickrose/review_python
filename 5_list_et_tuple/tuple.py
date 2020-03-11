#!/usr/bin/python3.4
# -*-coding:utf-8 -*


def decomposer(nombre,diviseur):
    entiere = nombre // diviseur
    reste = nombre % diviseur
    return entiere, reste


if __name__ == '__main__':
    liste = list()
    liste.append(9)
    liste.append(4)
    liste.append(5)
    liste.append(3)
    liste.append(7)
    liste.append(4)

    for i,	elm in enumerate(liste):
        print("la valeur dans {} est {}".format(i,elm)) 

    tuplez = ()
    print(tuplez)

    entiere, reste = decomposer(5,2)  
    print("entiere {} et rest {}".format(entiere,reste))







