#!/usr/bin/python3.4
# -*-coding:utf-8 -*

from os import system
from random import randrange


def get_color(numero):
    if numero%2 == 0:
        return "noir"
    else:
        return "rouge"


def get_bet_value():
    valor = 50
    while valor == 50 or valor <0 or valor > 49:
        current_value = input("Entrez un numero de 0 a 49 ")
        try:
            current_value = int(current_value)
        except:
            pass
        else:
            valor = current_value
    return valor
            
            
def get_played_money():
    valor = 0
    while valor <= 0:
        current_value = input("Entrez votre mise en $ ")
        try:
            current_value = int(current_value)
        except:
            pass
        else:
            valor = current_value
    return valor


def get_random_value():
    return randrange(50)


def calculate_benefit(played_money, bet_value, winning_number):
    if winning_number == bet_value:
        return played_money*2 
    elif get_color(winning_number)==get_color(bet_value):
        return -played_money/2
    else:
        return -played_money




    
    
      
      
if __name__ == "__main__":
    played_money = get_played_money()
    bet_value = get_bet_value()
    bet_color = get_color(bet_value)
    winning_number = get_random_value()
    winning_color = get_color(winning_number)
    benefit = calculate_benefit(played_money, bet_value, winning_number)
    current_money = played_money + benefit
    print("Mise $",played_money)
    print("Numero joué",bet_value)
    print("Couleur jouée",bet_color)
    print("Numero gagnant",winning_number)
    print("Couleur gagnante",winning_color)
    print("Argent courrant",current_money)
    print("benefit ",benefit)
    system("pause")
       
