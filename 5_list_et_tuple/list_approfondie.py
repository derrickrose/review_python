#!/usr/bin/python3.4
# -*-coding:utf-8 -*

""" method split """
chaine = "hello word"
liste = chaine.split(" ")
print(liste)

""" join avec espace """
liste = ['bonjour','mes', 'dames', 'et', 'monsieurs']
chaine = " ".join(liste)
print(chaine)

""" redifinition de la methode print """
def imprimer(*params, delimiteur=" ", fin="\n"):
    chaine = ""
    for elmt in params:
        chaine+=(str(elmt)+delimiteur)
    chaine.strip()
    chaine+=fin
    print(chaine)

if __name__ == '__main__':
    valor = 10
    value = 15
    imprimer(valor,value)
    
    liste = [valor,value]
    """ on peut aussi passer une liste comme parametres de fonction voyez la diff"""
    print (liste)
    print(*liste)
    """ intervation directement dans la liste """
    liste = [nb * 2 for nb in liste]
    print(liste)
    """ filtrer dans une liste """
    liste.append(10)
    liste.append(11)
    liste.append(13)
    print(liste)
    liste = [nb for nb in liste if nb%2 == 0]
    print(liste)

    
