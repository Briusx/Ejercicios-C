oracion = input("Escribe algo para contar las vocales")
string = oracion.lower()
print (string)
count = 0
vocales = ["a", "e", "i", "o", "u"]
for char in string:
    if char in vocales:
        count = count+1

print ("el número de vocales es", count)
