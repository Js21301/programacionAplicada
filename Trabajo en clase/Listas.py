my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']
#input()
print(my_lista)
print(type(my_lista))
print(my_lista[2])
my_lista.append('Blanco')      #Agrega elemento al final de la lista
print(my_lista)
my_lista.insert(3, 'Negro')
print(my_lista)
my_lista.extend(['Marron', 'Gris'])   #Concatena a otra lista
print(my_lista)
print(my_lista.index('Azul'))
print(my_lista.pop()) #Elimina el ultimo elemento
size = len(my_lista)
print("size = ", size)
#print(my_lista.pop(size))
my_tupla = tuple(my_lista)
print()
print()
print("my_tuple: ", my_tupla)

print(my_tupla[0])
print(my_tupla[2])
