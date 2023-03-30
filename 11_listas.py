primera_lista = ["Manzana", "Banano"]
print(primera_lista)
nombres = ['Diego', 'Kelly', 'Liam']
print('Tipo de dato lista nombres')
print(type(nombres))

lista1 = [2,4,89,1000, 3.14]
print(lista1)    
lista2 = ['a', 123, 'A', 3.1416, 'Palabra', True, 1000]
print(lista2)
# Los valores de tipo bool, int, float no es necesario colocarlos dentro de comillas únicamente los datos de tipo str
print(len(lista2)) # en este caso la función len se utiliza para determinar cuantos elementos tiene la lista.
print(len(lista1))

# Otra lista
num = [1,2,3,4,5]
print(num)  
# La función lista nos permite convertir un conjunto de datos a lista.
num2 = list((1,2,3,4,5))
print(num2)
 # las listas si permiten quitar algún dato, modificar valores de datos y agregar algún dato, por el caso de las tuplas esto no es posible. A esto se le llama en programación mutar.

print('index list:')
print(num[0])
print(num[0:3])
print(num[-1::-1])

print('Uso de la función IN:')
print(3 in num)
print(10 in num)
print(num is num2) # Relación del mismo espacio en memoria de la lista que sería diferente a preguntar num == num2





