
cantidad = int(input("Cuantos numeros quieres leer?\n"))
mayores_a_cero = 0
menores_a_cero = 0
iguales_a_cero = 0
for i in range(cantidad):
    numero = int(input("Ingresa un numero:\n"))
    if numero > 0:
        mayores_a_cero += 1
    elif numero < 0:
        menores_a_cero += 1
    else:
        iguales_a_cero += 1
print(f"Ingresaste {mayores_a_cero} numeros mayores a cero")
print(f"Ingresaste {menores_a_cero} numeros menores a cero")
print(f"Ingresaste {iguales_a_cero} numeros iguales a cero")