import math
import sys
import random

onde = []
carrello = 3
a = random.randint(0, 2)
b = random.randint(0, 31)

def drawMare():



    for s in range(3):
        colonna = []

        onde.append(colonna)
        for r in range(32):
            o = random.randint(1, 2)
            if o == 1:
                colonna.append("`")
            if o == 2:
                colonna.append("~")




def drawOnde():
    print("CACCIA AL TESORO")
    print("Decimali + unità")
    print("---------1---------2---------3--")
    print("01234567890123456789012345678901")
    print("".join(onde[0]))
    print("".join(onde[1]))
    print("".join(onde[2]))

def Radar():
    global x, y


    x = int(input("digita la coordinata x comprea tra 0 e 31..."))
    y = int(input("digita la coordinata y compresa tra 0 e 2..."))

    if isValidinput():
        onde[y][x] = "R"
        drawOnde()
        sonda()


    else:
        print("Coordinate fuori portata.RIPROVA")
        drawOnde()




def isValidinput():
    if  y >= 0 and y <=2 and x >=0 and x <=31:
        return True

#def carrello():
    #carrello = 3

    #carrello = carrello - 1

    #return carrello
    
def checkW():
    if y == a and x == b:
        onde[a][b] = "X"
        drawOnde()
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("Tesoro rovato!!Complimenti")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        return True

def distanza():
    while (b - x or x- b) and (a - y or y - a) <= 3:
        return True

def sonda():
    if distanza():
        print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
        print("Il tesoro è vicino di 3 valori nelle tue coordinate!!")
        print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")


while carrello > 0:
    print("Benvenuto! Per giocare digita le coordinate")
    print('R è il radar: ne hai a disposizione 3')
    #print(a, b)
    drawMare()
    Radar()
    carrello -= 1
    if checkW():
        break

print("GAME OVER")


