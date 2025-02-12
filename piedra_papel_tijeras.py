import random

print("-----------------------")
print("1)Piedra")
print("2)papel")
print("3)Tijeras")
print("-----------------------")

usu = int(input("Ingrese el número correspondiente a su decisión: "))
maq = random.randint(1,3)

if usu >= 4:
    print("No valido")
else:
    if usu == 1:
        print("Tú elegiste: piedra")
    elif usu == 2:
        print("Tú elegiste: papel")
    else:
        print("Tú elegiste: tijeras")

    if maq == 1:
        print("La maquina eligio: piedra")
    elif maq == 2:
        print("La maquina eligio: papel")
    else:
        print("La maquina eligio: tijeras")

    if usu == maq:
        print("empate")
    elif usu == 2 and maq == 1:
        print("Ganaste")
    elif usu == 3 and maq == 2: 
        print("Ganaste")
    elif usu == 1 and maq == 3:
        print("Ganaste")
    else:
        print("Perdiste")
