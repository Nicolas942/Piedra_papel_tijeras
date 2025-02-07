import random

print("--------------------------------------------")
print("1) Piedra")
print("2) papel")
print("3) tijeras")
print("--------------------------------------------")

usu = int(input("Dijite el numero correspondiente a su decisión: "))

maq = random.randint(1,3)

if usu >= 4:
    print("Opcion no valida")

elif usu == maq:
    print(f"el usuario escogio: {usu}")
    print(f"la computadora escogio: {maq}")
    print("Empate")

elif (usu == 3 and maq == 1) or (usu == 1 and maq == 2) or (usu == 2 and maq == 3):
    print(f"el usuario escogio: {usu}")
    print(f"la computadora escogio: {maq}")
    print("Perdiste")

else:
    print(f"el usuario escogio: {usu}")
    print(f"la computadora escogio: {maq}")
    print("Ganaste")



