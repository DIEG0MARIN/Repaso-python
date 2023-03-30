num = [99, 34, 25, 56, 72]
print(num)
# cambiar valor de una lista
num[1] = 88
print(num)

# Función INSERT
# num = [99,88,25,56,72]
print("Función Insert")
num.insert(1, 77)  # Adiciona el valor a la lista en el lugar que se le indica
print(num)

# Función APPEND:
# num = [99,77,88,25,56,72]
print('Función append')
num.append(100)
print(num)
# num = [99,77,88,25,56,72,100] agrega el valor al final de la lista

#FUNCION EXTEND
print('función extend')
frutas = ['Manzana', 'Pera', 'Uvas', 'Sandia']
num.extend(frutas)
print(num)  # agregar una lista a otra.

# Borrar elementos de una lista
# Funcion REMOVE para el caso de remove lo que va dentro del parentesis lo que debe ir es el valor el cual deseamos eliminar.
print("Función remove")
num.remove(100)
print(num)

# Función pop
# Dentro de los parametros que establce la funcion pop lo que va dentro del parentesis es la posición indice donde del elemento que se va a eliminar. En este caso eliminaremos el 88 , que se encuentra en la posición 2.
# num = [99,77,88,25,56,72,'Manzana ', 'Pera', 'Uvas', 'Sandia']
num.pop(2)
print(num)
#[99,77,25,56,72,'Manzana ', 'Pera', 'Uvas', 'Sandia']

# Función DEL
del num[0]
print(num)
#[99,77,25,56,72,'Manzana ', 'Pera', 'Uvas', 'Sandia']

# Función CLEAR: esta función borra todo lo que hay dentro de la lista.
num1 = [1, 4, 7, 10, 13, 15, 17]
num1.clear()
print(num1)







# revisar con mas tiempo la clase del 22
