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
            


def get_money(output_label, limit_money=0):
    valor = 0
    while valor <= 0 or (limit_money>0 and limit_money-valor<0):
        current_value = input(output_label)
        try:
            current_value = int(current_value)
        except:
            pass
        else:
            valor = current_value
    return valor

    
def get_played_money(total_money):
    return get_money("Entrez votre mise en $ ",total_money)


def get_total_money():
    return get_money("Entrez votre argent total en $ ")  


def get_random_value():
    return randrange(50)


def calculate_benefit(played_money, bet_value, winning_number):
    if winning_number == bet_value:
        print("Bien joué, votre mise est triplée!!")
        return played_money*2 
    elif get_color(winning_number)==get_color(bet_value):
        print("Pas mal, on vous rembourse la moitié!!")
        return -played_money/2
    else:
        print("Désolé, vous perdez votre mise!!")
        return -played_money
      
      
if __name__ == "__main__":
    total_money = get_total_money()
    while total_money>0:
        played_money = get_played_money(total_money)
        bet_value = get_bet_value()
        bet_color = get_color(bet_value)
        winning_number = get_random_value()
        winning_color = get_color(winning_number)
        benefit = calculate_benefit(played_money, bet_value, winning_number)
        total_money += benefit
        print("""
        Mise $ {0}
        Numero joué {1}
        Couleur jouée {2}
        Numero gagnant {3}
        Couleur gagnante {4}
        Benefice {5}
        Argent total {6}
        """.format(played_money,bet_value,bet_color,winning_number,winning_color,benefit,total_money))
    print("Vous avez perdu!!!")
    system("pause")

          
