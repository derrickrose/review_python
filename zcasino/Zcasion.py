from os import system


def get_color(numero):
    if numero%2 == 0:
        return "black"
    else:
        return "red"


def get_bet_value():
    valor = 50
    while valor == 50 or valor <0 or valor > 49:
        current_value = input("entrez un numero de 0 a 49 ")
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
        current_value = input("entrez votre mise en $ ")
        try:
            current_value = int(current_value)
        except:
            pass
        else:
            valor = current_value
    return valor
      
      
if __name__ == "__main__":
    played_money = get_played_money()
    bet_value = get_bet_value()
    bet_color = get_color(bet_value)
    print("played money $",played_money)
    print("bet value",bet_value)
    print("bet color",bet_color)
    system("pause")
       