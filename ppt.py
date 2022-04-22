import random

aleat=random.randrange(0, 3)
elpc=""
print("1. PIEDRA")
print("2. PAPEL")
print("3. TIJERA")
mov=int(input("¿Cuál es su movimiento?"))
if mov == 1:
    elusu="Piedra"
if mov == 2:
    elusu="Papel"
if mov == 3:
    elusu="Tijera"
print("ELEGISTE", elusu)
if aleat == 0:
    elpc="Piedra"
if aleat == 1:
    elpc="Papel"
if aleat == 2:
    elpc="Tijera"
print("EL MOVIMIENTO DE LA MÁQUINA ES: ",elpc)
if elpc == "Piedra" and elusu =="Tijera":
    print("PERDISTE, LA PIEDRA DESTROZA LAS TIJERAS")
if elpc == "Papel" and elusu == "Tijera":
    print("GANASTE, LAS TIJERAS CORTAN EL PAPEL")
if elpc == "Tijera" and elusu =="Tijera":
    print("EMPATE")
if elpc == "Piedra" and elusu =="Papel":
    print("GANASTE, EL PAPEL ENVUELVE A LA PIEDRA")
if elpc == "Papel" and elusu == "Papel":
    print("EMPATE")
if elpc == "Tijera" and elusu == "Papel":
    print("PERDISTE, LAS TIJERAS CORTAN EL PAPEL")
if elpc == "Piedra" and elusu == "Piedra":
    print("EMPATE")
if elpc == "Papel" and elusu == "Piedra":
    print("PERDISTE, EL PAPEL ENVUELVE A LA PIEDRA")
if elpc == "Tijera" and elusu == "Piedra":
    print("GANASTE, LA PIEDRA ROMPE LAS TIJERAS")