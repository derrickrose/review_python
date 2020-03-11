#!/usr/bin/python3.4
# -*-coding:utf-8 -*

test:str = input ("entrez un caractere ")
print("test {0}".format(test))


for carac in test:
    print(carac)


test_upper_case=test.upper()
print("test upper {0}".format(test_upper_case))


print("le premier caractere est {0} ".format(test[0]))


string = """test
multi line"""


print(string)




       
prenom = "Paul"
nom = "Dupont"
age = 21
print( \
    "hirehirheirheirh"
  "Je m'appelle {0} {1} ({3} {0} pour l'administration) et j'ai {2} " \
  "ans.".format(prenom, nom, age, nom.upper()))


""" substring """

coupee = test[0:2]
print ("couupe"+coupee)
