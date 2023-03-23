import random 
from random import randint


while True:
    print("Digite el numero de jugadores")
    jugadores = int(input())
    while jugadores < 2 or jugadores >6:
        print("no se puede jugar con",jugadores,"jugadores")
        print("Digite el numero de jugadores nuevamente")
        jugadores = int(input())
        plante = 10000
        user = [str() for ind in range (jugadores)]
        for i in range (1,jugadores+1,+1):
            print("Nombres de los jugadores")
            user [i-1] = input()
            print("Coloque el plante")
            print("El plante es de",plante )
            while True:
                for i in range(1, jugadores + 1 ):
                    if plante > 0:
                        print("El turno es para", user [i-1])
                        print("presione enter para lanzar el dado")
                        x = input()
                        lanzar1 = randint(0,5)+1
                        if lanzar1 == 1 or lanzar1 == 6:
                            print("El numero es", lanzar1)
                            print("Perdio!!! coloque el plante")
                            plante = plante + 10000
                            print("El plante total es de ", plante)
                        else:
                            print("Su puntaje es",lanzar1)
                            print("Agregue 10000 al plante")
                            plante = float(input())
                            while plante < 0 or plante > plante:
                                print("Incorrecto, agregue de nuevo 10000")
                                plante = float(input())
                                print("Presione enter para lanzar")
                                x = input()
                                lanzar = randint(0,5)+1
                                if lanzar1+1 > lanzar:
                                    print("Su puntaje es", lanzar)
                                    print("Vuelva  a lanzar")
                                else:
                                    print("Su numero es ",lanzar)
                                    print("Pasa!!! retire su dinero")
                                    print("El plante es igual a",plante)
                            else:
                                if plante <= 0:
                                    print("Fin del juego")
                                    break


                                