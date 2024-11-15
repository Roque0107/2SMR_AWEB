#Roque Morales Grimaldi
num1 = int(input("Escriba un número entero "))
num2 = int(input("Escriba otro número entero "))


inicio = min(num1, num2)
fin = max(num1, num2)


if inicio != fin:
    lista = list(range(inicio + 1, fin))
else:
    lista = []

print("Lista de menor a mayor ", lista)