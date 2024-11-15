numero = input ("Escriba un número mayor que cero ")

numero = int(numero)

if numero > 0:
    for n2 in range(1, (numero + 1)):
        if numero % 2 == 0:
            print("Los divisores de" + str (numero) +"son " (list(n2)))

else:
    print("Necesito un numero mayor que cero, espabila")
