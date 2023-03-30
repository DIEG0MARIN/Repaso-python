#Operaciones relacionales o de comparación
# TRUE / False
"""number = int(input("Digite un número "))
print(number > 3)
print(number >= 3)
print(number <= 3)
print(number < 3)
print(number==3)
print(number!=3)"""

#Operaciones lógicas
print("operaciones lógicas.")
# Conjunción(and,&)
print(True and True)
print(True and False)
print(False and True)
print(False and False)
#DISYUNCION (or, |)
print("Operaciones con el operador or")
print(True | True)
print(True | False)
print(False | True)
print(False | False)
#NEGACION (not, )
print("Operaciones con el operador not")
print(not (True | True))
print(not (True & False))
print(not (False | True))
print(not (False & False))

# OR exclusiva (^)
print("Or exclusiva")
print(True ^ True)
print(True ^ False)  # Para este caso da verdadero

# OPERACIONES DE PERTENENCIA
#in
print("Operador in")
nombre = "Diego Marin"
print("D" in nombre)
print("l" in nombre)
