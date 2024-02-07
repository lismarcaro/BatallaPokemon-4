#Batalla Pokemon con Funciones


import random # para elegir el ataque del oponente

#variables
# pos 0 es vida, pos 1 es defensa
jugador = [100, 100]
oponente = [100, 100]

Ataques = ("latigo", "placaje", "Pistola de agua", "ascuas", "malicioso")
ataque1 = (10, 10)
ataque2 = (29, 31)
ataque3 = (18, 21)
ataque4 = (9, 11)
ataque5 = (5, 32)

#Funciones de ataques
def ataque_latigo(oponente):
    oponente[1] -= ataque1[1]
    oponente[0] -= ataque1[0]
    print(f"Tu ataque es: {Ataques[0]}")
    print(f"La vida del oponente es {oponente[0]}")

    if oponente[1] <= 0:
            oponente[1] = 1

def ataque_placaje(oponente):
    print(f"Tu ataque es: {Ataques[1]}")
    oponente[0] -= ataque2[1] * (100 / oponente[1])
    print(f"La vida del oponente es {oponente[0]}")

def ataque_pistola_de_agua(oponente):
    print(f"Tu ataque es: {Ataques[2]}")
    oponente[0] -= ataque3[0]
    print(f"La vida del oponente es {oponente[0]}")

def ataque_ascuas(oponente):
    print(f"Tu ataque es: {Ataques[3]}")
    print(f"La vida del oponente es {oponente[0]}")

def ataque_malicioso(oponente):
    oponente[1] -= ataque5[1]
    print("Tu ataque es: {Ataques[4]}")
    print(f'La vida del oponente es {oponente[0]}')
    

#Función para el turno del oponente
def turno_oponente(jugador):
    ataque_oponente = random.randrange(1, 5)
    if ataque_oponente == 1:
        jugador[1] -= ataque1[1]
        jugador[0] -= ataque1[0]
        print(f"El ataque de tu oponente es: {Ataques[0]}")
        print(f"Tu vida es {jugador[0]}")


while jugador[0] > 0 and oponente[0] > 0:
    print("Escoge tu nuevo ataque:")
    print("Los ataques son: latigo, placaje, pistola de agua, ascuas y malicioso")
    ataque_jugador = input("Ataque: ")

    if ataque_jugador == "malicioso":
        ataque_malicioso(oponente)
        
    elif ataque_jugador == "latigo":
        ataque_latigo(oponente)

    elif ataque_jugador == "placaje":
        ataque_placaje(oponente)

    elif ataque_jugador == "pistola de agua":
        ataque_pistola_de_agua(oponente)
        
    elif ataque_jugador == "ascuas":
        ataque_ascuas(oponente)

    turno_oponente(jugador)

    #chequeo de si alguna vida llegó a cero
    if jugador[0] <= 0 or oponente[0] <= 0:
        break

#Resultado del juego
if jugador[0] <= 0:
    print("¡Perdiste! La vida de tu personaje llegó a cero.")
else:
    print("¡Ganaste! La vida del oponente llegó a cero.")

