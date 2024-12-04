vocales = "AEIOU"
while True:
    letra = input("Ingresa una letra\n espacio para salir: ")
    if letra == " ":
        break
    else: 
        if letra.upper() in vocales:
            print("Es una Vocal")
        else:
            print("No es una vocal")